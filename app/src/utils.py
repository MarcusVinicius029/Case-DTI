def testType(value):
    """
    Verifica se o valor NÃO pode ser convertido para inteiro.

    Returns:
        bool: Retorna True se o valor não for um inteiro (ex: contém letras), e False caso contrário.
    """
    try:
        int(value)
        return False
    except ValueError:
        return True
