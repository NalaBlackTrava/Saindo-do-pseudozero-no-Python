from ast import If
from msilib.schema import Condition
import pandas as pd
from twilio.rest import Client

account_sid = "AC95b45026db107ed681e049d4988d3d49"
auth_token  = "13464e8cf85fc6535e963693275f87dc"
client = Client(account_sid, auth_token)

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel (f'{mes}.xlsx')
    if (tabela_vendas['Vendas']> 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas']> 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas']> 55000, 'Vendas'].values[0]
        message = client.messages.create(
            to="+55011971483509", 
            from_="+19126003150",
            body=f'No mês de {mes}, {vendedor} vendeu R$ {vendas},00, ou seja, bateu a meta.\n \n  Uffas, agora que o chefe financiou um novo apê na Barra, vc vai poder viajar... ☭\n  Continue assim e quem sabe ele passa uma Panamera ano que vem :)\n')
