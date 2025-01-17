def describe_number(num):
    if num > 0:
        if num % 2 == 0:
            return "Positive Even"
        else:
            return "Positive Odd"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"
