import random

pada = random.choice([True, False]) #Tutaj program losuje którąś z opcji
zgaduj = True

while zgaduj:
    odpowiedz = input("Czy pada? (t/n) ")
    #tutaj rozwiązanie
    if(odpowiedz == "t" and pada):
        print("zgadles")
        zgaduj = False
    else:
        print ("Zgaduj dalej")
