# Solicitar el precio de la comida
precio = float(input("Ingrese el precio de la comida: $"))

# Determinar el porcentaje de propina
if precio < 20:
    propina = precio * 0.10
elif 20 <= precio <= 50:
    propina = precio * 0.15
else:
    propina = precio * 0.20

# Calcular el total
total = precio + propina

# Mostrar resultados
print(f"Propina: ${propina:.2f}")
print(f"Total a pagar: ${total:.2f}")
