# Automatizador de Holerites:

Este projeto tem como objetivo automatizar o processo de extração de datas de pagamento de arquivos PDF de holerites e os renomeia de acordo, no formato AAAA/MM/DD. Utilizando bibliotecas como `pdfplumber`, `pytesseract`, e `tkinter`, ele permite a leitura de PDFs, extração de dados específicos, e a geração de saídas úteis a partir dos arquivos processados.

## Funcionalidades:

- Extração de datas e outros dados específicos de holerites em formato PDF.
- Utilização de OCR para reconhecimento de texto em PDFs que são imagens.
- Interface gráfica amigável para facilitar a escolha de arquivos e a visualização de resultados.
- Geração de hashes para verificação de integridade dos arquivos processados.

## Pré-requisitos:

Para rodar o projeto, você precisará instalar as seguintes dependências:

- Python 3.x
- pdfplumber
- pytesseract
- tkinter (geralmente já vem com a instalação do Python)
- pdf2image
- fitz (PyMuPDF)
Você pode instalar as dependências necessárias usando o "pip":
- pip install pdfplumber pytesseract pdf2image pymupdf

## Instale Tesseract OCR:

- Certifique-se de que o Tesseract OCR está instalado no seu sistema. Caso contrário, instale!

## Instalação

Clone este repositório para o seu ambiente local:
- git clone https://github.com/paulo-moretti/Combinador-de-Holerites-Automacao-de-PDFs.git
- cd Combinador-de-Holerites-Automacao-de-PDFs
Instale as dependências do projeto:
- pip install -r requirements.txt

## Uso

1. Execute o script principal para iniciar a interface gráfica:
python automatizador_holerites.py

2. Use a interface gráfica para:
Selecionar arquivos PDF de holerites.

3. Executar a extração de dados automaticamente.
Visualizar os resultados extraídos diretamente na interface.

## Extração de dados

O script utiliza as seguintes técnicas de extração:
- pdfplumber: Para extrair texto de PDFs baseados em texto.
- pytesseract: Para PDFs que são baseados em imagens, o OCR (reconhecimento óptico de caracteres) é utilizado para converter a imagem em texto.
- Geração de Hash: Após a extração dos dados, um hash é gerado para verificar a integridade dos arquivos processados.

## Interface Gráfica

A interface gráfica foi construída com Tkinter, permitindo que o usuário escolha facilmente os arquivos PDF que deseja processar e visualize os resultados diretamente na aplicação.

## Estrutura do Projeto

automatizador_holerites.py: Script principal que contém a lógica de extração de dados e a interface gráfica do usuário.
- pdfplumber: Usado para extrair texto de arquivos PDF.
- pytesseract: Utilizado para reconhecer texto em PDFs que são imagens.
- Tkinter: Interface gráfica para facilitar a seleção e o processamento dos arquivos.

## Contribuição

- Faça um fork do projeto.
- Crie um branch para sua nova feature (git checkout -b nova-feature).
- Commit suas mudanças (git commit -m 'Adiciona nova feature').
- Faça o push para o branch (git push origin nova-feature).
- Abra um pull request.

# Licença de Uso - Automatizador de Holerites

Este software ("Automatizador de Holerites") foi desenvolvido por Paulo Eduardo Moretti. Ao utilizar, modificar ou distribuir este software, você concorda com os seguintes termos:

## Permissões

- **Uso pessoal**: Você pode utilizar este software para uso pessoal e projetos próprios.
- **Modificações**: Você pode modificar o código-fonte para adaptar o software às suas necessidades, desde que as modificações sejam mantidas em caráter privado ou interno.
- **Distribuição**: Você pode distribuir o software original ou modificado, desde que mantenha esta licença incluída em todas as cópias distribuídas.

## Restrições

- **Uso comercial**: O uso deste software para fins comerciais é **proibido** sem a permissão explícita e por escrito do autor.
- **Garantias**: Este software é fornecido "como está", sem garantias de qualquer tipo. O autor não se responsabiliza por quaisquer danos ou problemas causados pela utilização deste software.
- **Atribuição**: Ao utilizar ou distribuir este software, você deve fornecer a devida atribuição ao autor original, Paulo Eduardo Moretti.

## Limitação de Responsabilidade

Em nenhuma hipótese o autor será responsável por qualquer dano direto, indireto, incidental, especial, exemplar ou consequente (incluindo, mas não se limitando a, aquisição de bens ou serviços substitutos; perda de uso, dados ou lucros; ou interrupção de negócios) decorrente de qualquer forma do uso deste software, mesmo que advertido da possibilidade de tais danos.

## Alterações e Revogação

O autor reserva-se o direito de alterar esta licença a qualquer momento, sem aviso prévio, desde que tal alteração seja devidamente registrada no repositório oficial do projeto. Esta licença poderá ser revogada a qualquer momento em caso de violação de quaisquer de seus termos.

---

© 2024 Paulo Eduardo Moretti. Todos os direitos reservados.
