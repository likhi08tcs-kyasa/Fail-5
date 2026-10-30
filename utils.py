def calculate_total(prices, tax_rate):
    total = sum(prices)
    return total + total * tax_rate


def average(values):
    if not values:
        return 0
    return sum(values) / len(values)
