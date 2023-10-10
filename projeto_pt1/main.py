import pdfplumber
import pandas as pd
import re

# espera o caminho/nome do arquivo .pdf

with pdfplumber.open('pedido_notebook.pdf') as pdf:

# Pegando apenas a primeira pagina do arquivo

    page_number = 0 

# ele diz que a 'page' é o meu arquivo pdf na pagina definida acima (seleciona a pagina que deseja ler, possivel usar for para pegar todas)

    page = pdf.pages[page_number]

# Extrai o texto do arquivo

    text = page.extract_text()

# Encontra as palavras-chave no arquivo pdf, (\w+) - para encontrar apenas uma palavra,
# (\s+) para encontrar espaços e 
# (.*) para encontrar tudo até o fim da linha
        
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

# Define o header/colunas da tabela

    header = ["Nome", "Modelo", "Quantidade", "Especificações", "Pagamento", "Endereço"]

# Cria uma linha com os dados encontrados

    dados = [nome[1], modelo[1], qtd[1], especs[1], pay[1], endr[1]]

# Cria um df com as colunas definidas em 'header' e as informações encontradas em 'dados', 
# é possivel fazer um looping for e usar uma lista para adicionar mais dados, 
# mesma logica usada no scraping HTML

    arquivo = pd.DataFrame([dados],columns=header)

# transforma o df em um arquivo excel.

    arquivo.to_excel("arquivo.xlsx")
    
    print("Scraping concluido!")
