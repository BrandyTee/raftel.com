from flask import Flask, render_template, flash, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from werkzeug.security import generate_password_hash, check_password_hash
import requests
from urllib.request import urlopen
import urllib.error
import json
import random


app = Flask(__name__)
#Add Database 
#Secret Key
app.config['SECRET_KEY'] = "I will become king of the pirates"


#Create Search Form 
class SearchForm(FlaskForm):
    searched = StringField(" Searched ", validators=[DataRequired()])
    submit = SubmitField("Submit")



#Create Game Form 
class GameForm(FlaskForm):
    name = StringField(" Name ", validators=[DataRequired()])
    submit = SubmitField("Submit")
    
    

@app.route("/search", methods=['GET', 'POST'])
def search():
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
    
    return render_template("raftel base.html", anime_list=anime_list)



#Home Page
@app.route("/", methods=['GET', 'POST'])
def raftel_home():
    try:
        
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
                
            
                
        
        #Top Anime URL
        uri1 = "https://api.jikan.moe/v4/top/anime"
            
        response1 = requests.get(uri1)
        animes1 = response1.json()
            
        #Image lists and shit
        image_list1 = []
        title_list1 = []
        id_list1 = []
        length = len(animes1["data"])
        for a in range(length):
            image = animes1["data"][a]["images"]["jpg"]["large_image_url"]
            id = animes1["data"][a]["mal_id"]
                
            #Titles in English
            title = animes1["data"][a]["titles"]
            for x in title:
                type = x["type"]
                if type == "English":
                    titles = x['title']
                    title_list1.append(titles)
                
                    image_list1.append(image)
                    id_list.append(id)
                
            
        #Get the length
        lengths1 = len(image_list1)
        
        #Merge lists 
        images = image_list + image_list1
        titles = title_list + title_list1
        ids = id_list + id_list1
        
        #Combine And Shuffle 
        temp = list(zip(images, titles, ids))
        random.shuffle(temp)
        images1, titles1, ids1 = zip(*temp)
        # res1 and res2 come out as tuples, and so must be converted to lists.
        images1, titles1, ids1 = list(images1), list(titles1), list(ids1)
         
        #Get the length
        lengths = len(images)
            
        
        
        #Anime Recommendations    
        uri_recommendations = "https://api.jikan.moe/v4/recommendations/anime"
            
        response_recommendations = requests.get(uri_recommendations)
        animes2 = response_recommendations.json()
            
        image_list2 = []
        title_list2 = []
        length2 = len(animes["data"])
        for x in range(length2):
            for y in range(0, 2):
                title2 = animes2["data"][x]["entry"][y]["title"]
                image2 = animes2["data"][x]["entry"][y]["images"]["webp"]["large_image_url"]
                image_list2.append(image2)
                title_list2.append(title2)
            
        #random.shuffle(image_list2)
        #random.shuffle(title_list2)
            
        image_recommendations = image_list2
        title_recommendations = title_list2
            
        lengths2 = len(image_recommendations)
            
            
        
        #Get the characters
        uri3 = "https://api.jikan.moe/v4/top/characters"
            
        response3 = requests.get(uri3)
        animes3 = response3.json()
            
            
        image_list3 = []
        name_list3 = []
        id_list3 = []
        length3 = len(animes3["data"])
        for a in range(length3):
            image = animes3["data"][a]["images"]["jpg"]["image_url"]
            name = animes3["data"][a]["name"]
            id = animes3["data"][a]["mal_id"]
            image_list3.append(image)
            name_list3.append(name)
            id_list3.append(id)
            
        #print(image_list)
        #print(name_list)
        lengths3 = len(image_list3)
            
            
            
        #Popular Episodes 
        uri4 = "https://api.jikan.moe/v4/watch/episodes"
            
        response4 = requests.get(uri4)
        animes4 = response4.json()
            
            
        #Image lists and shit
        image_list4 = []
        name_list4 = []
        length4 = len(animes4["data"])
        for a in range(length4):
            image = animes4["data"][a]["entry"]["images"]["webp"]["large_image_url"]
            name = animes4["data"][a]["entry"]["title"]
            image_list4.append(image)
            name_list4.append(name)
                
            lengths4 = len(image_list4)
        
            
            
        #Watch episodes
        uri = "https://api.jikan.moe/v4/watch/episodes/popular"
            
        response = requests.get(uri)
        animes = response.json()
            
        #print(animes["data"][0])
            
        episode_list = []
        episode_title_list = []
        title_list5= []
        image_list5 = []
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
            title_list5.append(title)
            image_list5.append(image)
            uri_list.append(uri)
            
            
        #print(uri_list)
        lengths5 = len(uri_list)
            
            
            
        #Random Character
        uri = "https://api.jikan.moe/v4/random/characters"
            
        response = requests.get(uri)
        animes = response.json()
            
        #print(animes["data"])
            
        about = animes["data"]["about"]
        name = animes["data"]["name"]
        image = animes["data"]["images"]["jpg"]["image_url"]
        small_image = animes["data"]["images"]["webp"]["small_image_url"]
        nickname = animes["data"]["nicknames"]
                    
            
        return render_template("raftel_home.html",
            images1=images1, 
            titles1=titles1, 
            lengths=lengths, 
            ids1=ids1,
            
            image_list1=image_list1, 
            title_list1=title_list1, 
            lengths1=lengths1, 
            id_list1=id_list1,
                
            lengths2=lengths2,
            image_recommendations=image_recommendations,
            title_recommendations=title_recommendations,
                
            image_list3=image_list3, 
            name_list3=name_list3, 
            lengths3=lengths3,
            id_list3=id_list3,
                
            image_list4=image_list4, 
            name_list4=name_list4, 
            lengths4=lengths4,
                
            uri_list=uri_list,
            episode_list = episode_list,
            episode_title_list = episode_title_list,
            title_list5 = title_list5,
            image_list5 = image_list5,
            lengths5=lengths5,
                
            about=about,
            name=name,
            image=image,
            small_image=small_image,
            nickname=nickname,
                
            )
    except:
        oops = "Oops, there is something wrong. Please try again!!!"
        return render_template("error.html", oops=oops)



#Anime Today
@app.route("/anime_today", methods=['GET', 'POST'])
def anime_today():
    number = random.randint(1, 1000)
    try:
        uri = f"https://api.jikan.moe/v4/anime/{number}/full"
                        
        response = requests.get(uri)
        animes = response.json()
            
        #print(animes["data"])
            
        #demographics = animes["data"]["demographics"][0]["name"]
        studio = animes["data"]["studios"][0]["name"]
        #licensors = animes["data"]["licensors"][0]["name"]
        producers = animes["data"]["producers"][0]["name"]
        synopsis = animes["data"]["synopsis"]
        rating = animes["data"]["rating"]
        ratings1 = rating.split(' ')
        ratings = ratings1[0]
        score = animes["data"]["score"]
            
        aired = animes["data"]["aired"]["string"]
        episodes = animes["data"]["episodes"]
        title = animes["data"]["titles"][0]["title"]
            
        title = animes["data"]["titles"]
        title_list = []
        for x in title:
            type = x["type"]
            if type == "English":
                titles = x['title']
                title_list.append(titles)
            
        image_trailer = animes["data"]["images"]["jpg"]["image_url"]
        trailer = animes["data"]["trailer"]["url"]           
        image = animes["data"]["images"]["jpg"]["large_image_url"]
        
        
        #Recommendations
        uri_recommendations = "https://api.jikan.moe/v4/recommendations/anime"
        
        response_recommendations = requests.get(uri_recommendations)
        animes2 = response_recommendations.json()
        
        image_list2 = []
        title_list2 = []
        length2 = len(animes["data"])
        for x in range(length2):
            for y in range(0, 2):
                title2 = animes2["data"][x]["entry"][y]["title"]
                image2 = animes2["data"][x]["entry"][y]["images"]["webp"]["large_image_url"]
                image_list2.append(image2)
                title_list2.append(title2)
        
        #random.shuffle(image_list2)
        #random.shuffle(title_list2)
        
        image_recommendations = image_list2
        title_recommendations = title_list2
        
        lengths2 = len(image_recommendations)
        
        
        return render_template("anime_today.html", 
                image=image,
                image_trailer=image_trailer,
                trailer=trailer,
                titles=titles,
                title_list=title_list,
                episodes=episodes,
                aired=aired,
                score=score,
                ratings=ratings,
                synopsis=synopsis,
                studio=studio,
                #producers=producers
                
                lengths2=lengths2,
                image_recommendations=image_recommendations,
                title_recommendations=title_recommendations,
                )
    except:
        oops = "Oops, there is something wrong. Please try again!!!"
        return render_template("error.html", oops=oops)



#Anime Full
@app.route("/anime_full<chosen_anime>", methods=['GET', 'POST'])
def anime_full(chosen_anime):
    number = random.randint(1, 1000)
    try:
        uri = f"https://api.jikan.moe/v4/anime/{chosen_anime}/full"
                        
        response = requests.get(uri)
        animes = response.json()
            
        #print(animes["data"])
            
        #demographics = animes["data"]["demographics"][0]["name"]
        studio = animes["data"]["studios"][0]["name"]
        #licensors = animes["data"]["licensors"][0]["name"]
        producers = animes["data"]["producers"][0]["name"]
        synopsis = animes["data"]["synopsis"]
        rating = animes["data"]["rating"]
        ratings1 = rating.split(' ')
        ratings = ratings1[0]
        score = animes["data"]["score"]
            
        aired = animes["data"]["aired"]["string"]
        episodes = animes["data"]["episodes"]
        title = animes["data"]["titles"][0]["title"]
            
        title = animes["data"]["titles"]
        title_list = []
        for x in title:
            type = x["type"]
            if type == "English":
                titles = x['title']
                title_list.append(titles)
            
        image_trailer = animes["data"]["images"]["jpg"]["image_url"]
        trailer = animes["data"]["trailer"]["url"]           
        image = animes["data"]["images"]["jpg"]["large_image_url"]
        
        
        #Recommendations
        uri_recommendations = "https://api.jikan.moe/v4/recommendations/anime"
        
        response_recommendations = requests.get(uri_recommendations)
        animes2 = response_recommendations.json()
        
        image_list2 = []
        title_list2 = []
        length2 = len(animes["data"])
        for x in range(length2):
            for y in range(0, 2):
                title2 = animes2["data"][x]["entry"][y]["title"]
                image2 = animes2["data"][x]["entry"][y]["images"]["webp"]["large_image_url"]
                image_list2.append(image2)
                title_list2.append(title2)
        
        #random.shuffle(image_list2)
        #random.shuffle(title_list2)
        
        image_recommendations = image_list2
        title_recommendations = title_list2
        
        lengths2 = len(image_recommendations)
        
        
        return render_template("anime_full.html", 
                image=image,
                image_trailer=image_trailer,
                trailer=trailer,
                titles=titles,
                title_list=title_list,
                episodes=episodes,
                aired=aired,
                score=score,
                ratings=ratings,
                synopsis=synopsis,
                studio=studio,
                #producers=producers
                
                lengths2=lengths2,
                image_recommendations=image_recommendations,
                title_recommendations=title_recommendations,
                )
    except:
        oops = "Oops, there is something wrong. Please try again!!!"
        return render_template("error.html", oops=oops)



#Guessing In Anime
@app.route("/top_anime", methods=['GET', 'POST'])
def top_anime():
    form = GameForm()
    uri = "https://api.jikan.moe/v4/top/anime"
            
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
                #name = titles.split(' ')
                title_list.append(titles)
                image_list.append(image)
                    
        
        id_list.append(id)
                    
                
    #Get the length
    lengths = len(image_list)
    
    #print(image_list)
    #print(title_list)
    
    
    
    #Shuffle and randomize 
    lists = list(zip(image_list, title_list))
    random.shuffle(lists)
    
    images, titles = zip(*lists)
    images, titles = list(images), list(titles)
    
    answers = []
    answer = []
    for x in titles:
        answer.append([x])     
            
        
    length = len(images)
    print(length)
    
    
    
    return render_template("top_anime.html",
        images=images,
        titles=titles,
        length=length,
        )


#top_anime()



#Guessing In Anime
@app.route("/anime_guess", methods=['GET', 'POST'])
def anime_guess():
    form = GameForm()
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
                #name = titles.split(' ')
                title_list.append(titles)
                image_list.append(image)
                    
        
        id_list.append(id)
                    
                
    #Get the length
    lengths = len(image_list)
    
    #print(image_list)
    #print(title_list)
    
    
    
    #Shuffle and randomize 
    lists = list(zip(image_list, title_list))
    random.shuffle(lists)
    
    images, titles = zip(*lists)
    images, titles = list(images), list(titles)
    
    answers = []
    answer = []
    for x in titles:
        answer.append([x])     
            
        
    length = len(images)
    print(length)
    
    
    
    return render_template("anime_guess.html",
        images=images,
        titles=titles,
        length=length,
        #map(json.dumps, titles)
        )




#Guessing Top Characters
@app.route("/top_characters", methods=['GET', 'POST'])
def top_characters():
    form = GameForm()
    uri = "https://api.jikan.moe/v4/characters"
    
            
    response = requests.get(uri)
    animes = response.json()
                
    #Image lists and shit
    image_list = []
    title_list = []
    id_list = []
    length = len(animes["data"])
    for a in range(length):
        image = animes["data"][a]["images"]["jpg"]["image_url"]
        id = animes["data"][a]["mal_id"]
                    
        #Titles in English
        title = animes["data"][a]["name"]
        
        title_list.append(title)
        image_list.append(image)
                    
        
        id_list.append(id)
                    
                
    #Get the length
    lengths = len(image_list)
    
    #print(image_list)
    #print(title_list)
    
    
    
    #Shuffle and randomize 
    lists = list(zip(image_list, title_list))
    random.shuffle(lists)
    
    images, titles = zip(*lists)
    images, titles = list(images), list(titles)
    
    answers = []
    answer = []
    for x in titles:
        answer.append([x])     
            
        
    length = len(images)
    print(images)
    
    
    
    return render_template("top_characters.html",
        images=images,
        titles=titles,
        length=length,
        #map(json.dumps, titles)
        )



#top_characters()



#Guessing Characters
@app.route("/character_guess", methods=['GET', 'POST'])
def character_guess():
    form = GameForm()
    
    #Random Character
    uri = "https://api.jikan.moe/v4/random/characters"
            
    response = requests.get(uri)
    animes = response.json()
            
    #print(animes["data"])
            
    about = animes["data"]["about"]
    name = animes["data"]["name"]
    image = animes["data"]["images"]["jpg"]["image_url"]
    small_image = animes["data"]["images"]["webp"]["small_image_url"]
    nickname = animes["data"]["nicknames"]
    
    return render_template("character_guess.html",
        name=name,
        image=image,
        nickname=nickname,
        )


#Context Processor 
@app.context_processor
def quizzes_base():
    form = SearchForm()
    #towns = cities
    return dict(form=form)


#Quizzes In Anime
@app.route("/quizzes", methods=['GET', 'POST'])
def quizzes():
    return render_template("quizzes.html"
        )





#Characters Page 
@app.route("/character_full<chosen_character>", methods=['GET', 'POST'])
def character_full(chosen_character):
 
        
    uri = "https://api.jikan.moe/v4/top/characters"
                    
    response = requests.get(uri)
    animes = response.json()
    
    image = []
    name = []
    nickname = []
    about = []
        
    for a in range(len(animes["data"])):
        id = animes["data"][a]["mal_id"]
        
        if id == int(chosen_character):
            
            images = animes["data"][a]["images"]["jpg"]["image_url"]
            names = animes["data"][a]["name"]
            nicknames = animes["data"][a]["nicknames"]
            abouts = animes["data"][a]["about"]
            
            image.append(images)
            name.append(names)
            nickname.append(nicknames)
            about.append(abouts)
            
    
    
            
        
        
    #Recommendations
    uri_recommendations = "https://api.jikan.moe/v4/recommendations/anime"
        
    response_recommendations = requests.get(uri_recommendations)
    animes2 = response_recommendations.json()
        
    image_list2 = []
    title_list2 = []
    length2 = len(animes["data"])
    for x in range(length2):
        for y in range(0, 2):
            title2 = animes2["data"][x]["entry"][y]["title"]
            image2 = animes2["data"][x]["entry"][y]["images"]["webp"]["large_image_url"]
            image_list2.append(image2)
            title_list2.append(title2)
        
        
        
    image_recommendations = image_list2
    title_recommendations = title_list2
        
    lengths2 = len(image_recommendations)
    
        
    return render_template("characters.html", 
        lengths2=lengths2,
        image_recommendations=image_recommendations,
        title_recommendations=title_recommendations,
        
        image=image,
        name=name,
        nickname=nickname,
        about=about,
        
        )
    '''except:
        oops = "Oops, there is something wrong. Please try again!!!"
        return render_template("error.html", oops=oops)'''


#character_full(417)



#search()




if __name__ == "__main__":
    app.run("0.0.0.0")