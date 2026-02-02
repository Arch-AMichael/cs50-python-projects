"""In a file called plates.py,
reimplement Vanity Plates from Problem Set 2,
restructuring your code per the below,
wherein is_valid still expects a str as input and returns True if that str meets all requirements and False if it does not,
but main is only called if the value of __name__ is __main__:

Then, in a file called test_plates.py,
implement four or more functions that collectively test your implementation of is_valid thoroughly,
each of whose names should begin with test_ so that you can execute your tests with:

pytest test_plates.py"""

from plates import is_valid


def test_length():
    assert is_valid("CS50") == True
    assert is_valid("CS") == True
    assert is_valid("C") == False
    assert is_valid("CS50") == True
    assert is_valid("CS50PY") == False
    assert is_valid("CS50PYT") == False
    assert is_valid("") == False


def test_start_letters():
    assert is_valid("CS50") == True
    assert is_valid("CS") == True
    assert is_valid("CV50") == True
    assert is_valid("5CS") == False
    assert is_valid("50CS") == False
    assert is_valid("C") == False


def test_number_placement():
    assert is_valid("CS50") == True
    assert is_valid("CSO5") == True
    assert is_valid("CS505") == True
    assert is_valid("CS") == True
    assert is_valid("CS5O") == False
    assert is_valid("CS50P") == False
    assert is_valid("CS5P0") == False
    assert is_valid("C5S0") == False
    assert is_valid("C5") == False


def test_first_number_not_zero():
    assert is_valid("CS50") == True
    assert is_valid("CS") == True
    assert is_valid("CS5") == True
    assert is_valid("CS05") == False
    assert is_valid("CS0") == False
    assert is_valid("C0") == False
    assert is_valid("C5") == False


def test_no_punctuation():
    assert is_valid("CS50") == True
    assert is_valid("CSO5") == True
    assert is_valid("CSO") == True
    assert is_valid("CS") == True
    assert is_valid("C5") == False
    assert is_valid("CS-50") == False
    assert is_valid("CS.50") == False


def test_no_numbers():
    assert is_valid("CS") == True
    assert is_valid("CSO") == True
    assert is_valid("CS50") == True
    assert is_valid("CSO5") == True
    assert is_valid("CS5O") == False
    assert is_valid("C") == False


def test_no_special_characters():
    assert is_valid("CS50") == True
    assert is_valid("CSO") == True
    assert is_valid("CS") == True
    assert is_valid("CS@50") == False
    assert is_valid("CS#50") == False
    assert is_valid("CS$50") == False
    assert is_valid("CS%50") == False
    assert is_valid("CS^50") == False
    assert is_valid("CS&50") == False
    assert is_valid("CS*50") == False
    assert is_valid("CS(50)") == False
