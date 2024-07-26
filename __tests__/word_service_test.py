from services.word_service import WordService

service = WordService()

def test_getword():
    assert service.getVowalsCount('hello') == 2
    assert service.getVowalsCount('world') == 1
    assert service.getVowalsCount('aeiou') == 5
    assert service.getVowalsCount('') == 0
    assert service.getVowalsCount('aaaaaaaaa') == 9
    assert service.getVowalsCount('bbbbbbbb') == 0
    assert service.getVowalsCount('aeiouaeiouaeiouaeiouaeiou') == 25
    assert service.getVowalsCount('"!@#$%¨&*()_+{}:?></*-+,0°¹²³£¢¬~´`₢') == 0
    assert service.getVowalsCount('àáèéìíòóùú') == 10
    