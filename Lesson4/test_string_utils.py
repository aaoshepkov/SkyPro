from task_1 import StringUtils

utils = StringUtils()

def test_capitalize():

    result = utils.capitilize('skypro')
    assert result == 'Skypro'


def test_trim():

    result = utils.trim(' skypro is good')
    assert result == 'skypro is good'


def test_to_list():

    result = utils.to_list('skypro, skyeng, python, english', ', ')
    assert result == ['skypro', 'skyeng', 'python', 'english']

    result = utils.to_list(' ', '')
    assert result == []

def test_contains():

    result = utils.contains('skypro', 'y')
    assert result == True

    result = utils.contains('skypro', 'a')
    assert  result == False


def test_delete_symbol():

    result = utils.delete_symbol('skypro', 's')
    assert result == 'kypro'

    result = utils.delete_symbol('skypro', 'o')
    assert result == 'skypr'


def test_starts_with():

    result = utils.starts_with('skypro', 's')
    assert result == True

    result = utils.starts_with('skypro', 'o')
    assert result == False


def test_end_with():

    result = utils.end_with('skypro', 's')
    assert result == False

    result = utils.end_with('skypro', 'o')
    assert result == True


def test_is_empty():

    result = utils.is_empty('skypro')
    assert result == False

    result = utils.is_empty('')
    assert result == True


def test_list_to_string():

    result = utils.list_to_string(['skypro', 'is', '№', 1], ' ')
    assert result == 'skypro is № 1'

