from services.word_service import WordService

service = WordService()

def test_get_vowals_count():
    assert service.get_vowals_count('hello') == 2
    assert service.get_vowals_count('world') == 1
    assert service.get_vowals_count('aeiou') == 5
    assert service.get_vowals_count('') == 0
    assert service.get_vowals_count('aaaaaaaaa') == 9
    assert service.get_vowals_count('bbbbbbbb') == 0
    assert service.get_vowals_count('aeiouaeiouaeiouaeiouaeiou') == 25
    assert service.get_vowals_count('"!@#$%¨&*()_+{}:?></*-+,0°¹²³£¢¬~´`₢') == 0
    assert service.get_vowals_count('àáèéìíòóùú') == 10
    
def test_get_vowals_from_array():
    assert service.get_vowals_from_array(['hello', 'world', 'aeiou', '']) == { 'hello': 2, 'world': 1, 'aeiou': 5 }
    assert service.get_vowals_from_array(['aaaaaaaaa', 'bbbbbbbb', 'aeiouaeiouaeiouaeiouaeiou']) == { 'aaaaaaaaa': 9, 'bbbbbbbb': 0, 'aeiouaeiouaeiouaeiouaeiou': 25 }
    assert service.get_vowals_from_array(['"!@#$%¨&*()_+{}:?></*-+,0°¹²³£¢¬~´`₢', 'àáèéìíòóùú']) == { '"!@#$%¨&*()_+{}:?></*-+,0°¹²³£¢¬~´`₢': 0, 'àáèéìíòóùú': 10 }
    assert service.get_vowals_from_array(['']) == {}
    assert service.get_vowals_from_array([]) == {}
    