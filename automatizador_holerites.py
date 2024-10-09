import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pdfplumber
import os
import re
from datetime import datetime
from pdf2image import convert_from_path
import pytesseract
import hashlib
import fitz

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

def renomear_arquivos_por_data(diretorio, progress_bar=None):
    arquivos_processados = {}
    arquivos_pdf = [arquivo for arquivo in os.listdir(diretorio) if arquivo.lower().endswith('.pdf')]

    for i, arquivo in enumerate(arquivos_pdf, 1):
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
        
        if progress_bar:
            progress_bar['value'] = (i / len(arquivos_pdf)) * 50
            progress_bar.update()

def ordenar_pdfs_por_nome(pasta_dos_pdfs):
    arquivos_pdf = [os.path.join(pasta_dos_pdfs, f) for f in os.listdir(pasta_dos_pdfs) if f.lower().endswith('.pdf')]
    return sorted(arquivos_pdf)

def combinar_pdfs_pymupdf(pdfs_ordenados, arquivo_saida, progress_bar=None, inicio_progress=0):
    try:
        pdf_documento = fitz.open()
        total_pdfs = len(pdfs_ordenados)
        for i, caminho_pdf in enumerate(pdfs_ordenados, 1):
            try:
                pdf_atual = fitz.open(caminho_pdf)
                pdf_documento.insert_pdf(pdf_atual)
                pdf_atual.close()
            except Exception as e:
                print(f"Erro ao ler o PDF '{caminho_pdf}': {e}")
            
            if progress_bar:
                progress_bar['value'] = inicio_progress + (i / total_pdfs) * (100 - inicio_progress)
                progress_bar.update()

        pdf_documento.save(arquivo_saida)
        pdf_documento.close()
        print(f"PDFs combinados com sucesso em: {arquivo_saida}")
    except Exception as e:
        print(f"Erro ao salvar o arquivo combinado: {e}")

def processar_arquivos(opcao):
    diretorio = filedialog.askdirectory(title="Selecione a pasta com os holerites")
    if diretorio:
        progress_bar['value'] = 0
        progress_bar.update()

        if opcao == "renomear_e_juntar":
            renomear_arquivos_por_data(diretorio, progress_bar)
            inicio_progress_juncao = 50
        else:
            inicio_progress_juncao = 0

        nome_da_pessoa = os.path.basename(diretorio)
        arquivo_saida_local = os.path.join(diretorio, f"HOLERITES COMPLETOS {nome_da_pessoa}.pdf")
        pdfs_ordenados = ordenar_pdfs_por_nome(diretorio)
        combinar_pdfs_pymupdf(pdfs_ordenados, arquivo_saida_local, progress_bar, inicio_progress_juncao)

        progress_bar['value'] = 100
        progress_bar.update()

        messagebox.showinfo("Sucesso", "Processo completo! Holerites renomeados e combinados com sucesso! ✔" if opcao == "renomear_e_juntar" else "Processo completo! Holerites combinados com sucesso! ✔")

def abrir_menu_principal():
    menu_principal = tk.Toplevel(app)
    menu_principal.title("Escolha uma Opção")

    frame_menu = tk.Frame(menu_principal, padx=20, pady=20)
    frame_menu.pack(padx=10, pady=10)

    label_menu = tk.Label(frame_menu, text="Escolha uma Opção", font=("Arial", 14))
    label_menu.pack(pady=10)

    botao_renomear_juntar = tk.Button(frame_menu, text="Renomear e Juntar Holerites", command=lambda: processar_arquivos("renomear_e_juntar"), width=20, height=2)
    botao_renomear_juntar.pack(pady=5)

    botao_juntar = tk.Button(frame_menu, text="Somente Juntar Holerites", command=lambda: processar_arquivos("juntar"), width=20, height=2)
    botao_juntar.pack(pady=5)

app = tk.Tk()
app.title("Renomear e Combinar Holerites")

frame = tk.Frame(app, padx=20, pady=20)
frame.pack(padx=10, pady=10)

label = tk.Label(frame, text="Renomear e Combinar Holerites", font=("Arial", 14))
label.pack(pady=10)

botao_iniciar = tk.Button(frame, text="Iniciar", command=abrir_menu_principal, width=20, height=2)
botao_iniciar.pack(pady=10)

progress_bar = ttk.Progressbar(app, orient="horizontal", length=300, mode="determinate")
progress_bar.pack(pady=10)

app.geometry("400x300")
app.mainloop()
