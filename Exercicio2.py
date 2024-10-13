
def verifica_letra_a(string: str) -> None:
    """
    Verifica a ocorrência da letra 'a' (incluindo acentuadas) em uma string.
    :param string: A string na qual a letra 'a' será verificada.
    """
    string_normalizada =string.lower()

    # Conta a ocorrência das letras 'a', 'â', 'á' e 'ã'
    letras_a = ['a', 'â', 'á', 'ã','à']
    quantidade = sum(string_normalizada.count(letra) for letra in letras_a)

    # Verifica se a letra 'a' existe
    if quantidade > 0:
        print(f"A letra 'a' (incluindo acentuadas) aparece {quantidade} vez(es) na string.")
    else:
        print("A letra 'a' (incluindo acentuadas) não aparece na string.")

if __name__ == "__main__":
    try:
        # Solicita a string do usuário
        texto = input("Informe uma string: ")
        verifica_letra_a(texto)
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

