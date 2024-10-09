import tkinter as tk
from tkinter import filedialog, messagebox
import pdfplumber
import os
import re
from datetime import datetime
from pdf2image import convert_from_path
import pytesseract
import hashlib
import fitz  
import shutil

def extrair_data_com_pdfplumber(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            texto = page.extract_text()
            if texto:
                match = re.search(r'(\d{2}/\d{2}/\d{4})', texto)
                if match:
                    return match.group(1)
    return None

def extrair_data_com_ocr(pdf_path):
    imagens = convert_from_path(pdf_path)
    for imagem in imagens:
        texto = pytesseract.image_to_string(imagem)
        match = re.search(r'(\d{2}/\d{2}/\d{4})', texto)
        if match:
            return match.group(1)
    return None

def extrair_data_pagamento(pdf_path):
    data = extrair_data_com_pdfplumber(pdf_path)
    if data:
        return data

    return extrair_data_com_ocr(pdf_path)

def calcular_hash_arquivo(caminho_pdf):
    hasher = hashlib.md5()
    with open(caminho_pdf, 'rb') as file:
        buf = file.read()
        hasher.update(buf)
    return hasher.hexdigest()

def arquivos_sao_iguais(arquivo1, arquivo2):
    return calcular_hash_arquivo(arquivo1) == calcular_hash_arquivo(arquivo2)

def renomear_arquivos_por_data(diretorio):
    arquivos_processados = {}

    for arquivo in os.listdir(diretorio):
        if arquivo.lower().endswith('.pdf'):
            caminho_pdf = os.path.join(diretorio, arquivo)
            data_pagamento = extrair_data_pagamento(caminho_pdf)

            if data_pagamento:
                data_formatada = datetime.strptime(data_pagamento, '%d/%m/%Y').strftime('%Y-%m-%d')
                novo_nome = f'{data_formatada}.pdf'
                caminho_novo_arquivo = os.path.join(diretorio, novo_nome)

                if data_formatada in arquivos_processados:
                    arquivo_existente = arquivos_processados[data_formatada]
                    if arquivos_sao_iguais(caminho_pdf, arquivo_existente):
                        os.remove(caminho_pdf)
                        print(f'Arquivo duplicado removido: {arquivo}')
                    else:
                        print(f'Erro: o arquivo {novo_nome} já existe com conteúdo diferente.')
                else:
                    try:
                        os.rename(caminho_pdf, caminho_novo_arquivo)
                        arquivos_processados[data_formatada] = caminho_novo_arquivo
                        print(f'Arquivo renomeado: {arquivo} -> {novo_nome}')
                    except FileExistsError:
                        print(f'Erro: o arquivo {novo_nome} já existe.')
                    except Exception as e:
                        print(f'Erro ao renomear {arquivo}: {e}')
            else:
                print(f'Data não encontrada no arquivo: {arquivo}')

    messagebox.showinfo("Sucesso", "Holerites renomeados com sucesso! ✔")

def ordenar_pdfs_por_nome(pasta_dos_pdfs):
    arquivos_pdf = [os.path.join(pasta_dos_pdfs, f) for f in os.listdir(pasta_dos_pdfs) if f.lower().endswith('.pdf')]
    arquivos_pdf_ordenados = sorted(arquivos_pdf)
    return arquivos_pdf_ordenados

def combinar_pdfs_pymupdf(pdfs_ordenados, arquivo_saida):
    try:
        pdf_documento = fitz.open()
        for caminho_pdf in pdfs_ordenados:
            try:
                pdf_atual = fitz.open(caminho_pdf)
                pdf_documento.insert_pdf(pdf_atual)
                pdf_atual.close()
            except Exception as e:
                print(f"Erro ao ler o PDF '{caminho_pdf}': {e}")
        pdf_documento.save(arquivo_saida)
        pdf_documento.close()
        print(f"PDFs combinados com sucesso em: {arquivo_saida}")
    except Exception as e:
        print(f"Erro ao salvar o arquivo combinado: {e}")

def processar_arquivos():
    diretorio = filedialog.askdirectory(title="Selecione a pasta com os holerites")
    if diretorio:
        renomear_arquivos_por_data(diretorio)

        nome_da_pessoa = os.path.basename(diretorio)
        arquivo_saida_local = os.path.join(diretorio, f"HOLERITES COMPLETOS {nome_da_pessoa}.pdf")
        pdfs_ordenados = ordenar_pdfs_por_nome(diretorio)
        combinar_pdfs_pymupdf(pdfs_ordenados, arquivo_saida_local)

        messagebox.showinfo("Sucesso", "Processo completo! Holerites renomeados e combinados com sucesso! ✔")

app = tk.Tk()
app.title("Renomear e Combinar Holerites")

frame = tk.Frame(app, padx=20, pady=20)
frame.pack(padx=10, pady=10)

label = tk.Label(frame, text="Renomear e Combinar Holerites", font=("Arial", 14))
label.pack(pady=10)

botao = tk.Button(frame, text="Selecionar Pasta", command=processar_arquivos, width=20, height=2)
botao.pack(pady=10)

app.geometry("400x200")
app.mainloop()
