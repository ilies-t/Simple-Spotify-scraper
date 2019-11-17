from selenium import webdriver
from collections import Counter
from json import dump

# open selenium & file
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(options=chrome_options)
fp = open("result.json", "w")
playlist_wanted = [
    "37i9dQZF1DX2A29LI7xHn1?si=qT3X5wUCRDCXEhpJyg2_Mw",
    "37i9dQZF1DX7Ku6cgJPhh5?si=HCwok0iiTvykUVQlCXjjcg",
    "37i9dQZF1DXcBWIGoYBM5M?si=GqVK28qqQ2WQ4tB2060Ldg"
    ]

def scrape_playlist(playlist_array):
    # count_artist is the list with all of playlist
    count_artist = []

    # start loop for all playlist in playlist_wanted
    for p in playlist_array:
        # open driver and create artist list
        driver.get("https://open.spotify.com/playlist/"+p)
        artist_list = []

        # parse HTML content with Xpath
        artist_value = driver.find_elements_by_xpath('//a[@class="tracklist-row__artist-name-link"]')
        for artist in artist_value:
            artist = artist.get_attribute('innerHTML')
            artist_list.append(artist)
        playlist_name = driver.find_element_by_xpath('//div[@class="TrackListHeader__entity-name"]/h2/span').get_attribute('innerHTML')

        # count result and write on file
        p_result = {playlist_name: Counter(artist_list)}
        count_artist.append(p_result)

    c = dump(count_artist, sort_keys=True, indent=4, fp=fp)
    fp.close()
    driver.quit()

# scrape and see result !
scrape_playlist(playlist_wanted)

# finish
print("finish :)")