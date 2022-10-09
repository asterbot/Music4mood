import requests
import text2emotion as te
from flask import Flask, render_template, request,json

global count
count=0
SPOTIFY_GET_RECOMMENDATIONS_URL = "https://api.spotify.com/v1/recommendations"
ACCESS_TOKEN = "BQCgsQIwyfglSmHVYDRHrYKoRWB7yK_QsBtw_eFyVfr4_zyF6Pdoxy3jaekSXZCLlwt_oSHsjbjer0hTuMdenJ7EFeS2kQvfpJ9d8ZzY7wC8etlztZAkEi1Wcfn19Hx1zotvqQxPF5etAKUoDbaqZbSde8eWafZf_q4q9m1umW3p9bSGqQAeddDlpui2nY4"
main = Flask(__name__)

@main.route('/', methods=['POST','GET'])
def index():
    global count
    #print("count: ",count)
         
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

    #print(request.method)
    if count>=1:
        text = str(request.values.get("thetext")) #replace 'thetext' with html name tag of input box
        num = int(request.values.get("thenumoftracks")) #replace 'thenumoftracks' with html name tag of input box
        print(text)
        print(num)
        if request.method == 'GET':
            #print("ok")
            artists = "4UXqAaa6dQYAk18Lv7PEgX"
            genres = "pop,country,classical"
            tracks = "0c6xIDDpzE81m2q797ordA"
            emotions_value=te.get_emotion(text)
            target_valence=(emotions_value['Happy']+1-emotions_value['Sad'])/2
            target_energy=1-emotions_value['Sad']
            target_danceability=emotions_value['Happy']
            target_liveness=emotions_value['Happy']
            target_loudness=(emotions_value['Angry']+emotions_value['Fear'])/2

            recommendations = get_recommendations_on_spotify(seed_artists=artists,seed_genres=genres,seed_tracks=tracks,limit=num,target_valence=target_valence,target_energy=target_energy,target_danceability=target_danceability,target_liveness=target_liveness,target_loudness=target_loudness)
            #print(recommendations)
            #all_recommendations = [(str(i['name'])+" by "+str(i['artists'][0]['name'])) for i in recommendations['tracks']]
            all_recommendations=[i['external_urls']['spotify'] for i in recommendations['tracks']]
            print(all_recommendations)
            json_string = json.dumps(all_recommendations)

            
            return render_template('index.html', data=json_string)

    count+=1
    return render_template('index.html',data="nothing to see here")




if __name__ == '__main__':
    main.run()
