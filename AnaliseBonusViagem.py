from ast import If
from msilib.schema import Condition
import pandas as pd

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel (f'{mes}.xlsx')
    if (tabela_vendas['Vendas']> 55000).any():
        print(f'No mês {mes} teve ume trabalhador q vendeu mais de 55k, uffas, agora tu pode viajar, seu chefe financiou um novo ape na Barra')


#If X > 55k --> envia um SMS com o nome, o mês e as vendas delu

#Else --> nothing
