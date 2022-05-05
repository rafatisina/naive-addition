from src.add import add
def test_add():
    assert add(1) == 101

def test_add_string():
    assert add("Fourth","Brain")=="FourthBrain"

