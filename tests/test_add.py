from src.add import add
def test_add():
    assert add(1) == 101

def test_add_string():
    assert add("Fourth","Brain")=="FourthBrain"

def test_add_1array():
    assert add([1,2]) == 103
	
def test_add_2array():
    assert add ([1,2],[3,4])==10
