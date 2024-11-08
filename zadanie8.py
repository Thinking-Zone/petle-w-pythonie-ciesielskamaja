pada = False
licznik_nie = 0
while not pada:
    print("Nie pada! yaaay")
    odpowiedz = input("Czy pada? (tak/nie) ")
    if odpowiedz == 'tak':
        print('powiedziales nie: ',licznik_nie , 'razy')
        pada = True
    elif odpowiedz == 'nie':
        licznik_nie += 1 
    elif odpowiedz == 'nie wiem':
        print("to wyjdz na dwor i sie dowiedz")
    else:
        print("poweiedz tak lub nie")
