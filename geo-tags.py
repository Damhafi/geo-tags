import os
import piexif
from PIL import Image

def convert_to_dms(degree, ref):
    """Converte coordenadas decimais para formato DMS (graus, minutos, segundos)."""
    d = int(abs(degree))
    m = int((abs(degree) - d) * 60)
    s = int(((abs(degree) - d) * 60 - m) * 60 * 100)
    if degree < 0:
        ref = {'N': 'S', 'E': 'W'}[ref]
    return ((d, 1), (m, 1), (s, 100)), ref

def get_unique_output_path(output_path):
    """Verifica se o arquivo já existe. Se sim, adiciona um sufixo (1), (2), etc."""
    base, extension = os.path.splitext(output_path)
    counter = 1
    new_output_path = output_path
    while os.path.exists(new_output_path):
        new_output_path = f"{base}({counter}){extension}"
        counter += 1
    return new_output_path

def add_metadata(image_path, output_path, geotags, keywords, description):
    """Adiciona geotags, palavras-chave e descrição a uma imagem."""
    img = Image.open(image_path)

    # Verificar se a imagem tem EXIF e carregar
    exif_data = img.info.get("exif")
    if exif_data:
        exif_dict = piexif.load(exif_data)  # Se houver EXIF, carrega normalmente
    else:
        # Criar um dicionário EXIF básico se não houver EXIF na imagem
        exif_dict = {
            "0th": {},  # Metadados principais
            "Exif": {},  # Dados EXIF
            "GPS": {},  # Dados GPS
            "Interop": {},  # Dados de interoperabilidade
            "1st": {}  # Outras informações
        }

    # Adicionar geotags (coordenadas)
    latitude, lat_ref = convert_to_dms(geotags['latitude'], 'N')
    longitude, lon_ref = convert_to_dms(geotags['longitude'], 'E')

    gps_ifd = {
        piexif.GPSIFD.GPSLatitude: latitude,
        piexif.GPSIFD.GPSLatitudeRef: lat_ref,
        piexif.GPSIFD.GPSLongitude: longitude,
        piexif.GPSIFD.GPSLongitudeRef: lon_ref,
    }
    exif_dict['GPS'] = gps_ifd

    # Adicionar palavras-chave e descrição
    user_comment = f"Keywords: {', '.join(keywords)} | Description: {description}"
    exif_dict['Exif'][piexif.ExifIFD.UserComment] = user_comment.encode('utf-8')

    # Verificar se o arquivo de saída já existe e, se necessário, adicionar sufixo
    output_path = get_unique_output_path(output_path)

    # Salvar imagem com metadados
    exif_bytes = piexif.dump(exif_dict)
    img.save(output_path, "jpeg", exif=exif_bytes)

    print(f"Imagem salva como: {output_path}")

# Caminho da imagem e outros dados
image_path = r"............."
output_path = r"............."
geotags = {"latitude": ..........., "longitude": ........}  # Coordenadas
keywords = [".............."]
description = "........."

# Adicionar metadados à imagem
add_metadata(image_path, output_path, geotags, keywords, description)
