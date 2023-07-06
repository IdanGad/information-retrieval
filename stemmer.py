# This class will go through every file from the 'parser' and will change every word to its lemmatize form
import nltk

# nltk.download("wordnet") # need to run it only one time

from nltk.stem import WordNetLemmatizer


def run_stemmer():
    lmtz = WordNetLemmatizer()

    #  Get all the songs names and delete the'\n' like always
    songs_names = open('songsRunTimeFetch.txt', 'r')
    songs_names_list = songs_names.readlines()
    songs_names_list_mani = []

    # Remove the runtime from the last index, and save all to a new list
    for song_name in songs_names_list:
        song_name = song_name[:-1]
        song_name_list = song_name.split()
        temp = song_name_list[:-1]
        songs_names_list_mani.append(" ".join(temp))

    for i in range(0, 10):
        try:
            name = str(i) * 2 + " " + songs_names_list_mani[i]
            temp_song = open(name + '.txt', 'r')  # Get the song file -> 00 smooth santana lyrics...
            song_lyrics_list = temp_song.readlines()
            song_lyrics_list_mani = []
            for temp_word in song_lyrics_list:
                song_lyrics_list_mani.append(temp_word.strip())

            # Now 'song_lyrics_list_mani' is ready for lemmatization
            lematize_list = []
            for word in song_lyrics_list_mani:
                word2 = lmtz.lemmatize(word, "v")
                lematize_list.append(word2)

            #  Write to the file the lemmatized words
            final_lyrics = open(str(i) + name + '.txt', 'w')
            final_lyrics.write("\n".join(lematize_list))

        except:
            print("Error found")


def lemm():
    lmtz = WordNetLemmatizer()
    x = lmtz.lemmatize("the", "v")
    print(x)


run_stemmer()
