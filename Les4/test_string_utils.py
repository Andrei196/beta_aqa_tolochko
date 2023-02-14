import pytest
from string_utils import StringUtils

# Здесь был объект класса и я его придерживался... Просто забыл удалить.
# Возможно есть какие то правила китикета в название переменных, но как нам говорится чуть ли не в каждом уроке -переменную можно называть как угодно. Мне пришло в голову, что так будет интересно. Вот я и выбрал такое имя.

@pytest.mark.parametrize("cap, res", [("skypro", "Skypro"), ("s","S"), ("", ""), ("s skypro", "S skypro"), 
("мама мыла раму.", "Мама мыла раму.")]) # Как и просили было добавлено предложение. Смысл функции в том, что на любые вводимые текстовые данные будет только одно действие. Сделать любую первую букву заглавной.
def test_capitilize(cap, res):           # Да, если ввести пару предложений, то во втором предложении первое слово не получит приоритет первого слова, соответственно не будет получать модификатор.
    stringU = StringUtils()              # Но от этой функции этого и не требовалось. Я считаю, что такой список проверок крайне исчерпывающем и на длину текста он не влияет.
    check = stringU.capitilize(cap)      # С другой стороны добавленная проверка("", ""), является багом.
    assert check == res

@pytest.mark.parametrize("tri, res", [(" left", "left"), ("  left", "left"), ("   left", "left"), ("          left", "left")])
def test_trim(tri, res):                 # Я попробовал добавления проверок ("le ft", "left") и ("left  ", "left"). Как и ожидалось они выдали ошибку. Я не считаю, что их необходимо добавлять в исключения, так как
    stringU = StringUtils()              # функция  выполняет только одно условие (удалить пробелы в начале текста). Если бы функция имела переменную "elif" и по мимо одной команды могла выполнять действия исключений, то 
    check = stringU.trim(tri)            # в таком случае такие проверки были бы оправданы.
    assert check == res

@pytest.mark.parametrize("li, i, res", [("a,b,c,d",(","),["a", "b", "c", "d"]), (("1:2:3"),(":"),["1", "2", "3"]), ("a;b;c;d",(";"),["a", "b", "c", "d"]), (("1/2/3"),("/"),["1", "2", "3"])])
def test_to_list(li, i, res):            #("a,b,c,d",(","),["a", "b", "c", "d"]) такой метод написания запроса был выбран исходя из наличия переменной "i". Так или иначе для проверки "," переменная "i" не требуется, а сделал 
    stringU = StringUtils()              # так я для сокращения.
    check = stringU.to_list(li, i)
    assert check == res

@pytest.mark.parametrize("con, i, res", [("skypro", "k", True), ("mark", "s", False), ("markmarkmarkmark", "k", True), ("ma rk", " ", True), ("ma,rk", ",", True), ("ma rk", " ", True)])
def test_contains(con, i, res):          # Согласно функиональным особенностям скрипта. В строке ищется любой символ. Получается все символы вводимые с клавиатуры и оставляющие за собой элемент являются верными.
    stringU = StringUtils()              # Получается, сколько бы одинаковых символов небыло или ежели эти символы "пробел" итд. Функция возьмет любой и будет верно исполненой.
    check = stringU.contains(con, i)
    assert check == res

@pytest.mark.parametrize("dels, i, res",[("skypro", "sky","pro"), ("mark", "m","ark"), ("skyskyprosky", "sky","pro")])
def test_delete_symbol(dels, i, res):    # Если я все правильно понял из того, что от меня требовалось, то я добавил такую проверку, а если я так и не понял, то все равно я удивлен, что так тоже можно.
    stringU = StringUtils()              # Хотя если подумать, то почему нельзя... Функцию просят найти и удалить конкретный набор символов.
    check = stringU.delete_symbol(dels, i)
    assert check == res

@pytest.mark.parametrize("star, i, res", [("test", "t", True), ("tests", "e", False), (" test", " ", True)])
def test_starts_with(star, i, res):
    stringU = StringUtils()
    check = stringU.starts_with(star, i)
    assert check == res

@pytest.mark.parametrize("en, i, res", [("phone", "e", True), ("phone", "h", False), ("phone ", " ", True)])
def test_end_with(en, i, res):           # Непосредственно по этим двум работам у меня нет комментария. Символ есть символ.
    stringU = StringUtils()
    check = stringU.end_with(en, i)
    assert check == res

@pytest.mark.parametrize("iss, res", [("   ", True), ("f", False), ("", True)])
def test_is_empty(iss, res):
    stringU = StringUtils()
    check = stringU.is_empty(iss)
    assert check == res

@pytest.mark.parametrize("lis, i, res", [(["Sky", "Pro"], "", "SkyPro"), (["Sky", "Pro"], "-", "Sky-Pro"), (["Sky", ""], "-", "Sky-"), (["Sky", "Pro"], ",", "Sky,Pro")])
def test_list_to_string(lis, i, res):     # Тут у меня такой же метод решения как и в третьей проверке. Если нет переменной "i", то разделитель по умолчанию будет работать.
    stringU = StringUtils()
    check = stringU.list_to_string(lis, i)
    assert check == res