#Arquivo em que os membros devem implementar suas funções.
def calcular_vazao(area: float, velocidade: float) -> float:
    """
    Calcula a vazão volumétrica de um fluido em uma seção do tubo.
    
    Parâmetros:
    area (float): Área da seção transversal do tubo (ex: m²).
    velocidade (float): Velocidade de escoamento do fluido (ex: m/s).
    
    Retorna:
    float: A vazão volumétrica resultante (ex: m³/s).
    """
    if area <= 0:
        raise ValueError("A área da seção do tubo deve ser maior que zero.")
    if velocidade < 0:
        raise ValueError("A velocidade do escoamento não pode ser negativa.")
        
    vazao = area * velocidade
    return vazao