from math import ceil

class DiaryEntry:
    # Public Properties:
    #   title: a string
    #   contents: a string

    def __init__(self, title, contents): # title, contents are strings
        if title == '' or title.isspace():
            raise ValueError('Title cannot be empty')
        elif contents == '' or contents.isspace():
            raise ValueError('Contents cannot be empty')
        self.title = title
        self.contents = contents
        self.unread = contents

    def count_words(self):
        return len(self.contents.split())

    def reading_time(self, wpm):
        if type(wpm) != int:
            raise ValueError('wpm must be an integer')
        return ceil(self.count_words() / wpm)

    def reading_chunk(self, wpm, minutes):
        if type(wpm) != int:
            raise ValueError('wpm must be an integer')
        elif type(minutes) != int:
            raise ValueError('minutes must be an integer')
        
        words = self.unread.split()
        word_count = wpm * minutes

        if word_count >= len(words):
            self.unread = self.contents
            return ' '.join(words)
        else:
            self.unread = ' '.join(words[word_count:])
            return ' '.join(words[:word_count])