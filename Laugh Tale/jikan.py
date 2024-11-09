from jikanpy import Jikan
jikan = Jikan()

mushishi = jikan.anime(457)
mushishi_with_eps = jikan.anime(457, extension='episodes')

search_result = jikan.search('anime', 'Mushishi', page=2)

winter_2018_anime = jikan.seasons(year=2018, season='winter')

current_season = jikan.seasons(extension='now')