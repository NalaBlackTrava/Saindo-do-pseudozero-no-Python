from ast import If
from msilib.schema import Condition
import pandas as pd

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel (f'{mes}.xlsx')
    if (tabela_vendas['Vendas']> 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas']> 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas']> 55000, 'Vendas'].values[0]
        print(f'No mês de {mes}, {vendedor} vendeu R$ {vendas},00, ou seja, bateu a meta.\n \n  Uffas, agora que o chefe financiou um novo apê na Barra, vc vai poder viajar... ☭\n  Continue assim e quem sabe ele passa uma Panamera ano que vem :)\n')


#If X > 55k --> envia um SMS com o nome, o mês e as vendas delu

#Else --> nothing
