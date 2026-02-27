energie = float(input("Combien de kWh a consommé votre tâche ? "))
if energie < 1:
    print("Super, faible consommation !")
elif energie < 5:
    print("Consommation moyenne, pensez à optimiser.")
else:
    print("Consommation élevée ! Essayez d'économiser de l'énergie.")