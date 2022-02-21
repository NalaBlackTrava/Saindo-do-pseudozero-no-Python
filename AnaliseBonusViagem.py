from ast import If
from msilib.schema import Condition
import pandas as pd

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    print(mes)
    tabela_vendas = pd.read_excel (f'{mes}.xlsx')
    print (tabela_vendas)
    If (tabela_vendas:['Vendas']> 550000).any():
        print('Uffas, agora tu pode viajar, seu chefe financiou um novo ape na Barra')


#If X > 55k --> envia um SMS com o nome, o mês e as vendas delu

#Else --> nothing 
