import pytest
from string_utils import StringUtils

stringU = StringUtils()

@pytest.mark.parametrize("cap, res", [("skypro", "Skypro"), ("s","S"), ("s skypro", "S skypro")])
def test_capitilize(cap, res):
    stringU = StringUtils()
    check = stringU.capitilize(cap)
    assert check == res

@pytest.mark.parametrize("tri, res", [(" left", "left"), ("  left", "left"), ("   left", "left")])
def test_trim(tri, res):
    stringU = StringUtils()
    check = stringU.trim(tri)
    assert check == res

@pytest.mark.parametrize("li, i, res", [("a,b,c,d",(","),["a", "b", "c", "d"]), (("1:2:3"),(":"),["1", "2", "3"]), ("a;b;c;d",(";"),["a", "b", "c", "d"]), (("1/2/3"),("/"),["1", "2", "3"])])
def test_to_list(li, i, res):
    stringU = StringUtils()
    check = stringU.to_list(li, i)
    assert check == res

@pytest.mark.parametrize("con, i, res", [("skypro", "k", True), ("mark", "s", False)])
def test_contains(con, i, res):
    stringU = StringUtils()
    check = stringU.contains(con, i)
    assert check == res

@pytest.mark.parametrize("dels, i, res",[("skypro", "sky","pro"), ("mark", "m","ark")])
def test_delete_symbol(dels, i, res):
    stringU = StringUtils()
    check = stringU.delete_symbol(dels, i)
    assert check == res

@pytest.mark.parametrize("star, i, res", [("test", "t", True), ("tests", "e", False)])
def test_starts_with(star, i, res):
    stringU = StringUtils()
    check = stringU.starts_with(star, i)
    assert check == res

@pytest.mark.parametrize("en, i, res", [("phone", "e", True), ("phone", "h", False)])
def test_end_with(en, i, res):
    stringU = StringUtils()
    check = stringU.end_with(en, i)
    assert check == res

@pytest.mark.parametrize("iss, res", [("   ", True), ("f", False)])
def test_is_empty(iss, res):
    stringU = StringUtils()
    check = stringU.is_empty(iss)
    assert check == res

@pytest.mark.parametrize("lis, i, res", [(["Sky", "Pro"], "", "SkyPro"), (["Sky", "Pro"], "-", "Sky-Pro")])
def test_list_to_string(lis, i, res):
    stringU = StringUtils()
    check = stringU.list_to_string(lis, i)
    assert check == res