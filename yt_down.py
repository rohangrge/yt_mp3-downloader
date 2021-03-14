from __future__ import unicode_literals
import youtube_dl


with open("POP MAL SONGS .txt") as fp:
    Lines = fp.readlines()
a = []
for i in Lines:
    a.append(i)

for j in a:
    link = j.split()
    path = link[1]
    ydl_opts = {'postprocessors': [
        {'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '192'}]}
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([path])
    except:
        continue
