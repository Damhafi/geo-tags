import piexif
from PIL import Image

def read_exif(image_path):
    """Lê e exibe os metadados EXIF de uma imagem."""
    img = Image.open(image_path)

    # Obter os dados EXIF
    exif_data = img.info.get("exif")
    if exif_data:
        exif_dict = piexif.load(exif_data)
        # Exibir as informações EXIF
        print("Metadados EXIF da imagem:")
        for ifd_name in exif_dict:
            print(f"IFD: {ifd_name}")
            if exif_dict[ifd_name]:  # Verificar se existe dados antes de iterar
                for tag, value in exif_dict[ifd_name].items():
                    tag_name = piexif.TAGS[ifd_name].get(tag, {}).get('name', 'Unknown')
                    print(f"  {tag_name} : {value}")
            else:
                print(f"  Sem dados para o IFD: {ifd_name}")
    else:
        print("Sem dados EXIF.")

# Caminho da imagem com metadados adicionados
output_path = r"..................."   # Atualize com o caminho correto

# Verificar os metadados da imagem
read_exif(output_path)
