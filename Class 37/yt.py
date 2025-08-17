# from pytube import YouTube
# def download_youtube_video(url, output_path='.'):
#     yt_opts = {
#         'format': 'best',
#         'outtmpl': f'{output_path}/%(title)s.%(ext)s', 
#         'live_stream': True,
#         'merage_output_format': 'mp4',
#         'skip_existing': True,
#     }
#     with YouTube(yt_opts) as yt:
#         yt.download([url])
# # Example usage:
# url = "https://youtu.be/s9gG108zDh4?si=tFDhQ9X_8GD1y-FC"
# download_youtube_video(url, output_path ='./downloads')

import yt_dlp

def download_youtube_video(url, output_path="./downloads"):
    ydl_opts = {
        "outtmpl": f"{output_path}/%(title)s.%(ext)s",
        "format": "best"
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Example
url = "https://youtu.be/s9gG108zDh4?si=tFDhQ9X_8GD1y-FC"
download_youtube_video(url, "./downloads")

