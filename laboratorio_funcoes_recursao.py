TAXA_PROCESSAMENTO = 2.00

def calcular_frete(valor_compra, peso_kg):
    frete = peso_kg * 5
    return frete * 0.5 if valor_compra >= 200 else frete

def aplicar_cupom(valor_item, cupom_desconto):
    return valor_item * (1 - cupom_desconto / 100) + TAXA_PROCESSAMENTO

def exibir_cronograma_regressivo(parcelas_restantes, valor_parcela):
    if parcelas_restantes == 0:
        print("Todas as parcelas foram quitadas!")
        return
    print(f"Restam {parcelas_restantes} parcela(s) de R$ {valor_parcela}")
    exibir_cronograma_regressivo(parcelas_restantes - 1, valor_parcela)

print("=== TESTE PARTE 1: CALCULADORA DE FRETE ===")
print("Frete Final Esperado (10.0):", calcular_frete(200, 4))

print("\n=== TESTE PARTE 2: CUPOM E TAXAS DE ESCOPO ===")
print("Preço Final Esperado (92.0):", aplicar_cupom(100, 10))

print("\n=== TESTE PARTE 3: CRONOGRAMA RECURSIVO ===")
exibir_cronograma_regressivo(3, 150.0)