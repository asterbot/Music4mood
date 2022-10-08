import requests


SPOTIFY_GET_RECOMMENDATIONS_URL = f'https://api.spotify.com/v1/recommendations'
ACCESS_TOKEN = 'BQAcAJui0zV580Fp6FREPh3MrYQbAtCQsTfEhYux-pTBA0GqPe0x99ZJNFscmjexEh0km2JMfNBVvEB2u-V39iVEC97HCZMhwMEBxupZYmc7HHzrPAhvGjX7dzWhxC3mzmsD3b5G91tzBom9p_xgV8e-ffPZv6bC1czEW4PBRI9DqrQ_-RKabZ6_sHYTKpY'

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
    
    if (
    response.status_code != 204 and
    response.headers["content-type"].strip().startswith("application/json")):
        try:
            return response.json()
        except ValueError:
            # decide how to handle a server that's misbehaving to this extent
            pass


def main():
    artists = '4UXqAaa6dQYAk18Lv7PEgX'
    genres = 'pop,classical'
    tracks = '022DrG7Wp2PSCwzuD0bSzT'
    recommendations = get_recommendations_on_spotify(seed_artists=artists,seed_genres=genres,seed_tracks=tracks)
    print(f"Recommendations: {recommendations}")

if __name__ == '__main__':
    main()
