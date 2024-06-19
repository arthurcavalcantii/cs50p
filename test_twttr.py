from twttr import shorten

def test_shorten():
    assert shorten("hello") == "hll"
    assert shorten("hEllo") == "hll"
    assert shorten("hello1") == "hll1"
    assert shorten("hey, how are you") == "hy, hw r y"
