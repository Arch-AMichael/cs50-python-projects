from bank import value


def test_mistake():
    assert value('Hello') == '$100'
    assert value('Whats up') == '$20'
    assert value('Hey you') == '$0'

def test_correct():
    assert value('Hello') == '$100'
    assert value('Whats up') == '$100'
    assert value('Hey you') == '$100'
