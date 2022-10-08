import requests

user_id='iiwvh24n0pszxg56r4kj31016'
SPOTIFY_CREATE_PLAYLIST_URL = f'https://api.spotify.com/v1/users/{user_id}/playlists'
ACCESS_TOKEN = 'BQBQhMCVASThhixnioNSc__JWC8gu83Uev_58zvx0WGB5DOQ2-RNyqbN8Cv1AfXx5fW1p3VNOCv1QM_JOOOCdo1SIfM3ICQdqneqaL2fYGDsp-h-yUHX8n38Ks_9Ar9Dgwj0919tNpv3CurLDmmfEbU4wlFJNOGcdMcy9OPSiEWRjMpWUCrr9B3I1B_9iZ_YVN0E0UclWYqH9IxlKhzRE2ZkVIglbki8Y6hEN_b3cK3Zo-f_kaZ6U_nDZRo1'

def create_playlist_on_spotify(name,public):
    response=requests.post(
        SPOTIFY_CREATE_PLAYLIST_URL,
        headers={
            "Authorization": f"Bearer {ACCESS_TOKEN}"
        },
        json={
            "name": name,
            "public": public
        }
    )
    json_resp = response.json()
        
    return json_resp


def main():
    playlist=create_playlist_on_spotify(name='coding',public=False)
    print(f"Playlist: {playlist}")

if __name__ == '__main__':
    main()