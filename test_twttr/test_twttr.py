from twttr import shorten


def test_vowels():
    assert shorten('James') == 'Jms'
    assert shorten('Antonio') == 'ntn'
    assert shorten('Lumbag') == 'Lmbg'
    assert shorten('Michael') == 'Mchl'
    assert shorten('3faog') == '3fg'
    assert shorten('$grammer$') == '$grmmr$'
