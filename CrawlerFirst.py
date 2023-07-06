# Phase 1
# The purpuse of this file is to open Chrome browser and get a list of 10000 songs names in order to
# build a data base.
# Note that the songs names from the website need to be organized and changed before continuing to the phase 2.


# google chrome version 112.0.5615.138

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# give access to keys and manipulate them
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('chromedriver.exe')  # Define the web browser that I want to use
driver.get("http://top10000songs.blogspot.com/")  # Open the website that I wanted

#  Try-Finally block in case something happen
try:

    # Wait 20 sec until the element is found because maybe the element is not loaded yet
    # After max 20 sec' find the element that its ID is 'main' - it's all the songs names
    print("Getting songs names")
    main = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "main"))
    )

    # Every song is listed in different line, so enter all the song names to a list, every song to different index
    songs_names = main.text.split("\n")

    # The website has more than songs names so delete all the strings that are not songs names
    songs_names = songs_names[5:-3]  # Lose the unneeded Strings

    new_list = []  # This is a list to save all the songs names - the song name from the website may have extra strings
    newManipulatedString = ""  # String to save the song name without the extra chars from the website
    test = []  # I'll use this list to split the String from the website, then delete the number from the first index
    finalstr = ""  # The string to append to the new song list
    seperator = " "  # Seperator to join the string without the number and the '::'
    for song in songs_names:  # for all the Strings that we got from the website
        #  start manipulation
        newManipulatedString = song.replace("::", "")  # Deleting the '::' from the website's Sting
        test = newManipulatedString.split()  # Splitting to delete the number at the beginning of the string
        test = test[1:]  # Delete the first index
        finalstr = seperator.join(test) + " Lyrics"  # Join the String back and add 'Lyrics' for the Google search
        new_list.append(finalstr)  # Add the manipulated String to the new list
        newManipulatedString = ""  # Reset for next word
        finalstr = ""  # Reset for next word
        seperator = " "  # Reset for next word

    toJoin = "\n"  # String to join the lines back
    songsString = toJoin.join(new_list)  # final lyrics

    # Test to see that I got all the songs
    # print(songs_names[0])
    # print(songs_names[-1])
    print("If U got here, U got all songs names to a list.")

    f = open("songsNames.txt", "w", encoding="utf-8")
    f.write(songsString)  # Make the songsNames string a file

finally:  # Quit the first browser
    driver.quit()