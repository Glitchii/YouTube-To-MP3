#!/usr/bin/env python

import sys, os
from pytube import YouTube
from moviepy.editor import *

def download_video(url):
    try:
        yt = YouTube(url)
        print('Title: ', yt.title)
        stream = yt.streams.first()
        print('Downloading video...')
        stream.download(filename='temp_video.mp4')
        print('Video downloaded successfully.')
    except Exception as e:
        print(f"Error downloading video: {e}")

def convert_to_mp3():
    try:
        video = VideoFileClip('temp_video.mp4')
        video.audio.write_audiofile('output.mp3')
        print('Successfully converted to MP3.')
        os.remove('temp_video.mp4')
    except Exception as e:
        print(f"Error converting to MP3: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
        download_video(url)
        convert_to_mp3()
    else:
        print('Please provide a YouTube URL as an argument.')
