""" Test the Operations """
# pylint: disable=unnecessary-dunder-call, invalid-name
from decimal import Decimal

import pytest
from app.calculator.calculation import Calculation
from app.calculator.operations import divide


def test_operation(a, b, operation, expected):
    '''Testing various operations'''
    calculation = Calculation.create(a, b, operation)
    assert calculation.perform() == expected, f"{operation.__name__} operation failed"

def test_divide_by_zero():
    '''Testing the divide by zero exception'''
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculation = Calculation(Decimal('10'), Decimal('0'), divide)
        calculation.perform()
