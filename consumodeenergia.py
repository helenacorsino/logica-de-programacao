# Monitor de Consumo de Energia

consumo_total = 0
dias_acima_20 = 0

for dia in range(1, 8):
    consumo = float(input(f"Digite o consumo do dia {dia} (kWh): "))

    consumo_total += consumo

    if consumo > 20:
        dias_acima_20 += 1

print("\n=== Resultado da Semana ===")
print(f"Consumo total: {consumo_total:.2f} kWh")
print(f"Dias com consumo acima de 20 kWh: {dias_acima_20}")