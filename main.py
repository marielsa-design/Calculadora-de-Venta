# Regitro básico de ventas

nombre = input("Ingresa el nombre del cliente: ")
precio = float(input("Ingresa el precio unitario: "))
cantidad = int(input("Ingresa la cantidad de productos: "))
vip_input = input("¿El cliente tiene membresía VIP? (si/no): ")

es_vip = vip_input.lower() == "si"

subtotal = precio * cantidad

descuento = 0
if es_vip:
    descuento = subtotal * 0.10

total = subtotal - descuento

print("#" * 20)
print("RESUMEN DE VENTA")
print(f"Cliente:", nombre)
print(f"Subtotal:", subtotal)
print(f"descuento:", descuento)
print(f"Total a pagar:", total)
print("#" * 20)