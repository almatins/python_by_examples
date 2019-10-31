# permainan gua naga
import random
import time

# menampilkan intro
def tampilkanIntro():
  print('''Kamu sedang berada di pulau yang penuh dengan Naga.
  Di depanmu, ada 2 goa. Di salah satu goa, ada Naga yang baik,
  yang mau berbagi harta karun bersamamu. Tapi, Naga yang satunya
  lagi adalah Naga yang sedang lapar, yang akan langsung memakanmu
  saat dia melihatmu!.''')
  print()

# biarkan user memilih goa
def pilihGoa():
  goa = ''
  while goa != '1' and goa != '2':
    print('Pilih salah satu, Goa 1 atau Goa 2?')
    goa = input()

  return goa

# periksa goa pilihan user
def periksaGoa(goaYangDipilih):
  print('Kamu memilih masuk ke goa nomor ' + goaYangDipilih)
  time.sleep(2)
  print('Goa ini sangat gelap dan menakutkan !')
  time.sleep(2)
  print('''Seekor Naga yang sangat BESAR tiba-tiba melompat di hadapanmu !
        lalu Dia membuka mulutnya dan kemudian ...''')
  print()
  time.sleep(2)

  # goa yang bagus, random
  goaYangBagus = random.randint(1,2)

  # cek goa pilihan user, apakah goa yang bagus?
  if goaYangDipilih == str(goaYangBagus):
    print('memberikan harta karun yang banyak kepadamu !')
  else:
    print('Dia memakanmu hanya dalam 1 gigitan !')

# konfirmasi, apakah mau bermain lagi? default yes
# selama jawaban user yes atau y, loop while akan diulangi terus
bermainLagi = 'yes'
while bermainLagi == 'yes' or bermainLagi == 'y':
  tampilkanIntro()
  nomorGoa = pilihGoa()
  periksaGoa(nomorGoa)

  print('Mau bermain lagi? (yes or no)')
  bermainLagi = input()
