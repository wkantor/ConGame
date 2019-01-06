import sys
import time
import cmd
import os



"""
--------------
a1  a2  a3  a4
--------------
b1  b2  b3  b4
--------------
c1  c2  c3  c4
--------------
d1  d2  d3  d4
--------------
"""

### MIEJSCA ###

class Miejsca:
	NUMER = ''
	NAZWA = ''
	OPIS = ''
	DOSTYMP = ''

a1 = Miejsca()
a1.NUMER = 'A1'
a1.NAZWA = 'Mapa Pałacu'
a1.OPIS = 'Tu se możesz wybrać, kaj chcesz wyruszyć.'
a1.DOSTYMP = True

a2 = Miejsca()
a2.NUMER = 'A2'
a2.NAZWA = 'Hala Kontemplacji'
a2.OPIS = 'Tu sie nauczysz, jak kontemplować.' + 'Tu poznosz podstawy tej sztuki.'
a2.DOSTYMP = True

a3 = Miejsca()
a3.NUMER = 'A3'
a3.NAZWA = 'Komnata Oddech'
a3.OPIS = 'Tu sie spotkosz z mistrzym oddechu.' + 'Ón cie poprowaci do wglóndu do oddechu.'
a3.DOSTYMP = False

a4 = Miejsca()
a4.NUMER = 'A4'
a4.NAZWA = 'Komnata Ciała'
a4.OPIS = 'Tu sie spotkosz z mistrzym ciała.' + 'Ón cie poprowaci do wglóndu do ciała.'
a4.DOSTYMP = False

wszystki_miejsca1 = [a1,a2,a3,a4]

### MAPA PAŁACU ###

def mapa_pałacu():
	os.system("cls")
	print ('###########################################################################')
	print('# Numer: ' + a1.NUMER + '                                                               #')
	print ('# Nazwa: ' + a1.NAZWA + '                                                      #')
	print ('# Opis: ' + a1.OPIS + '                         #')
	print ('###########################################################################')
	print ('\n')
	mapa_talk1 = ('Narazie możesz weść do tych miejsc.\n\n')
	for character in mapa_talk1: 
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.05)
	
	print('###############')
	print('# ' + a1.NUMER + ' '+ a2.NUMER + ' '+ a3.NUMER + ' ' + a4.NUMER + ' ' + '#')
	print('###############\n')

	for komnata in wszystki_miejsca1:
		if komnata.DOSTYMP is False:
			continue
		else:
			print (komnata.NUMER+": "+komnata.NAZWA)


	wybór = ('')
	while wybór not in ['a1','a2']:
		wybór = input('> ')
		if wybór.lower() == ('a1'):
			mapa_pałacu()
		if wybór.lower() == ('a2'):
			hala_kontemplacji()

### HALA KONTEMPLACJI ###

a21 = Miejsca()
a21.NUMER = 'A21'
a21.NAZWA = 'Wstymp do kontemplacji'
a21.OPIS = 'Tu sie dowiysz teorie kontemplacji.'
a21.DOSTYMP = True

a22 = Miejsca()
a22.NUMER = 'A22'
a22.NAZWA = 'Ćwiczyni 1'
a22.OPIS = 'Piyrsze ćwiczyni kontemplacji.'
a22.DOSTYMP = False

wszystki_miejsca2 = [a21,a22]

def hala_kontemplacji():
	os.system("cls")
	print ('###########################################################################')
	print('# Numer: ' + a2.NUMER + '                                                               #')
	print ('# Nazwa: ' + a2.NAZWA + '                                                #')
	print ('# Opis: ' + a2.OPIS + ' #')
	print ('###########################################################################')
	print ('\n')
	a2_talk1 = ('Witej w Hali Kontemplacji!\nWybier se, kaj chcesz iść.\n\n')
	for character in a2_talk1: 
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.05)

	for komnata in wszystki_miejsca2:
		if komnata.DOSTYMP is False:
			continue
		else:
			print (komnata.NUMER+": "+komnata.NAZWA)

	print('(A1: Mapa Pałacu)')

	wybór2 = ('')
	while wybór2 not in ['a21','a22','home']:
		wybór2 = input('> ')
		if wybór2.lower() == ('a21'):
			wstymp_do_kontemplacji()
		if wybór2.lower() == ('a22'):
			piyrsze_ćwiczyni_kontemplaci() 
		if wybór2.lower() == ('a1'):
			mapa_pałacu()

### WSTYPMP DO KONTEMPLACJI###

def wstymp_do_kontemplacji():
	os.system("cls")
	print ('###########################################################################')
	print('# Numer: ' + a21.NUMER + '                                                              #')
	print ('# Nazwa: ' + a21.NAZWA + '                                           #')
	print ('# Opis: ' + a21.OPIS + '                               #')
	print ('###########################################################################')
	print ('\n')
	a21_talk1 = ('Przecztej se instrukje do kontemplacji.\n(Jak bejesz gotowy, napisz "ok".)\n\n')
	for character in a21_talk1: 
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.05)
	print('TU BEJE INSTRUKCJA.\n')


	wybór21 = input('> ')
	if wybór21 == ('ok'):
		a22.DOSTYMP = True
		a21_talk2 = ('\nTeraz mosz dostmpne A22!\n(Jak bejesz gotowy, napisz "ok".)\n\n')
		for character in a21_talk2: 
			sys.stdout.write(character)
			sys.stdout.flush()
			time.sleep(0.05)
	while wybór21 not in ['ok']:
			print('Nierozumiym... (Jak bejesz gotowy, napisz "ok".)\n')
			wybór21 = input('> ')
			if wybór21 == ('ok'):
				a22.DOSTYMP = True
				a21_talk2 = ('\nTeraz mosz dostmpne  A22!\n(Jak bejesz gotowy, napisz "ok".)\n\n')
				for character in a21_talk2: 
					sys.stdout.write(character)
					sys.stdout.flush()
					time.sleep(0.05)

		
	wybór22 = input('> ')
	if wybór22 == ('ok'):
		hala_kontemplacji()
	while wybór22 not in ['ok']:
		print('Nierozumiym... (Jak bejesz gotowy, napisz "ok".)\n')
		wybór22 = input('> ')
		if wybór22 == ('ok'):
			hala_kontemplacji()

### PIYRSZE ĆWICZYNI KONTEMPLACJI ###

def piyrsze_ćwiczyni_kontemplaci():
	os.system("cls")
	print ('###########################################################################')
	print('# Numer: ' + a22.NUMER + '                                                              #')
	print ('# Nazwa: ' + a22.NAZWA + '                                                       #')
	print ('# Opis: ' + a22.OPIS + '                                    #')
	print ('###########################################################################')
	print ('#                             5 minut                                     #')
	print ('#                     (napisz "***" aby przerwać)                         #')
	print ('\n')
	
	a22_talk1 = ('Kontempluj to zdani.\n\n"Co było w Puszce Pandory?"\n\n')
	for character in a22_talk1: 
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.05)
	
	timeout = 300
	timeout_start = time.time()
	while time.time() < timeout_start + timeout:
		kontemplacja22 = input('> ')
		if kontemplacja22 == ('***'):
			break

	a22_talk2 = ('\nKóniec! \n(Jak bejesz gotowy, napisz "ok")\n\n')
	for character in a22_talk2: 
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.05)

	wybór22 = input('> ')
	if wybór22 == ('ok'):
		hala_kontemplacji()
	while wybór22 not in ['ok']:
		print('Nierozumiym... (Jak bejesz gotowy, napisz "ok".)\n')
		wybór22 = input('> ')
		if wybór22 == ('ok'):
			hala_kontemplacji()

















### POCZÓNTEK ###


os.system("cls")

text1 = ('Witej w Pałacu Wglóndu!\n'+'Co cie tu sprowadzo?\n')
for character in text1: 
	sys.stdout.write(character)
	sys.stdout.flush()
	time.sleep(0.05)

text2 = ('>...\n')
for character in text2: 
	sys.stdout.write(character)
	sys.stdout.flush()
	time.sleep(0.3)

text3 = ('Nie musisz nic mówić, jak nie chcesz.\n'+'Wiym po co tu prziszłeś.\n'+'Tak jak każdy gdo sie tu pojawio, chladosz mądrość.\n'+'Móm prowde?\n')
for character in text3: 
	sys.stdout.write(character)
	sys.stdout.flush()
	time.sleep(0.05)

for character in text2: 
	sys.stdout.write(character)
	sys.stdout.flush()
	time.sleep(0.3)

text4 = ('Tak co, chcesz wejść dali? (ja/ni)\n')
for character in text4: 
	sys.stdout.write(character)
	sys.stdout.flush()
	time.sleep(0.07)

odpowiedz1 = input('> ')
if odpowiedz1.lower() == ('ja'):
	mapa_pałacu()                   
elif odpowiedz1 == ('ni'):
	sys.exit()
while odpowiedz1 not in ['ja','ni']:
	text5 = ('Nierozumiym...\n')
	for character in text5: 
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.05)
	odpowiedz1 = input('> ')
	if odpowiedz1.lower() == ('ja'):
		mapa_pałacu()                    
	elif odpowiedz1 == ('ni'):
		sys.exit()