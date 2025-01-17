def celsius_para_fahrenheit(celsius):
    if not isinstance(celsius, (int, float)):
        raise ValueError("Temperatura deve ser um número.")
    return celsius * 9/5 + 32