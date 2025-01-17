#Função para converter string em inteiro
def string_para_inteiro(s):
    if not s.isdigit():
        raise ValueError("A string deve conter apenas dígitos.")
    return int(s)