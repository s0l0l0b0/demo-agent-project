def calculate_discount(price, quantity):
    """
    Calculates total price with a 10% discount if total > 1000.
    Bug: It applies a 50% discount to the unit price instead of a 10% discount to the total.
    """
    total = price * quantity
    if total > 1000:
        # BUG: Currently applying a 50% discount instead of 10% to the total
        return (price * 0.5) * quantity
    return float(total)

def get_average_score(scores):
    """
    Calculates the average of a list of scores.
    Bug: Does not handle empty lists, will throw ZeroDivisionError.
    """
    return sum(scores) / len(scores)

def format_username(first_name, last_name):
    """
    Formats a full name.
    Bug: If last_name is empty string, it leaves a trailing space.
    """
    return f"{first_name} {last_name}"

def main():
    print("Hello from demo-agent-project!")

if __name__ == "__main__":
    main()