#!/usr/bin/env python3

import typer
from yt_dlp import YoutubeDL

cli = typer.Typer()

def download(url: str, format: str):
    if format.lower() == "mp3":
        options = {
            "format": "bestaudio/best",
            "outtmpl": "%(title)s.%(ext)s",
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }],
            "quiet": False,
        }
    elif format.lower() == "mp4":
        # Download the best available video+audio and merge them into an mp4.
        options = {
            "format": "bestvideo+bestaudio/best",
            "outtmpl": "%(title)s.%(ext)s",
            "merge_output_format": "mp4",
            "quiet": False,
        }

    with YoutubeDL(options) as ydl:
        ydl.download([url])

@cli.command()
def main(links: list[str] = typer.Argument(..., help="List of YouTube video URLs."), format: str = typer.Option("mp3", "--format", "-f", help="Output format: 'mp3' for audio, 'mp4' for video.")) -> None:
    """
    Download a list of YouTube links and convert them to the specified format.
    """
    
    for url in links:
        typer.echo(f"Downloading {url} as {format}...")
        download(url, format.lower())

if __name__ == "__main__":
    cli()
