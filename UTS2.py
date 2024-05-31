import pandas as pd
import matplotlib.pyplot as plt

data = {
    'fakultas': ["Bisnis", "D3 Perhotelan", "ICT", "Ilmu Komunikasi", "Seni dan Desain"],
    'jumlah_mahasiswa': [260, 28, 284, 465, 735],
    'akreditasi': ["A", "A", "B", "A", "A"]
}
df = pd.DataFrame(data)

plt.figure(figsize=(10, 6))
plt.bar(df['fakultas'], df['jumlah_mahasiswa'], color=['red', 'yellow', 'green', 'blue', 'purple'])
plt.xlabel('Fakultas')
plt.ylabel('Jumlah Mahasiswa')
plt.title('Jumlah Mahasiswa per Fakultas')
plt.xticks(rotation=45)
plt.show()
