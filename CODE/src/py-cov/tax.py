def calculate_tax(income, dependents, age):
    if income > 50000:
        if dependents > 2:
            if age > 60:
                return "Low Tax"
            else:
                return "Medium Tax"
        else:
            if age > 60:
                return "Medium Tax"
            else:
                return "High Tax"
    else:
        if dependents > 2:
            return "No Tax"
        else:
            return "Low Tax"
