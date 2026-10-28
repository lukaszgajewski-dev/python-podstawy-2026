"""
Źródło: https://youtu.be/eB3r2NQwNi4?si=wxJjTxD_MjK6VW8D
Lekcja 1: Podstawy logiki w Pythonie
Temat: Symulator bramkarza w klubie

Czego się tu nauczyłem:
1. input() - pobieranie danych od użytkownika.
2. łączenie tekstu w print() za pomocą przecinków i plusów.
3. int() - zamiana tekstu na liczbę, żeby móc sprawdzić wiek (>= 18).
4. if / elif / else - instrukcje warunkowe (jeśli, w przeciwnym razie jeśli, w przeciwnym razie).
5. Zagnieżdżanie i wcięcia (Tab) - logika sprawdzania krok po kroku.
"""


imie = input("Jak masz na imię? ")
wiek = input("Ile masz lat " + imie + "? ")

print("Cześć", imie + "! Masz", wiek, "lat!")
if int(wiek) >= 18:
    print("Jesteś pełnoletni", imie)

    stroj = input("Czy masz garnitur? ")
    if stroj == "tak":
        print("Bardzo ładnie wyglądasz")
    elif stroj == "nie":
        print("To idż se kup")
    else:
        print("Powinieneś mieć garnitur raczej")

    money = input("Czy masz dużo hajsu? ")
    if money == "tak":
        print("Bardzo fajnie, to zaimprezujemy!")
    elif money == "nie":
        print("No to nie wiem czy się opłaca wchodzić bo tu wszystko drogie:(")
    else:
        print("No to się zdecyduj czy masz czy nie")
else:
    print("sorry, nie możesz wejść", imie)