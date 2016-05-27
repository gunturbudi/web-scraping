import unirest,urllib

manga_id = 'full-metal-alchemist'
site_id = 'mangareader.net'

start_chapter = 1
end_chapter = 108

manga_url = open(manga_id+"_url.txt","wb")

for chapter in range(start_chapter,end_chapter+1):
  response = unirest.get("https://doodle-manga-scraper.p.mashape.com/"+site_id+"/manga/"+manga_id+"/"+str(chapter),
    headers={
      "X-Mashape-Key": "q4Vnyy9dhxmshgWOBnEl0WDEugFXp1NvCthjsnCbty0PDYJX8p",
      "Accept": "text/plain"
    }
  )

  for k in response.body['pages']:
    manga_url.write(k['url']+"\n")

manga_url.close()

#if you want to directly download the images
#urllib.urlretrieve(k['url'],filename)