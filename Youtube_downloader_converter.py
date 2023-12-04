import os
import tkinter as tk
from tkinter import ttk
from pytube import YouTube
from moviepy.editor import VideoFileClip

def download_and_convert():
    url = url_entry.get()
    output_path = output_directory_entry.get()

    try:
        # YouTube objektum létrehozása
        youtube = YouTube(url)

        # A videó letöltése a megadott elérési útvonalra
        video = youtube.streams.get_highest_resolution()
        video_file = video.download(output_path)

        # MP3-formátumba átalakítás
        mp3_file_path = convert_to_mp3(video_file)

        # Az eredeti videófájl törlése
        os.remove(video_file)

        result_label.config(text=f"A videó sikeresen letöltve és átalakítva MP3-formátumba. Mentve itt: {mp3_file_path}")
    except Exception as e:
        result_label.config(text=f"Hiba történt: {e}")

def convert_to_mp3(video_file):
    video_clip = VideoFileClip(video_file)
    audio_clip = video_clip.audio
    mp3_file_path = video_file.replace(".mp4", ".mp3")
    audio_clip.write_audiofile(mp3_file_path)
    audio_clip.close()
    video_clip.close()
    return mp3_file_path

# GUI létrehozása
app = tk.Tk()
app.title("YouTube Letöltő és Átalakító")

# URL beviteli mező
url_label = ttk.Label(app, text="YouTube URL:")
url_label.grid(row=0, column=0, padx=10, pady=10, sticky="W")
url_entry = ttk.Entry(app, width=40)
url_entry.grid(row=0, column=1, padx=10, pady=10)

# Célkönyvtár beviteli mező
output_directory_label = ttk.Label(app, text="Library:")
output_directory_label.grid(row=1, column=0, padx=10, pady=10, sticky="W")
output_directory_entry = ttk.Entry(app, width=40)
output_directory_entry.grid(row=1, column=1, padx=10, pady=10)

# Letöltés és átalakítás gomb
download_button = ttk.Button(app, text="Download and Convert", command=download_and_convert)
download_button.grid(row=2, column=0, columnspan=2, pady=10)

# Eredmény szöveg
result_label = ttk.Label(app, text="")
result_label.grid(row=3, column=0, columnspan=2, pady=10)

# GUI futtatása
app.mainloop()
