from stringlib.stringlib import basic_capitalize
import pytest

# Test the basic_capitalize function
def test_capitalize():
    # initialize
    value = "test value"
    expected = "Test value"
    # act
    res = basic_capitalize(value)
    # test
    assert res == expected

# Test for empty values
def test_empty_capitalize():
    # When the input string is empty, it should remain empty after capitalization
    value = ""
    expected = ""
    res = basic_capitalize(value)
    assert res == expected

# Test for string starting with a number
def test_number_capitalize():
    # When the input string starts with a number, it should be capitalized normally
    value = "123 string"
    expected = "123 string"
    res = basic_capitalize(value)
    assert res == expected

# Test for None values
def test_none_capitalize():
    # When the input is None, it should return None without attempting to capitalize
    value = None
    expected = None
    res = basic_capitalize(value)
    assert res == expected

# Test for wrong data type
def test_wrong_type_capitalize():
    # When the input is not a string, it should return the input without attempting to capitalize
    value = 123
    expected = 123
    res = basic_capitalize(value)
    assert res == expected

# Parametrized tests for different input values
@pytest.mark.parametrize("input_str, expected_output", [
    ("normal string", "Normal string"),  # Capitalize a normal string
    ("", ""),  # Test an empty string
    ("123 string", "123 string")  # Test a string starting with a number
])
def test_capitalize_values(input_str, expected_output):
    res = basic_capitalize(input_str)
    assert res == expected_output



