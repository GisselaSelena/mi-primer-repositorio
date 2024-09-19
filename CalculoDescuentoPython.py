def calcular_descuento(monto_total, porcentaje_descuento=12):
    """
        Calcula el descuento basado en el monto total de la compra y el porcentaje de descuento.

        Parámetros:
        monto_total (float): Monto total de la compra.
        porcentaje_descuento (int, optional): Porcentaje de descuento a aplicar (default=12).

        Retorna:
        float: Monto del descuento calculado.
        """
    descuento = (monto_total/100) * porcentaje_descuento
    return descuento

# Llamada a la función calcular_descuento con monto total de la compra
monto_total1 = 1500
descuento1 = calcular_descuento(monto_total1)
monto_final1 = monto_total1 - descuento1
print(f"Monto total de la compra: ${monto_total1:.2f}")
print(f"Descuento ({12}%): ${descuento1:.2f}")
print(f"Monto final a pagar: ${monto_final1:.2f}")

# Llamada a la función calcular_descuento con monto total de la compra y porcentaje de descuento
monto_total2 = 500
porcentaje_descuento2 = 20
descuento2 = calcular_descuento(monto_total2, porcentaje_descuento2)
monto_final2 = monto_total2 - descuento2
print(f"\nMonto total de la compra: ${monto_total2:.2f}")
print(f"Descuento ({porcentaje_descuento2}%): ${descuento2:.2f}")
print(f"Monto final a pagar: ${monto_final2:.2f}")