import openpyxl
import re

def format_xlsx():
    # Carregue o arquivo Excel
    workbook = openpyxl.load_workbook('./../PlanilhaSemFormatacao.xlsx')

    # Selecione a planilha desejada
    worksheet = workbook['Sheet1']

    # Defina uma lista com o nome das colunas que deseja formatar
    colunas = ['B', 'D', 'F',  'H', 'J']

    # Percorra todas as colunas desejadas e remova os números
    for coluna in colunas:
        # Selecione a coluna pelo cabeçalho
        col = worksheet[coluna]
        # Percorra as células na coluna e remova os números
        for cell in col:
            if cell.value is not None:
                cell.value = re.sub(r'[^\w\s]|[\d]', '', str(cell.value))

    colunas = ['C', 'E', 'G', 'I']

    # Percorra todas as colunas desejadas e remova tudo que não é número
    for coluna in colunas:
        # Selecione a coluna pelo cabeçalho
        col = worksheet[coluna]
        # Percorra as células na coluna e remova tudo que não é número
        for cell in col[1:]:
            if cell.value is not None:
                cell.value = re.sub(r'[^\d.\/\-]', '', str(cell.value))

    # Salve o arquivo Excel formatado
    workbook.save('./../ResultadoFinal.xlsx')

format_xlsx()