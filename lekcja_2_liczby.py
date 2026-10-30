"""
1. Zwykłe dodawanie
— po prostu wyświetla wynik,
oryginalne zmienne zostają nietknięte
"""
# a = 10
# b = 5
# print(a + b)

'''
2. Nadpisywanie zmiennej (pełny zapis) 
- bierzemy stare "a", 
dodajemy 5 i pakujemy z powrotem do pudełka "a"
'''
# a = 10
# a = a + 5
# print(a)

'''
3. Nadpisywanie zmiennej (skrócony zapis) 
- robi dokładnie to samo co wyżej, ale szybciej. 
Programiści tak piszą z lenistwa.'''
# a = 10
# a += 5
# print(a)

'''1. Zwykłe mnożenie - po prostu wyświetla wynik, 
oryginalne zmienne zostają nietknięte'''
# c = 6
# d = 2
# print(c * d)

'''
2. Nadpisywanie zmiennej (pełny zapis) 
- bierzemy stare "b", mnożymy razy 2 
i pakujemy z powrotem do pudełka "b" '''
# b = 6
# b = b * 2
# print(b)

'''3. Nadpisywanie zmiennej (skrócony zapis) 
- robi dokładnie to samo co wyżej, używając operatora *= '''
# b = 6
# b *= 2
# print(b)


"""
W Pythonie zwykłe dzielenie (pojedynczy ukośnik /) 
zawsze zwraca wynik w postaci liczby zmiennoprzecinkowej (ułamkowej, z kropką), 
nawet jeśli liczby dzielą się przez siebie idealnie bez reszty.
"""
'''1. Zwykłe dzielenie.
Wyświetli: 3.0'''
# c = 6
# d = 2
# print(c / d)

'''2. Nadpisywanie zmiennej (pełny zapis) 
- stare "c" dzielimy przez 2 i chowamy z powrotem. 
Wyświetli: 3.0'''
# c = 6
# c = c / 2
# print(c)

'''3. Nadpisywanie zmiennej (skrócony zapis). Wyświetli: 3.0'''
# c = 6
# c /= 2
# print(c)


"""
Jeśli chcesz pozbyć się .0 i otrzymać czystą liczbę całkowitą (samo 3),
powinieneś użyć podwójnego ukośnika, który oznacza dzielenie całkowite.
"""
'''1. Zwykłe dzielenie całkowite. Wyświetli: 3'''
# c = 6
# d = 2
# print(c // d)

'''2. Nadpisywanie zmiennej (pełny zapis) 
- stare "c" dzielimy całkowicie przez 2 i chowamy z powrotem.
Wyświetli: 3'''
# c = 6
# c = c // 2
# print(c)

'''3. Nadpisywanie zmiennej (skrócony zapis). Wyświetli: 3'''
# c = 6
# c //= 2
# print(c)

"""
Znak % (modulo) - zwraca resztę z dzielenia.
Bardzo przydatne do sprawdzania np. czy liczba jest parzysta.
"""
''' 1. Zwykłe modulo. Wyświetli: 1 (bo w 5 mieszczą się dwie dwójki i zostaje 1 reszty)'''
# a = 5
# b = 2
# print(a % b)

'''2. Nadpisywanie zmiennej (pełny zapis). Wyświetli: 1'''
# a = 5
# a = a % 2
# print(a) 

'''3. Nadpisywanie zmiennej (skrócony zapis). Wyświetli: 1'''
# a = 5
# a %= 2
# print(a)
