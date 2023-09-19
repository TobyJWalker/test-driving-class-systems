import pytest
from lib.diary_entry import DiaryEntry

def test_diary_entry_title_empty():
    with pytest.raises(ValueError) as e:
        DiaryEntry('', 'contents')
    assert str(e.value) == 'Title cannot be empty'

def test_diary_entry_title_is_space():
    with pytest.raises(ValueError) as e:
        DiaryEntry(' ', 'contents')
    assert str(e.value) == 'Title cannot be empty'

def test_diary_entry_contents_empty():
    with pytest.raises(ValueError) as e:
        DiaryEntry('title', '')
    assert str(e.value) == 'Contents cannot be empty'
    
def test_diary_entry_contents_is_space():
    with pytest.raises(ValueError) as e:
        DiaryEntry('title', ' ')
    assert str(e.value) == 'Contents cannot be empty'

def test_diary_entry_title_valid():
    entry = DiaryEntry('title', 'contents')
    assert entry.title == 'title'

def test_diary_entry_contents_valid():
    entry = DiaryEntry('title', 'contents')
    assert entry.contents == 'contents'

def test_diary_entry_count_words():
    entry = DiaryEntry('title', 'contents')
    assert entry.count_words() == 1

def test_diary_entry_count_words_multiple():
    entry = DiaryEntry('title', 'contents words')
    assert entry.count_words() == 2

def test_diary_entry_wpm_not_num():
    entry = DiaryEntry('title', 'contents')
    with pytest.raises(ValueError) as e:
        entry.reading_time('wpm')
    assert str(e.value) == 'wpm must be an integer'

def test_diary_entry_reading_time():
    entry = DiaryEntry('title', 'one two three four')
    assert entry.reading_time(4) == 1

def test_diary_entry_reading_time_rounded():
    entry = DiaryEntry('title', 'one two three four')
    assert entry.reading_time(3) == 2

def test_reading_chunk_wpm_not_num():
    entry = DiaryEntry('title', 'contents')
    with pytest.raises(ValueError) as e:
        entry.reading_chunk('wpm', 1)
    assert str(e.value) == 'wpm must be an integer'

def test_reading_chunk_minutes_not_num():
    entry = DiaryEntry('title', 'contents')
    with pytest.raises(ValueError) as e:
        entry.reading_chunk(1, 'minutes')
    assert str(e.value) == 'minutes must be an integer'

def test_reading_chunk_returns_chunk():
    entry = DiaryEntry('title', 'one two three four')
    assert entry.reading_chunk(2, 1) == 'one two'

def test_reading_next_chunk():
    entry = DiaryEntry('title', 'one two three four')
    entry.reading_chunk(2, 1)
    assert entry.reading_chunk(2, 1) == 'three four'

def test_reading_end_chunk_resets_to_start():
    entry = DiaryEntry('title', 'one two three four')
    entry.reading_chunk(2, 1)
    entry.reading_chunk(2, 1)
    assert entry.reading_chunk(2, 1) == 'one two'