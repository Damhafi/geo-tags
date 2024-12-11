# Geo-Tags Python Script

Este script em Python permite adicionar e verificar metadados EXIF em imagens, incluindo geotags (coordenadas geográficas) e outras informações como palavras-chave e descrição. As variáveis podem ser facilmente ajustadas para diferentes imagens e coordenadas.

## Variáveis Importantes

### 1. **Caminho das Imagens**
O script precisa de dois caminhos de arquivo principais: o caminho da imagem de entrada (a qual você deseja adicionar metadados) e o caminho de saída (onde a imagem com metadados será salva).

- **`image_path`**: Caminho para a imagem original (sem metadados ou com metadados a serem atualizados).
  - Exemplo: `"C:/imagens/imagem_original.jpg"`

- **`output_path`**: Caminho para salvar a imagem com os metadados adicionados.
  - Exemplo: `"C:/imagens/imagem_com_metadados.jpg"`

Certifique-se de atualizar esses caminhos com o local correto onde suas imagens estão armazenadas.

### 2. **Geotags (Latitude e Longitude)**
As coordenadas geográficas (latitude e longitude) são inseridas como números decimais. A conversão para o formato de graus, minutos e segundos (DMS) será realizada automaticamente.

- **Latitude**: A coordenada da latitude. Para o Hemisfério Sul, use valores negativos (exemplo: `-19.8157`).
- **Longitude**: A coordenada da longitude. Para o Hemisfério Oeste, use valores negativos (exemplo: `-43.9417`).

### 3. **Conversão de Coordenadas**
As coordenadas decimais são convertidas para o formato DMS (graus, minutos, segundos), que é o formato padrão para metadados EXIF.

- **Hemisfério Norte e Leste**: Se a coordenada for positiva, o valor será convertido normalmente.
- **Hemisfério Sul e Oeste**: Se a coordenada for negativa, o valor será invertido para os respectivos hemisférios (S para Latitude e W para Longitude).

### 4. **Palavras-chave e Descrição**
- **`keywords`**: Uma lista de palavras-chave associadas à imagem. Elas são usadas como parte dos metadados EXIF.
  - Exemplo: `["Praia de Copacabana", "Rio de Janeiro", "verão"]`

- **`description`**: Uma descrição geral da imagem ou do local relacionado.
  - Exemplo: `"Vista da Praia de Copacabana, no Rio de Janeiro, durante o verão."`

Esses dados serão adicionados aos metadados EXIF sob o campo `UserComment`.

## Como Usar

### 1. **Verificar Metadados EXIF**
Para verificar os metadados de uma imagem, altere a variável `output_path` para o caminho da imagem que deseja inspecionar e execute o script. O comando `read_exif(image_path)` exibirá as informações EXIF da imagem.

### 2. **Adicionar Metadados EXIF**
Para adicionar ou atualizar os metadados EXIF, altere as variáveis `image_path`, `output_path`, `geotags`, `keywords`, e `description` conforme necessário e execute o script. Os novos metadados serão incorporados na imagem e o arquivo com os metadados será salvo no caminho especificado em `output_path`.
