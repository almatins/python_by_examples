# lets guess the number

# import random
import random

# berapa kali user melakukan tebakan
jumlahTebakan = 0

# tanya nama user
print('Hello, Siapa namamu?')

# simpan nama user
namaUser = input()

# nomor acak
nomorAcak = random.randint(1,20)
print('Hey, aku sedang memikirkan nomor antara 1 sampai 20, coba tebak?!')

# cek jumlah tebakan, maksimal hanya bisa menebak 6x saja
for jumlahTebakan in range(6):
  print('Berapa angka tebakanmu?')
  # tebakan masih dalam bentuk string
  tebakan = input()
  # ubah tebakan ke type integer, supaya bisa dibandingkan
  tebakan = int(tebakan)

  if tebakan < nomorAcak:
    # tebakan salah, jika tebakan lebih kecil dari 6, ulangi
    print('Angka tebakanmu terlalu kecil!')

  if tebakan > nomorAcak:
    # tebakan salah, jika tebakan lebih kecil dari 6, ulangi
    print('Angka tebakanmu terlalu besar!')

  if tebakan == nomorAcak:
    # tebakan benar ... keluar dari loop for
    break

# setelah 6 kali menebak
if tebakan == nomorAcak:
  # tebakan benar
  jumlahTebakan = str(jumlahTebakan + 1)
  print('Kerja Bagus, ' + namaUser + '! Kamu menebak angka saya dalam ' + jumlahTebakan + ' kali tebakan!')

if tebakan != nomorAcak:
  # tebakan salah
  nomorAcak = str(nomorAcak)
  print('Salah ! nomor yang aku pikirkan adalah ' + nomorAcak + '.')
