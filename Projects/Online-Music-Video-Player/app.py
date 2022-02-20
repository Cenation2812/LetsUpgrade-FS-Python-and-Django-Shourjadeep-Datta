#import firebase_admin
from flask import Flask, render_template,request, redirect
import json
import requests

app = Flask(__name__)

@app.route('/getsongs',methods = ["POST","GET"])
def songs():
    return render_template("basic.html")

@app.route('/browse',methods = ["GET","POST"])
def browse():
    video_lst = []
    if request.method == "POST":
        video_lst = []
        music_video = {}
        artist_name = ""
        artist_name = request.form["Artist"]
        print(artist_name)
        URL = f"https://www.theaudiodb.com/api/v1/json/1/search.php?s={artist_name}"

        if URL:
            response = requests.request("GET",URL)

            artist = response.content

            artist_data = json.loads(artist.decode('utf-8'))
            lst = []

            #print(artist_data)

            lst = artist_data["artists"]

            aid = lst[0]["idArtist"]

            url = f"https://theaudiodb.com/api/v1/json/1/mvid.php?i={aid}"

            if response:

                response = requests.request("GET",url)

                music_video = response.content

                music_video_data = json.loads(music_video.decode('utf-8'))
                #print(music_video_data)

                video_lst = music_video_data["mvids"]
                song_lst = []
                if video_lst:
                    for each in video_lst:
                        song_data = {}
                        song_data["songname"] = each["strTrack"]
                        song_data["link"] = each["strMusicVid"]
                        #print(song_data["songname"],song_data["link"])
                        song_lst.append(song_data)
                else:
                    return redirect('/getsongs')
            else:
                return redirect('/getsongs')
        else:
            return redirect('/getsongs')
        
    return render_template("next.html",songs = song_lst)

if __name__ == '__main__':
    app.run(host = "127.0.0.1",port = "5002",debug = True)