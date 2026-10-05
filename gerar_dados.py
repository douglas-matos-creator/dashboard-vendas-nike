import pandas as pd
import numpy as np

# Definir semente para dados reproduzíveis
np.random.seed(42)

n_registos = 500

produtos = ['Nike Air Force 1', 'Nike Air Max', 'Nike Pegasus', 'Nike Dunk Low', 'Nike Tech Fleece', 'Nike Pro Training']
categorias = ['Calçado', 'Calçado', 'Calçado', 'Calçado', 'Vestuário', 'Vestuário']
regioes = ['Norte', 'Sul', 'Este', 'Oeste']
mapa_categoria = dict(zip(produtos, categorias))

datas = pd.date_range(start='2025-01-01', end='2025-12-31', periods=n_registos)
prods = np.random.choice(produtos, size=n_registos)
cats = [mapa_categoria[p] for p in prods]
quantidades = np.random.randint(1, 6, size=n_registos)

precos_base = {
    'Nike Air Force 1': 110,
    'Nike Air Max': 150,
    'Nike Pegasus': 130,
    'Nike Dunk Low': 115,
    'Nike Tech Fleece': 140,
    'Nike Pro Training': 55
}

precos_unit = [precos_base[p] for p in prods]
receita_total = [q * p for q, p in zip(quantidades, precos_unit)]

df_nike = pd.DataFrame({
    'ID_Pedido': [f'NKE-{1000 + i}' for i in range(n_registos)],
    'Data': datas.strftime('%Y-%m-%d'),
    'Produto': prods,
    'Categoria': cats,
    'Regiao': np.random.choice(regioes, size=n_registos),
    'Quantidade': quantidades,
    'Preco_Unitario': precos_unit,
    'Receita_Total': receita_total
})

df_nike.to_csv('vendas_nike.csv', index=False)
print("Ficheiro 'vendas_nike.csv' criado com sucesso!")
