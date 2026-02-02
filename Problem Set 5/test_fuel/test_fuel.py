import pytest
from fuel import convert, gauge


def test_convert():
    assert convert("1/9") == 11
    assert convert("2/8") == 25
    assert convert("3/4") == 75
    assert convert("3/5") == 60
    assert convert("1/9") == 11


def test_gauge():
    assert gauge(23) == f"{23}%"
    assert gauge(100) == "F"
    assert gauge(150) == "F"
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(-1) == "E"
    assert gauge(59) == f"{59}%"
    assert gauge(99) == "F"


def test_invalid_convert():  ## This was the real problem, I did'nt have the function to test for errors. Thanks chatgpt :)
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ValueError):
        convert("5/2")  # x > y
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ZeroDivisionError):
        convert("7/0")
    with pytest.raises(ValueError):
        convert("-1/7")
