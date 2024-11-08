import requests
from urllib.request import urlopen
import urllib.error
import json
import random


#Download
#
#uri = "https://api.jikan.moe/v4/anime/5/characters"



#uri = "https://api.jikan.moe/v4/anime/1/episodes"
#uri = "https://api.jikan.moe/v4/anime/{id}/episodes/{episode}"
#uri = "https://api.jikan.moe/v4/anime/1/news"
#uri = "https://api.jikan.moe/v4/anime/25/videos"


#uri = "https://api.jikan.moe/v4/anime/1/videos/episodes"
#uri = "https://api.jikan.moe/v4/anime/1/recommendations"

#uri = "https://api.jikan.moe/v4/characters"
#uri = "https://api.jikan.moe/v4/random/anime"
#uri = "https://api.jikan.moe/v4/genres/anime"
#uri = "https://api.jikan.moe/v4/clubs"

#uri = "https://api.jikan.moe/v4/users"
#uri = "https://api.jikan.moe/v4/recommendations/anime"
#uri = "https://api.jikan.moe/v4/random/characters"

#uri = "https://api.jikan.moe/v4/top/characters"
#uri = "https://api.jikan.moe/v4/top/anime"
#uri = "https://api.jikan.moe/v4/seasons/{2024}/{2}"

#uri = "https://api.jikan.moe/v4/watch/episodes/popular"
#uri = "https://api.jikan.moe/v4/watch/episodes"
#uri = "https://api.jikan.moe/v4/seasons"

#headers = {'X-Auth-Token' : '670f6be254e148088731f9822e295607', 'Accept-Encoding': '' }


#number = random.randint(1, 1000)
#uri = f"https://api.jikan.moe/v4/anime/{number}/full

#uri = "https://api.jikan.moe/v4/anime/1/full"


#uri = "https://api.jikan.moe/v4/anime/1/pictures"

#uri = "https://api.jikan.moe/v4/anime/1"

uri = "https://api.jikan.moe/v4/anime"
uris = "https://api.jikan.moe/v4/recommendations/anime"

#uri = "https://api.jikan.moe/v4/top/anime"
            
response = requests.get(uri)
animes = response.json()

response1 = requests.get(uris)
animes1 = response1.json()

#print(animes[])
length = len(animes["data"])
#print(length)
anime_list = []
for x in range(length):
    anime = animes["data"][x]["titles"][0]["title"]
    anime_list.append(anime)


length1 = len(animes1["data"])
#print(length
#anime_list = []
for x in range(length1):
    anime = animes1["data"][x]['entry'][0]['title']#["title"]
    #print(anime)
    anime_list.append(anime)


print(anime_list)
#print(animes["data"]["titles"][0]["title"])

'''title = animes["data"]["titles"][0]["title"]
new = title.lower()
newest=new.replace(" ", "-")
print(newest)'''

'''about = animes["data"]["about"]
name = animes["data"]["name"]
image = animes["data"]["images"]["jpg"]["image_url"]'''

'''episode_list = []
episode_title_list = []
title_list = []
image_list = []
uri_list = []


length = len(animes["data"])
for x in range(length):
    episode_title = animes["data"][x]["episodes"][0]["title"]
    episode = animes["data"][x]["episodes"][0]["url"]
    title = animes["data"][x]["entry"]["title"]
    image = animes["data"][x]["entry"]["images"]["jpg"]["large_image_url"]
    uri = animes["data"][x]["entry"]["url"]
    
    episode_list.append(episode)
    episode_title_list.append(episode_title)
    title_list.append(title)
    image_list.append(image)
    uri_list.append(uri)


print(uri_list)'''

'''#demographics = animes["data"]["demographics"][0]["name"]
studio = animes["data"]["studios"][0]["name"]
#licensors = animes["data"]["licensors"][0]["name"]
producers = animes["data"]["producers"][0]["name"]
synopsis = animes["data"]["synopsis"]
rating = animes["data"]["rating"]
score = animes["data"]["score"]

aired = animes["data"]["aired"]["string"]
episodes = animes["data"]["episodes"]

title = animes["data"]["titles"]
for x in title:
    type = x["type"]
    if type == "English":
        titles = x['title']

image_trailer = animes["data"]["images"]["jpg"]["image_url"]
trailer = animes["data"]["trailer"]["url"]           
image = animes["data"]["images"]["jpg"]["large_image_url"]

print(image)
print(trailer)
print(episodes)
print(producers)
'''

#Image lists and shit
'''image_list = []
name_list = []
length = len(animes["data"])
for a in range(length):
    image = animes["data"][a]["entry"]["images"]["webp"]["large_image_url"]
    name = animes["data"][a]["entry"]["title"]
    image_list.append(image)
    name_list.append(name)

print(image_list)
print(name_list)'''


'''uri3 = "https://api.jikan.moe/v4/top/characters"
    
response3 = requests.get(uri3)
animes3 = response3.json()   
    
image_list3 = []
name_list3 = []
length3 = len(animes3["data"])'''

#Top Anime URL
#uri = "https://api.jikan.moe/v4/top/anime"



#Anime URL
uri = "https://api.jikan.moe/v4/anime"
            
response = requests.get(uri)
animes = response.json()
            
#Image lists and shit
image_list = []
title_list = []
id_list = []
length = len(animes["data"])
for a in range(length):
    image = animes["data"][a]["images"]["jpg"]["large_image_url"]
    id = animes["data"][a]["mal_id"]
                
    #Titles in English
    title = animes["data"][a]["titles"]
    for x in title:
        type = x["type"]
        if type == "English":
            titles = x['title']
            title_list.append(titles)
                
            image_list.append(image)
            id_list.append(id)
                
            
#Get the length
lengths = len(image_list)
def swap():
    #lst = [1, 2, 3, 4, 5]
    [image_list[-1]] + image_list[:-1]

'''    temp = image_list[0]#441
    image_list[0] = image_list[-1]#491
    image_list[-1] = temp
    
    temp1 = title_list[0]#441
    title_list[0] = title_list[-1]#491
    title_list[-1] = temp1
    
    temp2 = id_list[0]#441
    id_list[0] = id_list[-1]#491
    id_list[-1] = temp2
    
swap()'''
#swap()
new_image_list = [image_list[-1]] + image_list[:-1]
new_title_list = [title_list[-1]] + title_list[:-1]
new_id_list = [id_list[-1]] + id_list[:-1]



# Shuffle two lists with same order
# Using zip() + * operator + shuffle()
temp = list(zip(new_image_list, new_title_list, new_id_list))
#print(temp)
#random.shuffle(temp)
#res1, res2, res3 = zip(*temp)
# res1 and res2 come out as tuples, and so must be converted to lists.
#res1, res2, res3 = list(res1), list(res2), list(res3)
 
# Printing result
#print(f"List 1 after shuffle :  {res1}")
#print(f"List 2 after shuffle :  {res2}")
#print(f"List 2 after shuffle :  {res3}")

#print(new)

#Random Character
#uri = "https://api.jikan.moe/v4/top/characters"
#uri = "https://api.jikan.moe/v4/genres/anime"
#uri = "https://api.jikan.moe/v4/anime/1/news"
uri = "https://api.jikan.moe/v4/characters"
#uri = "https://api.jikan.moe/v4/anime/5/characters"
            
response = requests.get(uri)
animes = response.json()

#print(animes["data"])

'''print(animes["data"][0]["images"]["jpg"]["image_url"])
print(animes["data"][0]["name"])
print(animes["data"][0]["nicknames"])
#print(animes["data"][0]["about"])
print(animes["data"][2])'''
