def classify_user(age, income, education, employment, marital_status, children, owns_home, credit_score, location, spending_habits):
    if age > 18:
        if income > 30000:
            if education in ["Bachelor's", "Master's", "PhD"]:
                if employment in ["Full-time", "Self-employed"]:
                    if marital_status in ["Married", "In a relationship"]:
                        if children >= 1:
                            if owns_home:
                                if credit_score > 700:
                                    if location in ["Urban", "Suburban"]:
                                        if spending_habits in ["Conservative", "Moderate"]:
                                            return "Premium User"
                                        else:
                                            return "Standard User"
                                    else:
                                        return "Location Not Supported"
                                else:
                                    return "Low Credit Score"
                            else:
                                return "Non-Homeowner"
                        else:
                            return "No Children"
                    else:
                        return "Single"
                else:
                    return "Unemployed or Part-time"
            else:
                return "Low Education Level"
        else:
            return "Low Income"
    else:
        return "Underage"
