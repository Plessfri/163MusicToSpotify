import json
import sys
import urllib
import httplib2
import urllib3
import os

while 1:
        fileName = input("File name:")
        with open(os.path.join(sys.path[0], fileName), "r", encoding = 'utf-8') as f:
                data = json.loads(f.read())
                
        output = ""

        if data["ErrCode"] != "OK":
                print(data["ErrCode"])
                print(errRetrive)
                print(help)
                continue
                
        body = data["Body"]
        playlistName = body["name"]
        tracks = body["songs"]
        
        for track in tracks:
                trackName = track["title"]
                artist = track["author"]
                output += trackName + " - " + artist + "\n" 
        
        with open(playlistName + ".txt", "wb+") as file:
                file.write(output.encode("utf8"))

        print("===== Success =====\nCheck the directory of this file and find the .txt file!")
        print
