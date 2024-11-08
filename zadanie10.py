# Sprawdzanie liczb pierwszych w przedziale 1-100
for liczba in range(1, 101):  # Iterujemy przez liczby od 1 do 100
    if liczba > 1:  # Liczba pierwsza musi być większa niż 1
        pierwsza = True  # Zakładamy, że liczba jest pierwsza
        for i in range(2, int(liczba**0.5) + 1):  # Sprawdzamy dzielniki od 2 do pierwiastka z liczby
            if liczba % i == 0:  # Jeśli liczba jest podzielna przez i, to nie jest pierwsza
                pierwsza = False
                break  # Jeśli znajdziemy dzielnik, przerywamy dalsze sprawdzanie
        if pierwsza:
            print(liczba)  # Jeśli liczba jest pierwsza, wypisujemy ją
            #prosze Pana niech ta klasa nie ma tych podpowiedzi co są po hasztagu, to jest dla Pana
