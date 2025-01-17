

import pytest

from student_board import classify_user

@pytest.mark.parametrize(
    "age, income, education, employment, marital_status, children, owns_home, credit_score, location, spending_habits, expected",
    [
        # Caso 1: Premium User
        (30, 80000, "Master's", "Full-time", "Married", 2, True, 750, "Urban", "Moderate", "Premium User"),

        # Caso 2: Standard User (gastos fora do esperado)
        (30, 80000, "Master's", "Full-time", "Married", 2, True, 750, "Urban", "Extravagant", "Standard User"),

        # Caso 3: Location Not Supported
        (30, 80000, "Master's", "Full-time", "Married", 2, True, 750, "Rural", "Moderate", "Location Not Supported"),

        # Caso 4: Low Credit Score
        (30, 80000, "Master's", "Full-time", "Married", 2, True, 600, "Urban", "Moderate", "Low Credit Score"),

        # Caso 5: Non-Homeowner
        (30, 80000, "Master's", "Full-time", "Married", 2, False, 750, "Urban", "Moderate", "Non-Homeowner"),

        # Caso 6: No Children
        (30, 80000, "Master's", "Full-time", "Married", 0, True, 750, "Urban", "Moderate", "No Children"),

        # Caso 7: Single
        (30, 80000, "Master's", "Full-time", "Single", 2, True, 750, "Urban", "Moderate", "Single"),

        # Caso 8: Unemployed or Part-time
        (30, 80000, "Master's", "Part-time", "Married", 2, True, 750, "Urban", "Moderate", "Unemployed or Part-time"),

        # Caso 9: Low Education Level
        (30, 80000, "High School", "Full-time", "Married", 2, True, 750, "Urban", "Moderate", "Low Education Level"),

        # Caso 10: Low Income
        (30, 20000, "Master's", "Full-time", "Married", 2, True, 750, "Urban", "Moderate", "Low Income"),

        # Caso 11: Underage
        (16, 50000, "Master's", "Full-time", "Married", 2, True, 750, "Urban", "Moderate", "Underage"),
    ],
)
def test_classify_user(age, income, education, employment, marital_status, children, owns_home, credit_score, location, spending_habits, expected):
    result = classify_user(age, income, education, employment, marital_status, children, owns_home, credit_score, location, spending_habits)
    assert result == expected
