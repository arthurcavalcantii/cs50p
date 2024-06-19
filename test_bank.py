from bank import value

def test_value1():
    assert value("hello") == "0"
def test_value2():
    assert value("hey") == "20"
def test_value3():
    assert value("arthur") == "100"