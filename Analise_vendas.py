
import pandas as pd

# Dados fictícios de vendas
dados = {
    "Produto": ["Notebook", "Mouse", "Teclado", "Monitor", "Headset"],
    "Quantidade": [5, 20, 15, 7, 10],
    "Preço": [3500, 80, 150, 900, 200]
}

# Criar DataFrame
df = pd.DataFrame(dados)

# Criar coluna de faturamento
df["Faturamento"] = df["Quantidade"] * df["Preço"]

print("📊 Tabela de Vendas:")
print(df)

total = df["Faturamento"].sum()
print("\n💰 Total de faturamento:", total)
