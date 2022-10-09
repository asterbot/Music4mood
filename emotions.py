import requests
import text2emotion as te
from flask import Flask, render_template, request



SPOTIFY_GET_RECOMMENDATIONS_URL = "https://api.spotify.com/v1/recommendations"
ACCESS_TOKEN = "BQAGt89rA_fiyOWgJHCV6RWyP2xUPgjAIidnmZPL_h-aY5tt1qKQlDInYARQgUUYijaeSQ6nNteBxPrR1InPSfejbPDQdt2RN2-rrIv-RomAvKBLj6kEZntmhR6q8oSInnpqzJMnQpUACVyNikhWvZFPOBPEuWTeBMFwUutsoAxb--7jSlBzRESbQYUNQs0"

main = Flask(__name__)

@main.route('/', methods=['POST', 'GET'])
def index():
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

    print(request.method)
    if request.method == 'GET':
        print("ok")
        text = request.form['thetext'] #replace 'thetext' with html name tag of input box
        num = request.form['thenumoftracks'] #replace 'thenumoftracks' with html name tag of input box
        
        artists = "4UXqAaa6dQYAk18Lv7PEgX"
        genres = "pop,country,classical"
        tracks = "0c6xIDDpzE81m2q797ordA"
        emotions_value=te.get_emotion(text)
        target_valence=(emotions_value['Happy']+1-emotions_value['Happy'])/2
        target_energy=1-emotions_value['Sad']
        target_danceability=emotions_value['Happy']
        target_liveness=emotions_value['Happy']
        target_loudness=(emotions_value['Angry']+emotions_value['Fear'])/2

        recommendations = get_recommendations_on_spotify(seed_artists=artists,seed_genres=genres,seed_tracks=tracks,limit=num,target_valence=target_valence,target_energy=target_energy,target_danceability=target_danceability,target_liveness=target_liveness,target_loudness=target_loudness)
        all_recommendations = [str(i['name'])+" by "+str(i['artists'][0]['name']) for i in recommendations['tracks']]
        print(all_recommendations)

        # HTML=f"""
        # <!DOCTYPE html>
        # <html>
        # <body>
        #     <p>enter your moods</p>
        #     <form>
        #         <input type="text" name="thetext" />
        #         <input type="text" name="thenumoftracks" />
        #         <input type="submit" value="submit" />
        #     </form>
        #     <p>"{all_recommendations}"</p>
        # </body>
        # </html>
        # """
        # with open(r"C:\Users\cinde\Documents\GitHub\Robohacks2\templates\index.html","w") as f:
        #     f.write(HTML)
            #print(f.read())
        return render_template('index.html', data=all_recommendations)

    return render_template('index.html',data="nothing to see here")




if __name__ == '__main__':
    main.run()
