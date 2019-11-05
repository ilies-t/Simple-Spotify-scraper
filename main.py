from selenium import webdriver
from time import sleep
from collections import Counter
from json import dumps

# open selenium & file
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(options=chrome_options)
fp = open("result.json", "w")
fp.write("{")
sleep(1)

def scrape_playlist(playlist_id, last=False):
    # open driver and create list
    driver.get("https://open.spotify.com/playlist/"+playlist_id)
    artist_list = []

    # parse HTML content with Xpath
    artist_value = driver.find_elements_by_xpath('//a[@class="tracklist-row__artist-name-link"]')
    for artist in artist_value:
        artist = artist.get_attribute('innerHTML')
        artist_list.append(artist)
    playlist_name = driver.find_element_by_xpath('//div[@class="TrackListHeader__entity-name"]/h2/span').get_attribute('innerHTML')

    # count result and write on file
    count_artist = dumps(Counter(artist_list), sort_keys=True, indent=12)

    # False parameters for JSON
    if last == True:
        fp.write('\n\t"{}":\n\t\t{}\n}}\n'.format(playlist_name ,count_artist))
    elif last == False:
        fp.write('\n\t"{}":\n\t\t{},'.format(playlist_name ,count_artist))

# scrape
scrape_playlist("37i9dQZF1DX7Ku6cgJPhh5?si=HCwok0iiTvykUVQlCXjjcg")
scrape_playlist("37i9dQZF1DWVuV87wUBNwc?si=3cwXbM5MQSauQAVxVeS11g", last=True)

# finish
fp.close()
driver.quit()
print("FINISH")