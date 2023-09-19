import pytest
from lib.diary import Diary
from lib.diary_entry import DiaryEntry

def test_diary_add_not_entry():
    diary = Diary()
    with pytest.raises(TypeError) as e:
        diary.add('not an entry')
    assert str(e.value) == 'Diary.add only accepts instances of DiaryEntry'

def test_diary_add_entry():
    diary = Diary()
    entry = DiaryEntry('title', 'contents')
    diary.add(entry)
    assert diary.entries == [entry]

def test_get_all_entries():
    diary = Diary()
    entry = DiaryEntry('title', 'contents')
    diary.add(entry)
    assert diary.all() == [entry]

def test_count_all_words_one_entry():
    diary = Diary()
    entry = DiaryEntry('title', 'contents')
    diary.add(entry)
    assert diary.count_words() == 1

def test_count_all_words_multiple_entries():
    diary = Diary()
    entry1 = DiaryEntry('title', 'contents')
    entry2 = DiaryEntry('title', 'This has more words')
    diary.add(entry1)
    diary.add(entry2)
    assert diary.count_words() == 5

def test_reading_time_whole_result():
    diary = Diary()
    entry = DiaryEntry('title', 'one two three four')
    diary.add(entry)
    diary.add(entry)
    assert diary.reading_time(4) == 2

def test_reading_time_decimal_result():
    diary = Diary()
    entry = DiaryEntry('title', 'one two three four')
    diary.add(entry)
    diary.add(entry)
    assert diary.reading_time(3) == 3

def test_best_entry_for_reading_time_non_valid():
    diary = Diary()
    entry = DiaryEntry('title', 'one two three four')
    diary.add(entry)
    diary.add(entry)
    assert diary.find_best_entry_for_reading_time(3, 1) == None

def test_best_entry_for_reading_time():
    diary = Diary()
    entry1 = DiaryEntry('title', 'one two three four')
    entry2 = DiaryEntry('title', 'one two three four five six')
    entry3 = DiaryEntry('title', 'one')
    diary.add(entry1)
    diary.add(entry2)
    diary.add(entry3)s
    assert diary.find_best_entry_for_reading_time(4, 1) == entry1