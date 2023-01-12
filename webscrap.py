import requests
from lxml import html
from mlist import Mlist

url = "https://www.imdb.com/name/nm0000375/?ref_=nv_sr_1?ref_=nv_sr_1"

print ("web scrapping started")

text = requests.get(url).text
tree = html.fromstring(text)

list_title = tree.xpath("//*[@class='filmo-row even']/b//text()")
#print(list_title)

def rating(t1):
    movie,links = t1          # ('Iron Man Three', ['https://www.imdb.com/title/tt1300854/'])
    link = links[0]
    #print ("web scrapping started")
    text = requests.get(link).text
    tree = html.fromstring(text)
    rating = tree.xpath('//span[@class="sc-7ab21ed2-1 jGRxWM"]//text()')
    print (movie,rating)


list_url = []
for each in list_title:
    try:
        url = Mlist(tree.xpath("//a[text()= '%s']/@href" %each))   # link& %s-->'Avengers: Infinity War'
        url.dupr()                                                 # remove duplicate element
        t1 = (each,["https://www.imdb.com" + each for each in url])
        print (t1)
        rating(t1)
        
    except Exception as e:
        print(e)