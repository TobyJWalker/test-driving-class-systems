from lib.diary_entry import DiaryEntry

class Diary:
    def __init__(self):
        self.entries = []

    def add(self, entry):
        if type(entry) != DiaryEntry:
            raise TypeError('Diary.add only accepts instances of DiaryEntry')
        self.entries.append(entry)

    def all(self):
        return self.entries

    def count_words(self):
        word_count = 0
        for entry in self.entries:
            word_count += entry.count_words()
        return word_count

    def reading_time(self, wpm):
        if type(wpm) != int:
            raise ValueError('wpm must be an integer')

        word_count = self.count_words()
        return round(word_count / wpm)

    def find_best_entry_for_reading_time(self, wpm, minutes):
        if type(wpm) != int:
            raise ValueError('wpm must be an integer')
    
        elif type(minutes) != int:
            raise ValueError('minutes must be an integer')
        
        best_entry = None

        for entry in self.entries:
            print(entry.reading_time(wpm))
            if entry.reading_time(wpm) <= minutes:
                if best_entry == None:
                    best_entry = entry
                elif entry.reading_time(wpm) < best_entry.reading_time(wpm):
                    best_entry = entry
        return best_entry
