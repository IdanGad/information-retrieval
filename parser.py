# The objective of this class is to break down each lyric document to words, and to not include stop words.
from datetime import datetime

def remove_special_chars(word):
    answer = ""
    for char in str(word):
        if char.isalnum() or char.isspace():
            answer += char

    return answer


def run_parser():
    # Workflow:
    # 1. Read the songs names from 'songsRunTimeFetch' because it's containing all songs that downloaded
    # 2. Add index to all the songs names, so we can read the files
    # 3. Clean the lyrics - lower case ,and delete stop words
    # 4. Save a new file with the clean words

    songsLyrics_and_runtime_file = open('songsRunTimeFetch.txt', 'r')  # Capture all the downloaded songs
    songs_from_file = songsLyrics_and_runtime_file.readlines()  # Reads all the lines from the file, and save as list

    stop_words_file = open('stop words.txt', 'r')  # Open the 'stop words' file
    stop_words_file_list = stop_words_file.readlines()  # Read the lines from the file
    for stop_word in stop_words_file_list:  # for all the stop words
        index = stop_words_file_list.index(stop_word)  # get the stop word index
        stop_word = stop_word.strip()  # delete '\n'
        stop_words_file_list[index] = stop_word  # Replace the word with the manipulated one: 'a\n' -> 'a'

    print("Stop words")
    print(stop_words_file_list)
    print(len(stop_words_file_list))

    # for all the songs in the file
    for i in range(0, 10):
        #           get the song by index // strip in from '\n' // make it a lower case // split it to array
        listTitle = songs_from_file[i].strip().lower().split()
        runtime = listTitle[-1]  # The song runtime
        listTitle = listTitle[:-1]  # Delete the runtime
        st = str(i) + " " + " ".join(listTitle)  # the final string I need to search the .txt file in my folder

        try:
            song_parser_start_time = datetime.now()
            temp_song = open(st + '.txt', 'r')  # Capture all the downloaded songs
            temp_song_lyrics = (temp_song.readlines())  # Reads all the lines from the file
            temp_song_lyrics_manipulated = []  # new list that will contain all the sentences without '\n
            for sentence in temp_song_lyrics:
                temp_song_lyrics_manipulated.append(sentence.strip())

            # After I lost '\n', I can join all the sentences together and split the string to words
            # Make all the words lower case
            # Now it's not the right time to delete special chars because I want to delete the stop words
            temp_song_lyrics_manipulated = " ".join(temp_song_lyrics_manipulated).lower().split()
            print(st)
            print(temp_song_lyrics_manipulated)
            print(len(temp_song_lyrics_manipulated))

            # Delete all the stop words from the current song i'm working on which is - temp_song_lyrics_manipulated
            list_of_words_without_stopwords = []
            for lyric_word in temp_song_lyrics_manipulated:
                if lyric_word not in stop_words_file_list:
                    list_of_words_without_stopwords.append(lyric_word)
                # if lyric_word in stop_words_file_list:
                # temp_song_lyrics_manipulated.remove(lyric_word)

            print("The song lyrics after deleting the stop words")
            print(list_of_words_without_stopwords)
            print(len(list_of_words_without_stopwords))

            #  Now delete all the punctuations
            list_of_words_without_stopwords = " ".join(list_of_words_without_stopwords)
            list_of_words_without_stopwords = remove_special_chars(list_of_words_without_stopwords).split()

            #  Now delete all the punctuations
            # temp_song_lyrics_manipulated = " ".join(temp_song_lyrics_manipulated)
            # temp_song_lyrics_manipulated = remove_special_chars(temp_song_lyrics_manipulated).split()
            print(temp_song_lyrics_manipulated)
            song_parser_end_time = datetime.now()
            print(song_parser_end_time - song_parser_start_time)
            #                       0  + 0 smooth santana lyrics
            final_lyrics = open(str(i) + st + '.txt', 'w')
            # final_lyrics.write("\n".join(temp_song_lyrics_manipulated))
            final_lyrics.write("\n".join(list_of_words_without_stopwords))

        except:  # If I didn't found the file - print that it's not found
            print(st, "File not found")


run_parser()
