from twttr import shorten


def test_vowels():
    assert shorten('James') == 'Jms'
    assert shorten('Antonio') == 'ntn'
    assert shorten('Lumbag') == 'Lmbg'
    assert shorten('Michael') == 'Mchl'


def test_numbers():
    assert shorten('3faog') == '3fg'

def test_punctuation():
    assert shorten('$grammer$') == '$grmmr$'
