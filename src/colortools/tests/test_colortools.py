import pytest

from colortools import Color


def test_init_rgb_color_correctly():
    c = Color(1, 2, 3)
    assert c.red == 1
    assert c.green == 2
    assert c.blue == 3
    assert c.alpha == 255


def test_init_from_rgba():
    assert Color(1, 2, 3, 255) == Color(1, 2, 3)


def test_init_color_from_name():
    assert Color('red') == Color(255, 0, 0)
    assert Color('lime') == Color(0, 255, 0)  # HTML name convention...
    assert Color('blue') == Color(0, 0, 255)


def test_init_from_3_hex():
    assert Color('#0F0') == Color(0, 255, 0)


def test_init_from_4_hex():
    assert Color('#0F01') == Color(0, 255, 0, 17)


def test_init_from_6_hex():
    assert Color('#00FF00') == Color(0, 255, 0)


def test_init_from_8_hex():
    assert Color('#00FF0080') == Color(0, 255, 0, 128)


def test_init_from_color():
    black = Color(0, 0, 0)
    assert Color(black) == black


def test_init_from_sequence():
    black = Color(0, 0, 0)
    assert Color([0, 0, 0]) == black
    assert Color((0, 0, 0)) == black
    assert Color((0, 0, 0, 255)) == black


def test_color_compares_with_tuple():
    color = Color('red')
    assert color == (255, 0, 0, 255)
    assert color == (255, 0, 0)


def test_getitem_color():
    color = Color(1, 2, 3, 4)
    assert color[0] == 1
    assert color[1] == 2
    assert color[2] == 3
    assert color[3] == 4


def test_getitem_fails():
    color = Color(1, 2, 3, 4)
    with pytest.raises(IndexError):
        color[4]


def test_init_color_from_color():
    black = Color('black')
    assert Color(black) == black
