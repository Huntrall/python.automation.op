import pandas as pd
import tabulate
df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22,35,58],
        "Sex": ["male", "male", "female"],
    }
)
df2 = pd.DataFrame(
    {
        "Provedor": ["Algar", "Pombonet", "Maxiweb"],
        "Qualidade": ["Ruim", "Médio", "Ótimo"],
        "Quantos Clientes Tem": ["1", "2", "5"]

    }
)

print(tabulate.tabulate(df2, headers='keys', tablefmt='fancy_grid', stralign='center'))