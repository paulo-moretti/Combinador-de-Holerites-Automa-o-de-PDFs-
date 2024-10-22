Extrator de Holerites

Este repositório contém um script Python avançado que processa e extrai dados de folhas de pagamento em formato PDF (clicavel), utilizando a biblioteca pdfplumber. O script é especializado em lidar com folhas de pagamento de funcionários aposentados, e extrai informações importantes, como nome, categoria, total de vencimentos, e valores correspondentes a itens de interesse baseados em códigos específicos. Os resultados são calculados e acumulados por período, permitindo uma análise detalhada dos dados.

Funcionalidades:
Extração de dados do PDF; Usa o pdfplumber para ler PDFs de folhas de pagamento e extrair informações textuais.
Filtragem de informações relevantes; Captura dados como nomes, categorias, vencimentos e valores associados a códigos de interesse.
Cálculos de totais; Realiza cálculos para somar valores por período e aplicar regras personalizadas para combinar diferentes códigos.
Saída em formato JSON; Salva os dados processados em um arquivo JSON estruturado para fácil análise posterior.
Modularidade; Possibilidade de expandir ou personalizar facilmente a lógica para outros tipos de documentos ou códigos.

Pré-requisitos:
Certifique-se de ter o Python 3.7 ou superior instalado. Além disso, você precisará instalar as dependências necessárias para rodar o projeto.

Dependências:
As principais dependências do projeto são
pdfplumber; Para manipulação e extração de dados de arquivos PDF.
PyPDF2; (Opcional) Se houver necessidade de manipular os PDFs em níveis mais baixos.
pandas; Para manipulação de dados em formato de tabela e para cálculos de agregação.
json; Para salvar e carregar os dados extraídos.

Você pode instalar as dependências rodando:
pip install -r requirements.txt

Se não tiver um arquivo requirements.txt pronto, ele deve conter as seguintes linhas:
pdfplumber
PyPDF2
pandas

#COMO USAR#
Clone este repositório para sua máquina local:
"git clone https://github.com/paulo-moretti/Combinador-de-Holerites-Automacao-de-PDFs.git"

Acesse o diretório do projeto:
cd seu-repositorio
Certifique-se de que as dependências estão instaladas conforme mostrado na seção de "Dependências".
Coloque seus arquivos PDF na pasta apropriada (ou ajuste o caminho no script).
Execute o script principal:
python extrator_holerites.py
Os resultados serão salvos em um arquivo JSON no diretório de saída especificado.

Personalizando:
Se desejar adicionar novos códigos de interesse ou modificar as regras de cálculo, você pode ajustar as funções no script principal. O código está modularizado para que seja fácil realizar essas modificações.

Estrutura do Projeto:
├── extrator_folhas_pagamento.py   # Script principal para extração e processamento dos PDFs
├── utils.py                       # Funções auxiliares para manipulação de dados
├── requirements.txt               # Arquivo de dependências
├── README.md                      # Este arquivo
├── input/                         # Pasta onde os PDFs de entrada devem ser colocados
└── output/                        # Pasta onde os arquivos JSON serão salvos

Exemplos de Uso:
Você pode alterar o script para ajustar os dados que deseja extrair e os códigos de interesse. Abaixo está um exemplo de configuração simples
"codigos_de_interesse = ["123", "456", "789"]"

Além disso, você pode personalizar como os dados são acumulados por período, e como os diferentes códigos interagem entre si para gerar relatórios mais completos.

Contribuições:
Contribuições são bem-vindas! Se você encontrar problemas ou tiver sugestões de melhoria, sinta-se à vontade para abrir uma issue ou enviar um pull request.
