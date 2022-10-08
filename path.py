import requests
import text2emotion as te

SPOTIFY_GET_RECOMMENDATIONS_URL = "https://api.spotify.com/v1/recommendations"
ACCESS_TOKEN = "BQAGt89rA_fiyOWgJHCV6RWyP2xUPgjAIidnmZPL_h-aY5tt1qKQlDInYARQgUUYijaeSQ6nNteBxPrR1InPSfejbPDQdt2RN2-rrIv-RomAvKBLj6kEZntmhR6q8oSInnpqzJMnQpUACVyNikhWvZFPOBPEuWTeBMFwUutsoAxb--7jSlBzRESbQYUNQs0"

def get_recommendations_on_spotify(seed_artists,seed_genres,seed_tracks,limit,target_valence,target_energy,target_danceability,target_liveness,target_loudness):
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
            "target_valence": target_valence,
            "target_energy": target_energy,
            "target_danceability": target_danceability,
            "target_liveness": target_liveness,
            "target_loudness": target_loudness
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
    target_valence=(emotions_value['Happy']+1-emotions_value['Happy'])/2
    target_energy=1-emotions_value['Sad']
    target_danceability=emotions_value['Happy']
    target_liveness=emotions_value['Happy']
    target_loudness=(emotions_value['Angry']+emotions_value['Fear'])/2

    recommendations = get_recommendations_on_spotify(seed_artists=artists,seed_genres=genres,seed_tracks=tracks,limit=n,target_valence=target_valence,target_energy=target_energy,target_danceability=target_danceability,target_liveness=target_liveness,target_loudness=target_loudness)
    #print(f"Recommendations: {recommendations}")
    for i in recommendations['tracks']:
        print(i['name'],"by",i['artists'][0]['name'])

if __name__ == '__main__':
    main()
