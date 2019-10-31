# hangman game
import random

HANGMAN_PICS = ['''
+---+
  |
  |
  |
  ===''','''
+---+
O  |
   |
   |
   ===''','''
+---+
O  |
|  |
   |
   ===''','''
+---+
 O  |
/|  |
    |
    ===''','''
+---+
 O  |
/|\ |
    |
    ===''','''
+---+
 O  |
/|\ |
/   |
    ===''','''
+---+
 O  |
/|\ |
/'\ |
    ===''']

words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

def ambilKataAcak(listKata):
  # fungsi ini memilih kata dari list kata yang diberikan
  indexKata = random.randint(0,len(listKata) -1)
  return listKata[indexKata]

def tampilkanPapan(hurufKurang, hurufBenar, kataRahasia):
  print(HANGMAN_PICS[len(hurufKurang)])
  print()

  print('Huruf yang salah: ', end='')
  for huruf in hurufKurang:
    print(huruf, end='')
  print()

  blanks = '*' * len(kataRahasia)

  for i in range(len(kataRahasia)):
    if kataRahasia[i] in hurufBenar:
      blanks = blanks[:i] + kataRahasia[i] + blanks[i+1:]

  for huruf in blanks:
    print(huruf, end='')
  print()

def ambilTebakan(sudahTertebak):
  while True:
    print('Tebak 1 huruf:')
    tebak = input()
    tebak = tebak.lower()

    if len(tebak) != 1:
      print('Silahkan ketik 1 huruf saja !')
    elif tebak in sudahTertebak:
      print('Kamu sudah menebak huruf itu. Pilih yang lain.')
    elif tebak not in 'abcdefghijklmnopqrstuvwxyz':
      print('Silahkan ketik huruf saja !')
    else:
      return tebak

def bermainLagi():
  print('Mau bermain lagi? (yes or no)')
  return input().lower().startswith('y')

print(' H A N G M A N')
hurufKurang = ''
hurufBenar = ''
kataRahasia = ambilKataAcak(words)
gameIsDone = False

while True:
  tampilkanPapan(hurufKurang, hurufBenar, kataRahasia)

  hurufTebakan = ambilTebakan(hurufKurang + hurufBenar)

  if hurufTebakan in kataRahasia:
    hurufBenar = hurufBenar + hurufTebakan

    semuaSudahTertebak = True
    for i in range(len(kataRahasia)):
      if kataRahasia[i] not in hurufBenar:
        semuaSudahTertebak = False
        break

    if semuaSudahTertebak:
      print('Yes ! kata rahasianya adalah : ' + kataRahasia + ', dan kamu MENANG !')
      gameIsDone = True
  else:
    hurufKurang = hurufKurang + hurufTebakan

    if (len(hurufKurang) == len(HANGMAN_PICS) -1):
      tampilkanPapan(hurufKurang, hurufBenar, kataRahasia)
      print('Kamu kehabisan kesempatan !\nSetelah' + str(len(hurufKurang)) + ' salah tebak dan ' + str(len(hurufBenar)) + 'tebakan benar, kata rahasianya adalah: ' + kataRahasia)

      gameIsDone = True

  if gameIsDone:
    if bermainLagi():
      hurufKurang = ''
      hurufBenar = ''
      gameIsDone = False
      kataRahasia = ambilKataAcak(words)
    else:
      break
