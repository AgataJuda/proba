from random import uniform
from math import sqrt
def podział(m):
	'''Funkcja zamienia listę znaków na tablicę.
		INPUT: m - string składający się z liczb (float) i przecinków,
				 które oddzielają kolejne liczby.
		OUTPUT: x - tablica składająca się z podanych wcześniej liczb'''
	delimiter=','
	m=m.split(delimiter)
	x=[]
	for i in m:
		x.append(int(i))
	return x

class Vector:
	def __init__(self, args=3):
		'''Funkcja tworzy wektor zerowy o podanej przez użytkownika długości.
			INPUT: args - liczba (int, większa od 0) określająca ilość współrzędnych wektora
						(brak podanej wartości - domyślne wybranie 3).
			OUTPUT: brak'''
		a=[]
		self.a=a
		self.args=args
		for i in range (self.args):
			self.a.append(0)
	def generate(self):
		'''Funkcja podmienia poprzednie współrzędne wektora losowymi liczbami (float) przybliżonymi
			do drugiego miejsca po przecinku z zakresu od -100 do 100.
			INPUT: brak
			OUTPUT: a - wektor (tablica) z nowymi losowymi współrzędnymi'''
		for i in range (self.args):
			k=uniform(-100,100)
			k=round(k,2)
			self.a[i]=k
		return self.a
	def wprow (self,b):
		'''Funkcja podmienia poprzednie współrzędne wektora liczbami (float) innej tablicy podanej 
			przez użytkownika.
			INPUT: b - tablica wypełniona liczbami (float), będąca innym wektorem
			OUTPUT: a - wektor (tablica) z nowymi współrzędnymi'''
		if len(self.a)!=len(b):
			raise ValueError("różne wymiary wektorów")
		else:
			for i in range (self.args):
				self.a[i]=b[i]
		return self.a
	def mn_przez_skal(self,k):
		'''Funkcja mnoży poprzednie współrzędne wektora przez liczbę (float) podaną przez użytkownika.
			INPUT: k - liczba (float) przez którą mnożymy
			OUTPUT: a - wektor (tablica) z nowymi (przemnożonymi) współrzędnymi'''
		for i in range (self.args):
			self.a[i]=k*float(self.a[i])
		return self.a
	def dlugosc (self):
		'''Funkcja oblicza długość wektora na bazie aktualnych współrzędnych
			INPUT: brak
			OUTPUT: z - długość wektora (float) przybliżona do dwóch miejsc po przecinku'''
		z=0
		for i in range (self.args):
			z=z+((float(self.a[i]))**2)
		z=round(sqrt(z),2)
		return z
	def __add__ (self,p):
		'''Funkcja dodaje do siebie dwa wektory (pod warunkiem że są tej samej długości)
			i zamienia wektor a na wektor będący sumą a i p, w innym przypadku wyrzuca błąd.
			INPUT: p - tablica wypełniona liczbami (float), będąca innym wektorem
			OUTPUT: a - wektor (tablica) z nowymi (dodanymi) współrzędnymi'''
		if len(self.a)!=len(p):
			raise ValueError("różne wymiary wektorów")
		else:
			for i in range (self.args):
				self.a[i]=self.a[i]+p[i]
		return self.a
	def __sub__ (self,p):
		'''Funkcja odejmuje od siebie dwa wektory (pod warunkiem że są tej samej długości)
			i zamienia wektor a na wektor będący róznicą a i p, w innym przypadku wyrzuca błąd.
			INPUT: p - tablica wypełniona liczbami (float), będąca innym wektorem
			OUTPUT: a - wektor (tablica) z nowymi (odjętymi) współrzędnymi'''
		if len(self.a)!=len(p):
			raise ValueError("różne wymiary wektorów")
		else:
			for i in range (self.args):
				self.a[i]=self.a[i]-p[i]
		return self.a
	def __mul__ (self,p):
		'''Funkcja mnoży skalarnie dwa wektory (pod warunkiem że są tej samej długości)
			INPUT: p - tablica wypełniona liczbami (float), będąca innym wektorem
			OUTPUT: z - liczba (float), będąca wynikiem mnożenia skalarnego'''
		if len(self.a)!=len(p):
			raise ValueError("różne wymiary wektorów")
		else:
			z=0
			for i in range (self.args):
				z+=(float(self.a[i])*p[i])
		return z
	def __getitem__(self,i):
		'''Funkcja podaje jaką wartość ma współrzędna na wybranej pozycji wektora
		   (liczone od 1), podanie liczby spoza zakresu wyrzuci błąd.
		INPUT: i - pozycja (int, większe od zera, nie większe niż ilość
				   współrzędnych wektora) 
		OUTPUT: z - liczba (float), będąca wynikiem mnożenia skalarnego'''
		if ((i-1)>len(self.a))or(i<0):
			raise ValueError("Nie ma takiej pozycji")
		else:
			return self.a[i-1] 
	def suma_el(self):
		'''Funkcja podaje sumę wszystkich współrzędnych wektora.
		INPUT: brak
		OUTPUT: s - liczba (float), będąca sumą wszystkich współrzędnych wektora'''
		s=0
		for i in range (len(self.a)):
			s+=float(self.a[i])
		return s
	def __cmp__(self,x):
		'''Funkcja sprawdza czy podana przez użytkownika liczba(float) znajduje się
		na dowolnwj współrzędnej wektora.
		INPUT: x - liczba (float), którą chcemy sprawdzić
		OUTPUT: Wartości bool (True, jeśli liczba jest na którejkolwiek współrzędnej lub 
		False, jeśli jej nie ma) '''
		if x in self.a:
			return True
		else:
			return False
	def __str__(self):
		'''Funkcja wypisująca wektor zerowy, który powstaje przez wywołanie 
			całej klasy "Vector".
		INPUT: brak
		OUTPUT: a - wektor zerowy, powstający przy wywołaniu klasy "Vector"'''
		return str(self.a)

