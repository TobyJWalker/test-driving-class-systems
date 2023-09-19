>> TESTS

entry = DiaryEntry("My First Entry", "This is the contents of my first entry")
diary = Diary()

>> When creating a diary entry, the title should not be empty
DiaryEntry("", "This is the contents of my first entry") raises ValueError

>> When creating a diary entry, the contents should not be empty
DiaryEntry("My First Entry", "") raises ValueError

>> When creating a diary entry, the title and contents should be set
entry.title => "My First Entry"
entry.title => "This is the contents of my first entry"

>> When count_words is called, the amount of words in contents should be returned
entry.count_words() => 8

>> When calculating reading time, the words per minute should be an integer
entry.calculate_reading_time('string') raises TypeError

>> When calculating reading time, the output should be the number of minutes
entry.calculate_reading_time(8) => 1

>> When reading a chunk, the wpm should be an integer
entry.read_chunk('string', 1) raises TypeError

>> When reading a chunk, the minutes should be an integer
entry.read_chunk(8, 'string') raises TypeError

>> When reading a chunk, the chunk should be returned
entry.read_chunk(4, 1) => "This is the contents"

>> When reading a chunk again, it should return the next chunk
entry.read_chunk(4, 1)
entry.read_chunk(4, 1) => "of my first entry"

>> When reading a whole chunk, it should reset back to the start the next time a chunk is read
entry.read_chunk(8, 1)
entry.read_chunk(4, 1) => "This is the contents"

>> When creating a diary, the entries should be empty
diary.entries => []

>> When adding an entry, the entry should be of class DiaryEntry (Integration)
diary.add("My First Entry", "This is the contents of my first entry") raises TypeError
diary.add(DiaryEntry("My First Entry", "This is the contents of my first entry")) => None

>> When adding an entry, the entry should be added to the entries (Integration)
diary.add(DiaryEntry("My First Entry", "This is the contents of my first entry"))
diary.entries => [DiaryEntry("My First Entry", "This is the contents of my first entry")]

>> When calling all entries, the list of entries should be returned (Integration)
diary.all() => [DiaryEntry("My First Entry", "This is the contents of my first entry")]

>> When counting all diary words, the total amount of words in all contents should be returned (Integration)
diary.add(DiaryEntry("My Second Entry", "This is the contents of my second entry"))
diary.count_words() => 16

>> When calculating all diary reading time, wpm should be an integer
diary.calculate_reading_time('string') raises TypeError

>> When calculating all diary reading time, the output should be the total number of minutes rounded to read all entries (Integration)
diary.calculate_reading_time(4) => 4 (for the two previous entries)
diary.calculate_reading_time(3) => 5 (for the two previous entries)

>> When finding the best entry for reading time, the wpm should be an integer
diary.find_best_entry_for_reading_time('string', 1) raises TypeError

>> When finding the best entry for reading time, the minutes should be an integer
diary.find_best_entry_for_reading_time(4, 'string') raises TypeError

>> When finding the best entry for reading time, the entry with the highest closest reading time below the minutes should be returned (Integration)
diary.find_best_entry_for_reading_time(4, 1) => DiaryEntry("My First Entry", "This is the contents of my first entry")

>> When finding the best entry for reading time, any entries which take too long should not show (Integration)
diary.find_best_entry_for_reading_time(1, 1) => None