from bs4 import BeautifulSoup
import requests

print("WELCOME TO MY GENIUS LYRICS FETCHER")
print()

print("Enter the artist's name. Caps does not matter")
inputName = input()


print("Enter name of song by artist. Song must be exactly same as on Album or Single release. Caps does not matter")
inputSong = input()


for i in range(len(inputName)):
    if (inputName[i] == ' '):
        inputName = inputName.replace(inputName[i], '-')


for i in range(len(inputSong)):
    if (inputSong[i] == ' '):
        inputSong = inputSong.replace(inputSong[i], '-')


#my_url = 'https://genius.com/Travis-scott-sicko-mode-lyrics'
my_url = 'https://genius.com/' + inputName + '-' + inputSong + '-lyrics'

page = requests.get(my_url).text

soup = BeautifulSoup(page , 'lxml')

lyrics = soup.find('div', class_= "song_body-lyrics")

print(lyrics.text)

input()



    
    





    


















