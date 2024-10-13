def pertence_fibonacci(numero: int) -> bool:
    """Verifica se um número pertence à sequência de Fibonacci."""
    a, b = 0, 1
    while a < numero:
        a, b = b, a + b

    return a == numero


if __name__ == "__main__":
    try:
        numero = int(input("Informe um número: "))
        if numero < 0:
            raise ValueError("O número deve ser não negativo.")
        
        resultado = pertence_fibonacci(numero)
        print(f"O número {numero} {'pertence' if resultado else 'NÃO pertence'} à sequência de Fibonacci.")
    except ValueError as e:
        print(f"Entrada inválida: {e}")

