from task_1 import StringUtils


def test_capitalize():

    utils = StringUtils()

    result = utils.capitalize('skypro')
    assert result == 'Skypro'



def test_trim():

    utils = StringUtils()

    result = utils.trim(' skypro')
    assert result == 'skypro'



def test_to_list():

    utils = StringUtils()

    result = utils.to_list('skypro, skyeng, python, english', ', ')
    assert result == ['skypro', 'skyeng', 'python', 'english']


def test_contains():

    utils = StringUtils()

    result = utils.contains('skypro', 'y')
    assert result == True

    result = utils.contains('skypro', 'a')
    assert  result == False


def test_delete_symbol():

    utils = StringUtils()

    result = utils.delete_symbol('skypro', 's')
    assert result == 'kypro'

    result = utils.delete_symbol('skypro', 'o')
    assert result == 'skypr'


def test_starts_with():

    utils = StringUtils()

    result = utils.starts_with('skypro', 's')
    assert result == True

    result = utils.starts_with('skypro', 'o')
    assert result == False


def test_end_with():

    utils = StringUtils()

    result = utils.end_with('skypro', 's')
    assert result == False

    result = utils.end_with('skypro', 'o')
    assert result == True


def test_is_empty():

    utils = StringUtils()

    result = utils.is_empty('skypro')
    assert result == False

    result = utils.is_empty('')
    assert result == True


def test_list_to_string():

    utils = StringUtils()

    result = utils.list_to_string(['skypro', 'is', '№', 1], ' ')
    assert result == 'skypro is № 1'

