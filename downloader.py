from pytube import YouTube

def get_the_youtube_obj():
    url = input("Specify the URL: ")
    yt = YouTube(url)
    return yt

def get_path():
    path = input("PLease, specify path to a file to save video: ")
    return path

def download_video():
    yt = get_the_youtube_obj()
    print("Title :", yt.title)
    print("Duration: ", yt.length)
    print("Resolution: ", yt.streams.first().resolution)
    video = yt.streams.first()
    path = get_path()
    video.download(path)


def download_audio():
    yt = get_the_youtube_obj()
    print("Title :", yt.title)
    print("Duration: ", yt.length)
    print("Resolution: ", yt.streams.first().resolution)
    audio = yt.streams.filter(only_audio=True).first()
    path = get_path()
    audio.download(path, filename=f"{yt.title}.mp3")

def get_choice():
    choice = input("Would you like to download video or audio (video/audio) ? ")
    if choice == "video":
        download_video()
    elif choice == "audio":
        download_audio()
    else:
        "Wrong mode."

if __name__ == "__main__":
    get_choice()
