import pytest
from lib.diary import Diary

def test_diary_initiation():
    diary = Diary()
    assert diary.entries == []

def test_reading_time_wpm_not_num():
    diary = Diary()
    with pytest.raises(ValueError) as e:
        diary.reading_time('wpm')
    assert str(e.value) == 'wpm must be an integer'

def test_best_time_wpm_not_num():
    diary = Diary()
    with pytest.raises(ValueError) as e:
        diary.find_best_entry_for_reading_time('wpm', 1)
    assert str(e.value) == 'wpm must be an integer'

def test_best_time_mins_not_num():
    diary = Diary()
    with pytest.raises(ValueError) as e:
        diary.find_best_entry_for_reading_time(1, 'mins')
    assert str(e.value) == 'minutes must be an integer'