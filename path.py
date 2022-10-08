import requests

SPOTIFY_GET_RECOMMENDATIONS_URL = "https://api.spotify.com/v1/recommendations"
ACCESS_TOKEN = "BQBao0KerTYCi6sH_1FgkBXob85hPY8UcU5aYxxNqAum9di0JYUZ03x-r9CZNUZiBjYws6uD3b-RbUP9JgutAtufKxKAxydEeM7FuWkINbdiioreOE1EFD1F2A8buqqaKAY3_M18LRZu23bS1aA-fLU4nno42tK2nDAu6bermTP4LY_J36qoDiYokDyzmxc"

def get_recommendations_on_spotify(seed_artists,seed_genres,seed_tracks):
    response=requests.get(
        SPOTIFY_GET_RECOMMENDATIONS_URL,
        headers={
            "Authorization": f"Bearer {ACCESS_TOKEN}"
        },
        params={
            "seed_artists": seed_artists,
            "seed_genres": seed_genres,
            "seed_tracks": seed_tracks
        }
    )
    
    return response.json()

def main():
    artists = "4NHQUGzhtTLFvgF5SZesLK"
    genres = "classical,country"
    tracks = "0c6xIDDpzE81m2q797ordA"
    recommendations = get_recommendations_on_spotify(seed_artists=artists,seed_genres=genres,seed_tracks=tracks)
    #print(f"Recommendations: {recommendations}")
    for i in recommendations['tracks']:
        print(i['name'],"by",i['artists'][0]['name'])

if __name__ == '__main__':
    main()
