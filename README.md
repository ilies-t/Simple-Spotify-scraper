# Simple Spotify scraper  
Return the name of a playlist and the number of times an artist is present in a playlist to "result.json".  
  
## Prerequisites  
#### Selenium  
```shell
pip install selenium
```  
#### Chrome webdriver  
* [Chromedriver](https://chromedriver.storage.googleapis.com/index.html?path=78.0.3904.70/) - Works with v.78.0.3904.70
  
## Usage  
**Put all your playlist id in a list even you have only one playlist** :
```python
playlist_wanted = ["37i9dQZF1DX2A29LI7xHn1?si=qT3X5wUCRDCXEhpJyg2_Mw"]
scrape_playlist(playlist_wanted)
```  
## License
[Apache License 2.0](https://choosealicense.com/licenses/apache-2.0/)