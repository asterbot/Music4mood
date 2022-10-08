import requests
import text2emotion as te

SPOTIFY_GET_RECOMMENDATIONS_URL = "https://api.spotify.com/v1/recommendations"
ACCESS_TOKEN = "BQAGt89rA_fiyOWgJHCV6RWyP2xUPgjAIidnmZPL_h-aY5tt1qKQlDInYARQgUUYijaeSQ6nNteBxPrR1InPSfejbPDQdt2RN2-rrIv-RomAvKBLj6kEZntmhR6q8oSInnpqzJMnQpUACVyNikhWvZFPOBPEuWTeBMFwUutsoAxb--7jSlBzRESbQYUNQs0"

def get_recommendations_on_spotify(seed_artists,seed_genres,seed_tracks,limit):
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
        }
    )
    
    return response.json()

def main():
    artists = "4UXqAaa6dQYAk18Lv7PEgX"
    genres = "pop,country,classical"
    tracks = "0c6xIDDpzE81m2q797ordA"

    recommendations = get_recommendations_on_spotify(seed_artists=artists,seed_genres=genres,seed_tracks=tracks,limit=int(input("Enter limit:")))
    #print(f"Recommendations: {recommendations}")
    for i in recommendations['tracks']:
        print(i['name'],"by",i['artists'][0]['name'])

if __name__ == '__main__':
    main()
