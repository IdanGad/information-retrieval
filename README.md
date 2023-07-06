# information-retrieval
Songs lyrics search engine

Program purpose is to build a search engine where a user can write a string and recive the most relavent songs to it.

files explanation:
Crawler first - donwloads a list of 10000 songs name from the web. 

Crawler second - goes through each song name from "crawler first" and downloads its lyrics. Saves each song's lyrics in a text file.

Parser - splits all the lyrics to individuals words, deletes all the stop words, adds a index number and eventually cleans each word.

Stemmer - make each word to its root. "dancing" to "dance", "talking" to "talk" and more. it uses WordNetLemmatizer library.

Indexer - builds a words dictionary. deletes duplicates, checks frequency, and saves each word as key:value pair. list a = [[song 1, x1 times],...[song y, x2 times]]
ranker - builds a dictionary of top song to the user. gets a string from the user, gives each word wight, calculates TF and DF values to the word, and find the cosine similarity.





