import pandas as pd

data = {
    'Hari': ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu'],
    'Datang': [2, 3, 4, 1, 1, 5, 2],
    'Biaya': [30000*2, 35000*3, 25000*4, 15000*1, 20000*1, 30000*5, 35000*2],
    'Mahasiswa': ['Ani', 'Budi', 'Jono', 'Lono', 'Joni', 'Ani', 'Budi']
}
df = pd.DataFrame(data)
rata_rata_datang = df['Datang'].mean()
biaya_tertinggi_hari = df.loc[df['Biaya'].idxmax(), 'Hari']
biaya_tertinggi = df['Biaya'].max()
hari_biaya_lebih_110000 = df[df['Biaya'] > 110000]['Hari'].tolist()
mahasiswa_terbanyak = df['Mahasiswa'].value_counts().idxmax()
datang_minggu = df.loc[df['Hari'] == 'Minggu', 'Mahasiswa'].values[0]
biaya_terendah = df['Biaya'].min()
frekuensi_tertinggi = df['Datang'].max()
frekuensi_terendah = df['Datang'].min()

print(f"a) Rata-rata mahasiswa datang pada minggu ini: {rata_rata_datang:.2f}")
print(f"b) Biaya tertinggi terjadi pada hari: {biaya_tertinggi_hari} dengan biaya {biaya_tertinggi}")
print(f"c) Hari dengan biaya lebih dari 110000: {', '.join(hari_biaya_lebih_110000)}")
print(f"d) Mahasiswa yang paling banyak datang ke kampus: {mahasiswa_terbanyak}")
print(f"e) Mahasiswa yang datang pada hari Minggu: {datang_minggu}")
print(f"f) Biaya tertinggi: {biaya_tertinggi}, Biaya terendah: {biaya_terendah}")
print(f"g) Frekuensi datang tertinggi: {frekuensi_tertinggi}, Frekuensi datang terendah: {frekuensi_terendah}")
