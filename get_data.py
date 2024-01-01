import pandas as pd

nama_file = 'data.xlsx'
df = pd.read_excel(nama_file, header=None)

master_data = []

for index, row in df.iterrows():
    kolom1 = row[0]
    kolom2 = row[1]
    kolom3 = row[2]
    master_data.append(
        f"{kolom2}. {kolom3}"
    )