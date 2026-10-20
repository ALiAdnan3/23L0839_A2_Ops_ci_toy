from calc import add, is_ai_label


def test_add():
    assert add(2, 3) == 5


def test_threshold():
    assert is_ai_label(0.9) is True
    assert is_ai_label(0.1) is False
