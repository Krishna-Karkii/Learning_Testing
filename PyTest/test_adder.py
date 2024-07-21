from add_function import addition


def test_number_addition():
    """Testing the addition function"""
    result = addition(5, 7)
    assert result == 12
