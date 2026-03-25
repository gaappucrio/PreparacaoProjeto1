# Arquivo em que os membros devem implementar suas funções.
#
# Premissa Leo
#
# Criar uma função que calcula o rendimento real de uma reação, recebendo o
# valor do rendimento teórico, e os valores tanto esperado quanto real do
# resultado.


def calcular_rendimento():

    """
    Calcula o rendimento percentual de uma reação química.

    Parâmetros:
    valor_teorico (float): A massa ou quantidade esperada (calculada no papel).
    valor_real (float): A massa ou quantidade obtida experimentalmente.

    Retorna:
    float: O rendimento percentual (%).
    """
    print("\n--- Calculadora de Rendimento Químico ---\n")


    try:
        # Solicitando os dados ao usuário
        teorico = float(input("Informe o rendimento teórico (g ou mol): "))
        real = float(input("Informe o rendimento real obtido (g ou mol): "))

        if teorico <= 0:
            print("Erro: O rendimento teórico deve ser maior que zero.")
            return

        # Cálculo
        rendimento = (real / teorico) * 100

        print(f"\nResultado:")
        print(f"Com um valor teórico de {teorico} e real de {real},")
        print(f"o rendimento da reação é de {rendimento:.2f}%.\n")

    except ValueError:
        print("Erro: Por favor, insira apenas números (use ponto em vez de vírgula).")

# Executa a função
# calcular_rendimento()
