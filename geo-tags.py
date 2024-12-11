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

    # Salvar imagem com metadados
    exif_bytes = piexif.dump(exif_dict)
    img.save(output_path, "jpeg", exif=exif_bytes)

# Caminho da imagem e outros dados
image_path = r"........."
output_path = r"..............."
geotags = {"latitude": ..............., "longitude": ............}  # Coordenadas
keywords = [".........."]
description = ".................."

# Adicionar metadados à imagem
add_metadata(image_path, output_path, geotags, keywords, description)

print("Metadados adicionados com sucesso!")
