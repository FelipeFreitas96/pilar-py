from services.word_service import WordService

service = WordService()

def test_get_vowals_count():
    assert service.getVowalsCount('hello') == 2
    assert service.getVowalsCount('world') == 1
    assert service.getVowalsCount('aeiou') == 5
    assert service.getVowalsCount('') == 0
    assert service.getVowalsCount('aaaaaaaaa') == 9
    assert service.getVowalsCount('bbbbbbbb') == 0
    assert service.getVowalsCount('aeiouaeiouaeiouaeiouaeiou') == 25
    assert service.getVowalsCount('"!@#$%¨&*()_+{}:?></*-+,0°¹²³£¢¬~´`₢') == 0
    assert service.getVowalsCount('àáèéìíòóùú') == 10
    
def test_get_vowals_from_array():
    assert service.getVowalsFromArray(['hello', 'world', 'aeiou', '']) == { 'hello': 2, 'world': 1, 'aeiou': 5 }
    assert service.getVowalsFromArray(['aaaaaaaaa', 'bbbbbbbb', 'aeiouaeiouaeiouaeiouaeiou']) == { 'aaaaaaaaa': 9, 'bbbbbbbb': 0, 'aeiouaeiouaeiouaeiouaeiou': 25 }
    assert service.getVowalsFromArray(['"!@#$%¨&*()_+{}:?></*-+,0°¹²³£¢¬~´`₢', 'àáèéìíòóùú']) == { '"!@#$%¨&*()_+{}:?></*-+,0°¹²³£¢¬~´`₢': 0, 'àáèéìíòóùú': 10 }
    assert service.getVowalsFromArray(['']) == {}
    assert service.getVowalsFromArray([]) == {}
    