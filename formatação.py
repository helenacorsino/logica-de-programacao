def formatar_citacao(nome_completo):

    partes = nome_completo.strip().split()

    sobrenome = partes[-1].upper()

    primeiro_nome = " ".join(partes[:-1])

    return sobrenome + ", " + primeiro_nome
nome_completo = print(input("Digite seu nome: "))