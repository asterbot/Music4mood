import requests
import text2emotion as te

SPOTIFY_GET_RECOMMENDATIONS_URL = "https://api.spotify.com/v1/recommendations"
ACCESS_TOKEN = "BQAGt89rA_fiyOWgJHCV6RWyP2xUPgjAIidnmZPL_h-aY5tt1qKQlDInYARQgUUYijaeSQ6nNteBxPrR1InPSfejbPDQdt2RN2-rrIv-RomAvKBLj6kEZntmhR6q8oSInnpqzJMnQpUACVyNikhWvZFPOBPEuWTeBMFwUutsoAxb--7jSlBzRESbQYUNQs0"

def get_recommendations_on_spotify(seed_artists,seed_genres,seed_tracks,limit,max_tempo,min_tempo,max_valence,min_valence,max_energy,min_energy,max_danceability,min_danceability,max_liveness,min_liveness,max_loudness,min_loudness):
    response=requests.get(
        SPOTIFY_GET_RECOMMENDATIONS_URL,
        headers={
            "Authorization": f"Bearer {ACCESS_TOKEN}"
        },
        params={
            "seed_artists": seed_artists,
            "seed_genres": seed_genres,
            "seed_tracks": seed_tracks,
            "limit": limit,
            "max_tempo": max_tempo,
            "min_tempo": min_tempo,
            "max_valence": max_valence,
            "min_valence": min_valence,
            "max_energy": max_energy,
            "min_energy": min_energy,
            "max_danceability": max_danceability,
            "min_danceability": min_danceability,
            "max_liveness": max_liveness,
            "min_liveness": min_liveness,
            "max_loudness": max_loudness,
            "min_loudness": min_loudness
        }
    )
    
    return response.json()

def main():
    artists = "4UXqAaa6dQYAk18Lv7PEgX"
    genres = "pop,country,classical"
    tracks = "0c6xIDDpzE81m2q797ordA"
    s=input("Enter your mood: ")
    #print(te.get_emotion(s))
    n=int(input("How many songs?"))
    emotions_value=te.get_emotion(s)
    max_tempo=min(emotions_value['Fear']+0.2,1)*2000
    min_tempo=max(emotions_value['Fear']-0.2,0)*2000
    max_valence=min(emotions_value['Happy']+0.2,1)
    min_valence=max(emotions_value['Happy']-0.2,0)
    max_energy=min(max(emotions_value['Happy'],1-emotions_value['Sad'])+0.2,1)
    min_energy=max(min(emotions_value['Happy'],1-emotions_value['Sad'])-0.2,0)
    max_danceability=min(1, emotions_value['Happy']+0.2)
    min_danceability=max(0,emotions_value['Happy']-0.2)
    max_liveness=min(1, emotions_value['Happy']+0.2)
    min_liveness=max(0,emotions_value['Happy']-0.2)
    max_loudness=min(1, (emotions_value['Surprise']+emotions_value['Angry'])/2+0.2)
    min_loudness=max(0,(emotions_value['Surprise']+emotions_value['Angry'])/2-0.2)

    recommendations = get_recommendations_on_spotify(seed_artists=artists,seed_genres=genres,seed_tracks=tracks,limit=n,max_tempo=max_tempo,min_tempo=min_tempo,max_valence=max_valence,min_valence=min_valence,max_energy=max_energy,min_energy=min_energy,max_danceability=max_danceability,min_danceability=min_danceability,max_liveness=max_liveness,min_liveness=min_liveness,max_loudness=max_loudness,min_loudness=min_loudness)
    print(f"Recommendations: {recommendations}")
    for i in recommendations['tracks']:
        print(i['name'],"by",i['artists'][0]['name'])

if __name__ == '__main__':
    main()
