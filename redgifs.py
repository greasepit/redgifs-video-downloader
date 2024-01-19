import requests
from urllib.request import Request, urlopen
import tkinter as tk


def Downloader(url, filename):
    FILE_TO_SAVE = filename + ".mp4"
    req = Request(
    url = url, 
    headers = {'User-Agent': 'Mozilla/5.0'}
)
    webpage = urlopen(req).read()
    webpage = webpage.decode("utf-8")
    videourl = webpage.split("https://api.redgifs.com/v2/gifs/")[1].split(".mp4")[0]
    videourl = "https://api.redgifs.com/v2/gifs/" + videourl + ".mp4"
    response = requests.get(videourl)
    with open(FILE_TO_SAVE, "wb") as f:
        f.write(response.content)
   

if __name__ == '__main__':
    window = tk.Tk()
    window.title("Redgifs downloader")
    window.geometry("380x400")
    
    urlentry = tk.Entry(window)
    urllabel = tk.Label(window,text="video url")
    fileentry = tk.Entry(window)
    filename = tk.Label(window,text="Save as")
    
    def onclick():
        url = urlentry.get()
        file = fileentry.get()
        Downloader(url,file)
        
    button = tk.Button(
        window,
        text="Download",
        width=25,
        height=5,
        command = lambda: onclick()
    )
    
    urlentry.pack()
    urllabel.pack()
    fileentry.pack()
    filename.pack()
    button.pack()
  
    window.mainloop()
