from pathlib import Path
import yt_dlp
import csv

def download_video(url):

    Path("videos").mkdir(exist_ok=True)

    # Save inside videos/ using the video title as the filename
    ydl_options = {
        "outtmpl": "videos/%(title)s.%(ext)s"
    }

    with yt_dlp.YoutubeDL(ydl_options) as ydl:
        ydl.download([url])
        
def read_video_urls(csv_path):
    url_list = []
    with open(csv_path, newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            # print(row["title"], row["url"])
            url_list.append(row["url"])
    return url_list

def write_to_file(file_path, data):
    if Path(file_path).is_file() and Path(file_path).exists():
        with open(file_path, "a") as file:
            file.write(f"\n{data}")
    else:
        with open(file_path, "w") as file:
            file.write(f"\n{data}")