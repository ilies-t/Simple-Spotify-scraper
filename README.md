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
Return one playlist in JSON, **use only the playlist ID** :
```python
scrape_playlist("37i9dQZF1DX7Ku6cgJPhh5?si=HCwok0iiTvykUVQlCXjjcg")
```  
If they are multiple playlist, put "last=True" at the last :  
```python
# last=True
scrape_playlist("37i9dQZF1DX7Ku6cgJPhh5?si=HCwok0iiTvykUVQlCXjjcg", last=True)
```  
## License
[Apache License 2.0](https://choosealicense.com/licenses/apache-2.0/)