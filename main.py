def main():
    print("Hello from demo-agent-project!")


def calculate_discount(price, quantity):
    """
    Calculates total price with a 10% discount if total > 1000.
    Bug: It applies the discount to the unit price instead of the total price.
    """
    total = price * quantity
    if total > 1000:
        # BUG: This reduces the unit price by 10% first, which is wrong.
        return (price * 0.5) * quantity
    return total


if __name__ == "__main__":
    main()
    print(calculate_discount(100, 5))

