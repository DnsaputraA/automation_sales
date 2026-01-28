import pandas as pd

# ganti path sesuai lokasi file kamu
df = pd.read_csv('data/daily_sales.csv')

# ganti nama kolom
df = df.rename(columns={
    'Order Date': 'date',
    'Sales': 'sales'
})

# simpan ulang ke CSV yang sama
df.to_csv('data/daily_sales.csv', index=False)

print("Berhasil ganti nama kolom dan menyimpan ulang.")
