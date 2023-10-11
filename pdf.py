import pdfplumber
import pandas as pd
import re

with pdfplumber.open('pedido_notebook.pdf') as pdf:

    header = ["Nome", "Modelo", "Quantidade", "Especificações", "Pagamento", "Endereço"]
    linhas = []

    for i in range(len(pdf.pages)):

        page = pdf.pages[i]
        text = page.extract_text()

        nome = re.search(r'nome:\s*(.*)', text, re.IGNORECASE)
        modelo = re.search(r'Modelo do Notebook:\s*(.*)', text, re.IGNORECASE)
        qtd = re.search(r'Quantidade:\s*(.*)', text, re.IGNORECASE)
        especs = re.search(r'Especificações:\s*(.*)', text, re.IGNORECASE)
        pay = re.search(r'Método de Pagamento:\s*(.*)', text, re.IGNORECASE)
        endr = re.search(r'Endereço de Entrega:\s*(.*)', text, re.IGNORECASE)

        print(nome[1])
        print(modelo[1])
        print(qtd[1])
        print(especs[1])
        print(pay[1])
        print(endr[1])

        dados = [nome[1], modelo[1], qtd[1], especs[1], pay[1], endr[1]]

        linhas.append(dados)

    arquivo = pd.DataFrame(linhas,columns=header)
    arquivo.to_excel("arquivo.xlsx")
    print("Scraping concluido!")

