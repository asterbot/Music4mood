import requests

user_id='m8f4bbvgse5o0a1n0fpmkmswc'
playlist_id='3eHvv9AcEN97dQROnoFrU3'
SPOTIFY_CREATE_PLAYLIST_URL = f'https://api.spotify.com/v1/users/{user_id}/playlists'
SPOTIFY_CHANGE_PLAYLIST_URL = f'https://api.spotify.com/v1/playlists/{playlist_id}'


ACCESS_TOKEN = '' #put access token here from spotify developer.spotify.com and go to console and get access token

# def create_playlist_on_spotify(name,public):
#     response=requests.post(
#         SPOTIFY_CREATE_PLAYLIST_URL,
#         headers={
#             "Authorization": f"Bearer {ACCESS_TOKEN}"
#         },
#         json={
#             "name": name,
#             "public": public
#         }
#     )
#     json_resp = response.json()
        
#     return json_resp


def change_playlist_on_spotify(name,description,public):
    response=requests.put(
        SPOTIFY_CHANGE_PLAYLIST_URL,
        headers={
            "Authorization": f"Bearer {ACCESS_TOKEN}"
        },
        json={
            "name": name,
            "description": description,
            "public": public
        }
    )
    #json_resp = response.json()
        
    #return json_resp
    

def main():
    change_playlist_on_spotify(name='drunklist',description='i am actually NOT problematic',public=False)
    #print(f"Playlist: {playlist}")

if __name__ == '__main__':
    main()