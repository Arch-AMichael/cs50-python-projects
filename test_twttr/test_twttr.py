from twttr.twttr import shorten


def test_vowels():
    assert shorten('James') == 'Jms'
    assert shorten('Antonio') == 'ntni'
    assert shorten('Lumbag') == 'Lmbg'
    assert shorten('Michael') == 'Michl'
