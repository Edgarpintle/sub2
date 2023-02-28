precio = 49.99
cantidad = 30
iva = 0.16

if cantidad > 12:
  descuento = 0.10

else:
  descuento = 0.0

subtotal = precio*cantidad
descuento = subtotal * descuento
IVA = (subtotal - descuento)* iva
total= subtotal - descuento
salida = f"""
subtotal:  ${subtotal:,.2f}
descuento  ${descuento:,.2f}
IVA:       ${iva:,.2f}
total:${total:,.2f}
"""
print(f"{iva:,.2%}")

usuario1="diego"
usuario2="elgar"
usuario3="bombo"
salida=f"{usuario1} \n{usuario2} \n{usuario3}"
print(salida)


subtotal = precio*cantidad
IVA = subtotal * iva
total = subtotal + subtotal
salida = f"""
subtotal:  ${subtotal:,.2f}
IVA:       ${IVA:,.2f}
total:     ${total:,.2f}
"""

print(salida)