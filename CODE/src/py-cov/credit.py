def credit_approval(income, credit_score, employment_status, debt_ratio):
    if income > 50000:
        if credit_score > 700:
            if employment_status == "Full-time":
                if debt_ratio < 0.3:
                    return "Approved"
                else:
                    return "High Debt"
            else:
                return "Unstable Employment"
        else:
            return "Low Credit Score"
    else:
        return "Insufficient Income"
