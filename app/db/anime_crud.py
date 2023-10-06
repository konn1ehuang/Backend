from ..db import db_client 
from ..anime_schema import Anime

table = db_client.client.table("anime") 

def get_anime(aid:int):
    return table.select("1").eq("aid", aid).execute()

def post_anime(anime:Anime):
    return table.upsert({
        "anime_id": anime.anime_id, 
        "anime_name": anime.anime_name, 
        "score": anime.score,
        "genres": anime.genres,
        "type": anime.type
        }).execute()
        



