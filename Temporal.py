
# True
try:
    nombre = input("Por favor escribe tu nombre: ").title().strip()
    precio_de_su_comida = float(input("por favor escribe cuanto deber pagar => "))

    if  precio_de_su_comida < 20:
        propina = precio_de_su_comida * 0.10
    elif precio_de_su_comida >=20 and precio_de_su_comida <= 50:
        propina = precio_de_su_comida * 0.15
    else:
        propina = precio_de_su_comida *0.20

    print("querio ",nombre, "Usted deber pagar",propina," de propina")
    print("por lo tanto su cuenta es de ", precio_de_su_comida+propina)
except ValueError:
    print("le pedí claramente un numero")
    print("reintente de nuevo")