from pytube.cli import on_progress
from pytube import YouTube
import pandas as pd

df = pd.read_csv('downloadable links.csv')
for i in range(len(df['Category'])):
    cat = df['Category'][i]
    link = df['Link'][i]

    yt = YouTube(link, on_progress_callback=on_progress)
    print(yt.title)
    yt.streams.first().download(output_path = str('./Videos/' + cat + '/'))
    print('Completed.')
