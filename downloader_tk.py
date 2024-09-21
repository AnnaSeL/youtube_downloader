from tkinter import *
from tkinter import ttk
from pytube import YouTube

def get_the_youtube_obj():
    url = entry_url.get()
    yt = YouTube(url)
    return yt

def get_path():
    path = entry_path.get()
    return path

def print_info(yt):
    title_label = ttk.Label(text=f"Title: {yt.title}", font=10)
    title_label.pack(pady=5)

    duration_label = ttk.Label(text=f"Duration: {yt.length} secs", font=10)
    duration_label.pack(pady=5)

    root.update()

def print_finished():
    finish_label = ttk.Label(text=f"File uploading is complete :)", font=10)
    finish_label.pack(pady=5)
    root.update()

def download_video():
    yt = get_the_youtube_obj()
    print_info(yt)
    video = yt.streams.first()
    path = get_path()
    video.download(path)
    print_finished()

def download_audio():
    yt = get_the_youtube_obj()
    print_info(yt)
    audio = yt.streams.filter(only_audio=True).first()
    path = get_path()
    audio.download(path, filename=f"{yt.title}.mp3")
    print_finished()


root = Tk()
root.title("Youtube Downloader")
width = 500
height = 340
root.geometry(f"{width}x{height}+{(root.winfo_screenwidth()-width)//2}+{(root.winfo_screenheight()-height)//2}")
root.resizable(width=False, height=False)
root.iconbitmap(default="youtube16.ico")

# URL Label and Entry
url_label = ttk.Label(text="Input Url", font=12)
url_label.pack(pady=5)

entry_url = ttk.Entry(width=45)
entry_url.pack(pady=5)

# Path Label and Entry
path_label = ttk.Label(text="Input Path", font=12)
path_label.pack(pady=5)

entry_path = ttk.Entry(width=45)
entry_path.pack(pady=5)

# Frame for buttons to center them
frame_buttons = Frame(root)
frame_buttons.pack(pady=10)

# Format Label
format_label = ttk.Label(frame_buttons, text="Choose format", font=12)
format_label.pack(side=TOP, pady=5)

# Video and Audio buttons on the same row
btn_video = ttk.Button(frame_buttons, text="Video", command=download_video)
btn_video.pack(side=LEFT, padx=10)

btn_audio = ttk.Button(frame_buttons, text="Audio", command=download_audio)
btn_audio.pack(side=LEFT, padx=10)




root.mainloop()