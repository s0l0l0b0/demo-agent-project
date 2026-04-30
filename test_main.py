from main import calculate_discount, get_average_score, format_username

def test_calculate_discount():
    # 100 * 11 = 1100. Total > 1000, 10% off should be 990.
    assert calculate_discount(100, 11) == 990.0
    # 200 * 6 = 1200. Total > 1000, 10% off should be 1080.
    assert calculate_discount(200, 6) == 1080.0

def test_get_average_score():
    assert get_average_score([10, 20, 30]) == 20.0
    # Bug trigger: Empty list should return 0, currently crashes.
    assert get_average_score([]) == 0

def test_format_username():
    # Bug trigger: Trailing space when last_name is empty.
    assert format_username("John", "Doe") == "John Doe"
    assert format_username("John", "") == "John"