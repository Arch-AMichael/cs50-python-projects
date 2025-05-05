from twttr import shorten


def test_vowels():
    assert shorten('James') == 'Jms'
    assert shorten('Antonio') == 'ntn'
    assert shorten('Lumbag') == 'Lmbg'
    assert shorten('Michael') == 'Mchl'
