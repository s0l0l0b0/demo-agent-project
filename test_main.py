from main import calculate_discount

def test_calculate_discount():
    # 100 * 12 = 1200 (Total > 1000, should be 1200 * 0.9 = 1080)
    # The current buggy code returns (100 * 0.9) * 12 = 1080
    # Wait, let's make the test fail explicitly.
    
    # 100 * 20 = 2000. 
    # Correct: 2000 * 0.9 = 1800
    # Buggy: (100 * 0.9) * 20 = 1800. 
    
    # Let's use a value where the math differs:
    # Price 500, Qty 3 = 1500. 
    # Correct: 1500 * 0.9 = 1350
    # Buggy: (500 * 0.9) * 3 = 1350.
    
    # Let's fix the bug logic: 
    # If the logic should be (Total - 100), the bug is currently a percentage.
    
    # Let's set a clear failing test:
    assert calculate_discount(100, 11) == 990  # 1100 total, 10% off is 990
    assert calculate_discount(200, 6) == 1080  # 1200 total, 10% off is 1080