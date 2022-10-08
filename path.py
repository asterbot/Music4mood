import requests

# seed_artists = '4NHQUGzhtTLFvgF5SZesLK'
# seed_genres = 'pop'
# seed_tracks = '0c6xIDDpzE81m2q797ordA'
SPOTIFY_GET_RECOMMENDATIONS_URL = f'https://api.spotify.com/v1/recommendations'
ACCESS_TOKEN = 'BQD9e1QBoBE9UK1MyrZwEsf9vOKeyrn5--QtCRLX52GMCdZp3wo12iybVQGT5NrC1_c_-x854YgiHuE3mwBEv5gdhSAqYHKGay-ayQYj9fwOtfvERvOiCJjGEcpmuINjiaBK2Y1ohR94mnxqdlYsPN79pdD1JNnYakFPwFpjOCQP6v8bsk5Dllb8kkOJwHc'
def get_recommendations_on_spotify(seed_artists,seed_genres,seed_tracks):
    response=requests.get(
        SPOTIFY_GET_RECOMMENDATIONS_URL,
        headers={
            "Authorization": f"Bearer {ACCESS_TOKEN}",
            "Content-Type": "application/json",
            "Host": "api.spotify.com"
        },
        json={
            "seed_artists": seed_artists,
            "seed_genres": seed_genres,
            "seed_tracks": seed_tracks
        }
    )
    json_resp = response.json()
        
    return json_resp    

def main():
    recommendations = get_recommendations_on_spotify(seed_artists="4NHQUGzhtTLFvgF5SZesLK",seed_genres="pop",seed_tracks="0c6xIDDpzE81m2q797ordA")
    print(f"Recommendations: {recommendations}")

if __name__ == '__main__':
    main()
