# Phase 2
# The purpose of this script is to get the lyrics of all the songs the I got from phase 1.
# The program will read the txt file with all the songs names then search the name in Google, fetch the lyrics and
# then save it to a file.
# After running this program the 10000 songs lyrics DB will be complete

from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# give access to keys and manipulate them
from selenium.webdriver.common.keys import Keys


# This method will remove any unwanted chars from a string. It will prevent problems in saving a file using its name
def remove_special_chars(word):
    answer = ""
    for char in str(word):
        if char.isalnum() or char.isspace():
            answer += char

    return answer


# driver = webdriver.Chrome('chromedriver.exe')  # Define the web browser that I want to use
# driver.get("http://top10000songs.blogspot.com/")  # Open the website that I wanted

total_program_start_time = datetime.now()

file = open('songsNames.txt', 'r')  # Open the file that has all the songs names that I got from CrawlerTwoPointO
songs_from_file = file.readlines()  # Reads all the lines from the file

new_songs_list = []  # New list to remove the "\n" from the end of each string
for song in songs_from_file:  # Removing the "\n" from all the Strings except the last one
    new_songs_list.append(song.strip())

# new_songs_list[8] = "Linkin park crawling lyrics"

# print(songs_from_file[0])
# print(new_songs_list[0])

# Appending songs to 'test_songs' list
# I need to do it because it would take roughly 28 hours to fetch 10,000 songs lyrics
# Every song runtime is 10 seconds
# 100 songs = 17 minutes
# 1000 songs = 2:46 hours

# The following loop will help me devide 28 hours to smaller chunks
# Control the loop! 0-20, 20-100, 100-200, 200-300....
# UPDATE THE INDEX!!!!!!
test_Songs = []
for i in range(0, 5000):
    test_Songs.append(new_songs_list[i])

fileToSaveTheRuntimeForEverySong = open("songsRunTimeFetch.txt", "w", encoding="utf-8")

# new_list = []
# This loop will iterate over all the String and do the following:
# 1. Open Google
# 2. Search the string at Google site. for example: Red hot chili peppers other side lyrics
# 3. Get the lyrics from the site
# 4. Save the lyrics to a .txt file
i = 0  # index for the songs number
for song in test_Songs:  # Get only the first song until the algorithm is verified with avigail

    iteration_start_time = datetime.now()  # The time that the iteration started
    # This 'options' 3 next lines preventing the browser to actually open in every iteration
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('disable-gpu')

    driver2 = webdriver.Chrome('chromedriver.exe', options=options)  # Define the web browser that I want to use
    driver2.get("http://www.google.com/")  # Open google
    search = driver2.find_element_by_name("q")  # find the "Search" element in Google
    search.send_keys(song)  # Type the song name at Chrome
    search.send_keys(Keys.RETURN)  # Hit Enter

    try:
        # Start searching lyrics
        # Wait 15 seconds until the lyrics appears
        songLyrics = WebDriverWait(driver2, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, "sATSHe"))
        )

        lyrics_man = songLyrics.text.split("\n")  # Get the lyrics and split them by line to a list to delete unneeded-
        # Strings
        lyrics_man = lyrics_man[1:-4]  # Lose the unneeded Strings
        toJoin = "\n"  # String to join the lines back
        final_ly = toJoin.join(lyrics_man)  # final lyrics

        # Test to see that the lyrics are good
        # print(final_ly)

        # Remove any special chars from the string for saving the file.
        song = remove_special_chars(song)

        # Save the lyrics to a file
        f = open(str(i) + " " + song + ".txt", "w", encoding="utf-8")
        f.write(final_ly)

        iteration_end_time = datetime.now()  # The time that the iteration ended
        total_iteration_time = iteration_end_time - iteration_start_time  # Total time took to fetch the song lyrics

        fileToSaveTheRuntimeForEverySong.write(song + " " + str(total_iteration_time) + "\n")  # Save the song runtime

        print(i, song, total_iteration_time)  # Song name
        i = i + 1  # Song's counter
        driver2.quit()  # Quit the browser

    except:
        # If there was a problem finding the song's lyrics
        print(song + " NOT FOUND")
        driver2.quit()  # Quit the browser


total_program_end_time = datetime.now()  # The time it took to fetch all the song

print()
print("Total run time is:", total_program_end_time - total_program_start_time)
