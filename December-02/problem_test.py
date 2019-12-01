import unittest
from problem import is_valid_credit_card


def test_with_valid_credit_cards():
    numbers = [
        49927398716,
        378282246310005,  # AMEX
        6011111111111117,  # DISCOVER
        5555555555554444,  # MASTERCARD
        4111111111111111  # VISA
    ]

    for number in numbers:
        assert is_valid_credit_card(number) == True


def test_with_negative_credit_card():
    number = -49927398716
    assert is_valid_credit_card(number) == False
