import pytest
from string_utils import StringUtils


@pytest.fixture
def utils():
    """Фикстура для создания экземпляра класса StringUtils
    перед каждым тестом."""
    return StringUtils()


@pytest.mark.parametrize("input_str, expected", [
    # Позитивные сценарии
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("абракадабра", "Абракадабра"),
    # Граничные условия
    ("A", "A"),
    ("a", "A"),
    ("", ""),  # Пустая строка
    ("   ", "   "),  # Строка из пробелов
    ("123sky", "123sky"),  # Начинается с цифры
    ("!sky", "!sky"),  # Начинается со спецсимвола
])
def test_capitalize(utils, input_str, expected):
    assert utils.capitalize(input_str) == expected


@pytest.mark.parametrize("input_str, expected", [
    # Позитивные сценарии
    ("   skypro", "skypro"),
    (" skypro", "skypro"),
    ("   skypro   ", "skypro   "),  # Пробелы в конце не должны
    # удаляться согласно докстрингу

    # Негативные / Граничные сценарии
    ("skypro", "skypro"),  # Нет пробелов в начале
    ("", ""),  # Пустая строка
    ("   ", ""),  # Только пробелы
    ("\t skypro", "\t skypro"),  # Другие виды пробельных символов (табуляция)
    # не удаляются
])
def test_trim(utils, input_str, expected):
    assert utils.trim(input_str) == expected


@pytest.mark.parametrize("input_str, symbol, expected", [
    # Позитивные сценарии
    ("SkyPro", "S", True),
    ("SkyPro", "Pro", True),
    ("Привет", "и", True),
    # Негативные сценарии
    ("SkyPro", "U", False),
    ("SkyPro", "s", False),  # Чувствительность к регистру
    ("", "A", False),  # Поиск в пустой строке
    # Специальные случаи
    ("SkyPro", "", True),  # Поиск пустой строки (в Python "" всегда
    # содержится в строке)
])
def test_contains(utils, input_str, symbol, expected):
    assert utils.contains(input_str, symbol) == expected


@pytest.mark.parametrize("input_str, symbol, expected", [
    # Позитивные сценарии
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("xoxo", "x", "oo"),  # Удаление всех вхождений символа
    # Негативные сценарии (символ отсутствует)
    ("SkyPro", "U", "SkyPro"),
    ("SkyPro", "kPro", "SkyPro"),
    ("", "A", ""),  # Удаление из пустой строки
    # Граничные сценарии
    ("SkyPro", "", "SkyPro"),  # Удаление пустой строки
    ("banana", "an", "ba"),  # Удаление повторяющихся подстрок
])
def test_delete_symbol(utils, input_str, symbol, expected):
    assert utils.delete_symbol(input_str, symbol) == expected
