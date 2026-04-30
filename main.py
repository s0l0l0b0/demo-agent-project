def main():
    print("Hello from demo-agent-project!")


def calculate_discount(price, quantity):
    """
    Calculates total price with a 10% discount if total > 1000.
    """
    total = price * quantity
    if total > 1000:
        # Apply 10% discount to the total (pay 90%)
        return total * 0.9
    return total


if __name__ == "__main__":
    main()
    print(calculate_discount(100, 5))