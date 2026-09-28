dados_brutos = [
    "carlos eduardo silva;desenvolvedor;11988887777",
    "ana paula mendes;analista de rh;21977776666",
    "roberto carlos oliveira;gerente de projetos;31966665555"
]

def limpar(texto):
    return texto.strip().upper()

def ddd(telefone):
    return telefone.strip()[:2]

def processar(lista):
    total = 0

    for dado in lista:
        nome, cargo, telefone = dado.split(";")

        print(f"Nome: {limpar(nome)}")
        print(f"Cargo: {limpar(cargo)}")
        print(f"DDD: {ddd(telefone)}")
        print()

        total += 1

    return total

def main():
    total = processar(dados_brutos)
    print(f"Total processado: {total}")

if __name__ == "__main__":
    main()
