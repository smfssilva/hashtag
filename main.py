import pandas as pd
from twilio.rest import Client

account_sid = "AC3f920516d3d046cf1a9c0be5eeb97495"
auth_token = "7158a8bedcbc9548ce519c5084a2339f"
client = Client(account_sid, auth_token)

# TODO: Instalar:
# pandas
# openpyxl
# twilio


# TODO: Passo a passo da solução.

# TODO: Abrir os 6 arquivos do excel.
lista_meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho"]
for mes in lista_meses:
    tabela_vendas = pd.read_excel(f"{mes}.xlsx")
    # TODO: Para cada arquivo:

    # TODO: ParVerificar se algum valor na coluna vendas daquele arquivo é maior que 55.000
    # TODO: Se for maior que 55.000 -> enviar um sms com o Nome, o mês e as vendas do vendedor.
    if (tabela_vendas["Vendas"] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas["Vendas"] > 55000, "Vendedor"].values[0]
        vendas = tabela_vendas.loc[tabela_vendas["Vendas"] > 55000, "Vendas"].values[0]
        print(f"No mês {mes} alguem bateu a meta.\nVendedor: {vendedor}\nVendas: {vendas}")
        message = client.messages.create(
            to="+5582987576704",
            from_ = "+18584139877",
            body = f"No mês {mes} alguem bateu a meta.\nVendedor: {vendedor}\nVendas: {vendas}"
        )
        print(message.sid)

    # TODO: Caso não seja maior que 55.000 não quero fazer nada.




