dados_brutos = [
    "  kiara;desenvolvedor;11988887777  ",
    "  JJ;analista de rh;21977776666  ",
    "  Pope;gerente de projetos;31966665555  "
]


def limpar_e_formatar_texto(texto):
    """
    FUNÇÃO 1:
    - Recebe uma string.
    - Remove espaços extras das pontas usando .strip().
    - Converte o texto para letras maiúsculas usando .upper().
    - Retorna o texto formatado.
    """
   
    texto_formatado = texto.strip().upper()

    return texto_formatado


def extrair_codigo_ou_ddd(dado):
    """
    FUNÇÃO 2:
    - Recebe um telefone ou CPF como string.
    - Remove espaços das pontas usando .strip().
    - Utiliza fatiamento [x:y] para extrair os 2 primeiros dígitos.
    - Retorna os dígitos extraídos.
    """

    dado_limpo = dado.strip()

    codigo = dado_limpo[0:2]

    return codigo


def processar_e_exibir_cadastros(lista_dados):
    """
    FUNÇÃO 3:
    - Recebe a lista de cadastros.
    - Percorre os dados utilizando FOR.
    - Separa as informações usando .split(";").
    - Utiliza as Funções 1 e 2.
    - Exibe os dados utilizando f-string.
    - Retorna a quantidade de registros processados.
    """

    total_processado = 0

    for dado in lista_dados:

        partes = dado.strip().split(";")

        nome = partes[0]
        cargo = partes[1]
        telefone = partes[2]

        nome_formatado = limpar_e_formatar_texto(nome)
        cargo_formatado = limpar_e_formatar_texto(cargo)
        ddd = extrair_codigo_ou_ddd(telefone)

        # Exibe o cadastro formatado
        print(f"Nome: {nome_formatado}")
        print(f"Cargo/Setor: {cargo_formatado}")
        print(f"DDD/Código: {ddd}")
        print("-" * 50)

        total_processado += 1

    return total_processado

def main():
    print("==================================================")
    print("     SISTEMA DE GESTÃO MODULARIZADO - AV2        ")
    print("==================================================\n")

    print("Iniciando o processamento dos dados...\n")

    total_processado = processar_e_exibir_cadastros(dados_brutos)

    print(f"Total de registros processados: {total_processado}")

    print("\n==================================================")
    print("             PROCESSAMENTO CONCLUÍDO              ")
    print("==================================================")


if __name__ == "__main__":
    main()