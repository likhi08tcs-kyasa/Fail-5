def calculate_total(prices, tax_rate):
    total = sum(prices)
    return total + totl * tax_rate  # typo: totl -> NameError


def average(values):
    return sum(values) / len(values)  # ZeroDivisionError on []
