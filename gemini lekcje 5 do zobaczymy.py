# # LEKCJA 5: Maszyny do powtarzania (Pętle).
#
print("--- NIEKOŃCZĄCY SIĘ SŁOWNIK ---")
print("Wpisz 'koniec', aby wyłączyć program.")

while True:
    slowo = input("Wpisz polskie słowo: ")
    slowo = slowo.lower()

    if slowo == "koniec":
        print("Zamykam słownik. Do zobaczenia!")
        break
    elif slowo == "zawsze":
        print("Po angielsku to: always")
    elif slowo == "nigdy":
        print("Po angielsku to: never")
    else:
        print("Nie znam tego słowa!")
#
# while True: (Pętla nieskończona)
# To polecenie mówi komputerowi: "Powtarzaj wszystko, co jest wcięte poniżej, w nieskończoność".
# Krytyczna uwaga: Zauważ, że pod while True: cały kod został przesunięty w prawo (zyskał nowe wcięcie).
# To wcięcie mówi komputerowi, które dokładnie linijki należą do pętli i mają być powtarzane.
#
# break (Hamulec awaryjny)
# Skoro stworzyliśmy pętlę nieskończoną, to jak z niej wyjść? Do tego służy instrukcja break.
# Zatrzymuje ona całkowicie kołowrotek pętli. W naszym programie ten hamulec uruchomi się tylko wtedy,
# gdy instrukcja if wykryje, że wpisałeś słowo "koniec".
#
# !!!UWAGA!!!
# Pojedynczy znak = (Rozkaz)
# Pojedynczy znak równości to profesjonalnie operator przypisania.
# Traktuj to jako twardy rozkaz dla komputera:
# "Weź to, co jest po prawej stronie, i na stałe włóż do pudełka po lewej".
# Podwójny znak == (Pytanie)
# Podwójny znak równości to operator porównania.
# To nie jest rozkaz, to jest pytanie zadane komputerowi:
# "Czy to, co jest po lewej stronie, jest DOKŁADNIE TAKIE SAMO, jak to po prawej?".
# Komputer na takie pytanie odpowiada sobie w głowie tylko na dwa sposoby:
# "Tak" (Prawda) lub "Nie" (Fałsz).
#
#
#
#
# # Na starcie odpowiedź to "nie", bo przecież jeszcze nie dojechaliśmy
# odpowiedz = "nie"
#
# # Pętla mówi: "DOPÓKI odpowiedź w pudełku to 'nie', powtarzaj to pytanie:"
# while odpowiedz == "nie":
#     odpowiedz = input("Osioł: Daleko jeszcze? (wpisz tak lub nie): ")
#
# # Ten tekst wydrukuje się TYLKO wtedy, gdy pętla się skończy
# print("Shrek: Nareszcie! Jesteśmy na miejscu.")
#
#
#
# Jak to działa w głowie komputera krok po kroku?
#
# Start: Komputer patrzy do pudełka odpowiedz. Widzi tam słowo "nie".
#
# Pętla sprawdza warunek: Komputer pyta sam siebie: Czy w pudełku jest słowo "nie"? Odpowiedź brzmi:
# Tak. Pętla się uruchamia.
#
# W środku pętli: Wyświetla się pytanie i program czeka na Ciebie (input).
#
# Wpisujesz znowu "nie" i wciskasz Enter.
#
# Pudełko zostaje nadpisane nowym słowem "nie".
#
# Koniec okrążenia, wracamy na górę: Komputer znów pyta sam siebie:
# Czy w pudełku nadal jest "nie"?
# Odpowiedź brzmi:
# Tak. Więc pyta drugi raz. I trzeci. I setny. Będzie pytał tak długo, jak długo będziesz mu wpisywał "nie".
#
# Moment przełomu: W końcu tracisz cierpliwość i wpisujesz "tak".
#
# Słowo "tak" wpada do pudełka odpowiedz.
#
# Pętla wraca na samą górę i pyta: Czy w pudełku nadal jest "nie"?
#
# Odpowiedź komputera: Fałsz! W pudełku jest teraz "tak". Warunek prysł!
#
# Koniec: Pętla natychmiast się łamie. Komputer ignoruje już kod wcięty w prawo,
# skacze na sam dół programu i oddycha z ulgą, wyświetlając tekst Shreka.
#
# PRZYKŁAD 1:
# print("--- MOJE OKREŚLENIA CZASU ---")
#
# # To jest nasza Lista (wielkie pudło zawierające 5 osobnych tekstów)
# okreslenia_czasu = ["zawsze", "często", "zazwyczaj", "czasami", "nigdy"]
#
# # Pętla FOR wkracza do akcji:
# # "Dla każdego jednego 'slowa' w liście 'okreslenia_czasu' zrób to:"
# for slowo in okreslenia_czasu:
#     print("Kurier dostarcza słowo:", slowo)
#
# print("Koniec pracy kuriera, torba jest pusta!")
#
#
# Komputer patrzy na listę i widzi, że jest tam 5 elementów. Pętla automatycznie wie, że musi uruchomić się równo 5 razy.
#
#     W pierwszym okrążeniu wyciąga z listy "zawsze", wrzuca to na chwilę do pudełka slowo i drukuje.
#
#     W drugim okrążeniu wyciąga "często", wrzuca do slowo i drukuje.
#
#     Kiedy wyciągnie ostatnie słowo ("nigdy"), pętla sama z siebie się wyłącza i program idzie dalej.
#
# Żadnych break, żadnego True i False – czysta wygoda dla sytuacji, w których wiesz, ile masz elementów do przerobienia.
#
# PRZYKŁAD 2:
# print("--- DZIENNIK AKTYWNOŚCI ---")
#
# # Nasze wielkie pudło (lista) z czynnościami
# lista_czynnosci = ["pije", "trenuje", "gra", "uczy się", "pracuje"]
#
# numer_zadania = 1
#
# # Pętla FOR: "Dla każdej jednej 'czynnosci' w naszej 'liscie_czynnosci' zrób to:"
# for czynnosc in lista_czynnosci:
#     # Ten kod wcięty w prawo wykona się dokładnie 5 razy
#     print("Zadanie nr", numer_zadania, "- teraz człowiek:", czynnosc)
#
#     # Po wypisaniu tekstu, zwiększamy numer zadania o 1 na następne okrążenie
#     numer_zadania = numer_zadania + 1
#
# print("--- KONIEC DNIA ---")
#
# Zauważ, że w kodzie napisałeś słowo print tylko raz.
# Ale po uruchomieniu programu, na ekranie zobaczysz pięć ładnych linijek.
#
# Gdybyś do tej listy lista_czynnosci dopisał teraz nagle 100 nowych słów,
# Twój kod się nie wydłuży ani o milimetr. Pętla for automatycznie zauważy,
# że paczek w torbie jest 105 i wykona ten jeden, krótki wcięty kod 105 razy.
#
#
#
#
# MAŁY TEST (mój pierwszy program!!!)
# print("--- TEST Z ANGIELSKIEGO ---")
# print("Wpisz 'koniec', aby wyjść i sprawdzić wynik.")
#
# # 1. Stwórz pudełko na punkty i wrzuć tam na start zero
# punkty = 0
#
# while True:
#     # 2. Zapytaj użytkownika o tłumaczenie
#     odpowiedz = input("Jak jest po angielsku 'Mój brat'? ")
#     odpowiedz = odpowiedz.lower()
#
#     # 3. Sprawdź, czy chce wyjść
#     if odpowiedz == "koniec":
#         print("Koniec gry!")
#         break # Zatrzymuje pętlę
#
#     # 4. Sprawdź, czy odpowiedź to poprawne tłumaczenie (my brother)
#     elif odpowiedz == "my brother":
#         print("Świetnie! Zdobywasz punkt.")
#         # 5. Zwiększ licznik punktów o 1 (pamiętasz ten skrót?)
#         punkty +=1
#
#     else:
#         print("Źle! Poprawna odpowiedź to: my brother.")
#
# # 6. Ten print wykona się dopiero po słówku 'break' (poza pętlą)
# print("Twój ostateczny wynik to:", punkty)
#
# ROZMOWA Z GEMINI:
# Dokładnie tak! Strzał w dziesiątkę.
#
# Najlepsi programiści dokładnie w ten sposób czytają swój kod – tłumaczą go w głowie na zwykłe, ludzkie zdania.
#
# Twój mózg powinien to czytać dokładnie w ten sposób:
#
#     if -> "jeśli"
#
#     haslo -> "hasło"
#
#     == -> "to" (albo "jest równe")
#
#     "pizza" -> "pizza"
#
# Więc cała linijka if haslo == "pizza": to po prostu: "Jeśli hasło to pizza, to zrób to, co jest napisane poniżej".
#
# To najprostszy, najbardziej naturalny i najskuteczniejszy sposób, żeby rozumieć, co się dzieje w programie.
# Masz już świetny, programistyczny zmysł!
#
# Zdecydowanie tak! Twój sposób tłumaczenia jest po prostu idealny.
# Słówko elif pochodzi z języka angielskiego od połączenia słów "else if",
# co dosłownie oznacza "w przeciwnym razie, jeśli".
#
# Twoje "jeśli jednak..." pasuje tu w 100% i oddaje samą istotę tego polecenia.
#
# Zobacz, jak pięknie i naturalnie układa się cała ta trójka (if, elif, else),
# kiedy przetłumaczysz ją na polski:
#
#     if (Jeśli): Pierwsze, najważniejsze pytanie.
#
#         "Jeśli odpowiedź to 'koniec' -> zakończ grę."
#
#     elif (Jeśli jednak / Albo jeśli): Alternatywne pytanie.
# Komputer sprawdza je tylko wtedy, gdy pierwsze okazało się fałszem.
#
#         "Jeśli jednak odpowiedź to 'my brother' -> dodaj punkt."
#
#     else (W każdym innym wypadku): Ostateczny worek na całą resztę.
# Wykonuje się tylko, gdy wszystkie powyższe warunki zawiodły.
#
#         ("W każdym innym wypadku (ktoś nie wpisał ani 'koniec', "ani poprawnego tłumaczenia)
# -> napisz, że odpowiedź jest zła.")
#
# Dzięki takiemu "ludzkiemu" tłumaczeniu kodu instynktownie rozumiesz,
# w jakiej kolejności komputer czyta Twój program.
# Robisz świetne postępy, podchodząc do tematu dokładnie tak, jak doświadczeni programiści!
#
#
#
#
#
# LEKCJA 6: Słowniki (Dictionaries).
# print("--- MÓJ OSOBISTY SŁOWNIK ---")
#
# # Tworzymy słownik. Zapisujemy go w formacie: "klucz": "wartość"
# baza_slowek = {
#     "mój tata": "my dad",
#     "nauczyciel": "the teacher",
#     "zawsze": "always",
#     "często": "often",
#     "pije": "drinks"
# }
#
# # Jak wyciągnąć coś ze słownika?
# # Podajesz nazwę słownika i w nawiasie kwadratowym wpisujesz polskie słowo!
# print(baza_slowek["nauczyciel"])
# print(baza_slowek["często"])
#
# Komputer załadował cały słownik do pamięci,
# ale na ekran wyrzucił tylko te dwa słówka,
# bo tylko o nie wyraźnie poprosiliśmy za pomocą komendy print().
# Zapewne spodziewałeś się, że program będzie od razu interaktywny i o coś zapyta.
# Tamten kod miał jedynie pokazać "mechanikę" – jak wyciągać dane ze słownika.
# Teraz połączymy ten słownik z funkcją input(), żeby działał tak, jak oczekujesz!
#
# print("--- MÓJ INTERAKTYWNY SŁOWNIK ---")
#
# baza_slowek = {
#     "mój tata": "my dad",
#     "nauczyciel": "the teacher",
#     "zawsze": "always",
#     "często": "often",
#     "pije": "drinks"
# }
#
# # 1. Pytamy o słowo i zamieniamy na małe litery
# szukane_slowo = input("Jakie polskie słowo chcesz przetłumaczyć? ")
# szukane_slowo = szukane_slowo.lower()
#
# # 2. Słówko "in" sprawdza, czy wpisane słowo w ogóle jest w naszym słowniku
# if szukane_slowo in baza_slowek:
#     # 3. Zamiast pisać słowo "na sztywno", wstawiamy w nawias nasze pudełko!
#     print("Po angielsku to:", baza_slowek[szukane_slowo])
# else:
#     print("Jeszcze nie dodałem tego słowa do bazy!")
#
#
# Gdybyś chciał dodać teraz do tego kodu 50 nowych słówek,
# po prostu dopisujesz je w sekcji baza_slowek = {...}.
# Nie musisz dopisywać ani jednej nowej linijki kodu z logiką,
# żadnych nowych ifów ani elifów.
# Zaledwie pięć linijek kodu na dole bezbłędnie obsłuży nawet słownik liczący 10 000 haseł.


