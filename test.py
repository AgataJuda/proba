from wektor import Vector 
from wektor import podział

v=Vector() #tworzenie
print(v)

v.generate() #generowanie
print('generowane współrzędne\n',v)

x=input('Podaj wspołrzędne wektora: ') #wprowadzanie 
x=podział(x)
v.wprow(x) 
print(v)

x=input('Podaj wspołrzędne wektora, który chcesz dodać: ') #dodawanie
x=podział(x)
print(v+x)

x=input('Podaj wspołrzędne wektora, który chcesz odjąć: ') #odejmowanie
x=podział(x)
print(v-x)

k=int(input('Podaj skalar do mnożenia: ')) #mnożenie przez skalar
v.mn_przez_skal(k)
print(v)

print('Długość wektora to: ',v.dlugosc()) #długość

print('Suma współrzędnych to: ',v.suma_el()) #suma elementów

x=input('Podaj wspołrzędne wektora, który chcesz pomnożyć skalarnie: ') #mnożenie skalarne
x=podział(x)
print(v*x)

k=int(input('Podaj pozycję, którą chcesz znać: ')) #sprawdzanie pozycji
print(v[k])

k=int(input('Podaj liczbę, którą chcesz sprawdzić czy jest na którejkolwiek współrzędnej: '))
print(k in v) #sprawdzanie czy jest element

print(Vector()) #działanie __str__
#print(in(2))
