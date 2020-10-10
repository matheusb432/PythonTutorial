import openpyxl as xl
from openpyxl.chart import BarChart, Reference

# Importando duas classes ( ^            ^ ) de do arquivo chart.py de openpyxl

wb = xl.load_workbook('transactions.xlsx')  # Carregando o workbook transactions.xlsx no objeto wb
sheet = wb['Sheet1']
cell = sheet['c2']
# cell = sheet.cell(1, 1) eh o mesmo que sheet['a1']
# range(x, y) retorna valores de x ate (y-1), logo, necessario usar sheet.max_row + 1
for row in range(2, sheet.max_row + 1):
    cell = sheet.cell(row, 3)  # armazenando os valores de cada linha no objeto cell
    corrected_price = cell.value * 0.9  # Reduzindo 10% de todos os precos da coluna e armazenando em corrected_price
    corrected_price_cell = sheet.cell(row, 4)  # definindo as colunas nesse objeto
    corrected_price_cell.value = corrected_price  # Finalmente, definindo os novos valores na celula em questao.
    # print(cell.value)  # Printando toda a terceira coluna ( nesse caso, a coluna de precos )

# Selecionando as celulas da linha 2 ate 4 na coluna 4
# E armazenando no objeto values ( estamos instanciando a classe Reference )
values = Reference(sheet,
                   min_row=2,
                   max_row=sheet.max_row,
                   min_col=4,
                   max_col=4)
# Obs; o objeto so esta definido assim para facilitar a legibilidade do codigo.

chart = BarChart()
chart.add_data(values)
sheet.add_chart(chart, 'e2')


# Salvando o arquivo em um novo arquivo excel, para nao correr o risco de perder o arquivo no evento de um bug.
wb.save('transactions2.xlsx')
