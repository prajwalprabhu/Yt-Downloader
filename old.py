from pytube import YouTube
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import os
import pickle
from time import perf_counter


def download_descriptio(root, youtube, directory):
    try:

        title = youtube.title.replace("|", "_")
        title = youtube.title.replace("||", "_")
        title = youtube.title.replace("&", "_")
        title = youtube.title.replace("!", "_")
        print("replaced")
        file = directory+"/"+title+"_discreption.txt"
        with open(file, "wb") as f:
            f.write(youtube.description.encode())
    except:
        title = "Youtube_video"
        file = directory+"/"+title+"_discreption.txt"
        with open(file, "wb") as f:
            f.write(youtube.description.encode())


def popup(youtube):
    messagebox.showinfo("Description Of  The Video ", youtube.description)


def download(root, youtube, mp4, directory):
    initial = perf_counter()
    if mp4 == 1:
        youtube.streams.first().download(directory)
    elif mp4 == 140:
        a = youtube.streams.get_by_itag(mp4).download(directory)

    else:
        a = youtube.streams.get_by_itag(mp4)
        a.download(directory)
    final = perf_counter()
    tk.Label(
        root, text=f"Done in{round((final-initial),2)}seconds").grid(row=11, column=0)


def continuee(root, e, path, download_path):
    done = 1
    if path.get() == "Select the folder to download":
        directory = filedialog.askdirectory(
            initialdir="/", title="Select the folder")
        download_path.insert(0, directory)
        root.update()
        with open("file_path.list", "wb") as f:
            pickle.dump(download_path, f)
    else:
        directory = path.get()

    try:

        youtube = YouTube(e.get())
        tk.Label(root, bg="#ff3333", fg="#ffff66",
                 text=f"Title : {youtube.title}\n Duration :{round((youtube.length)/60,2)} \n Author : {youtube.author} \n Views : {youtube.views} \n Average Ratings :{youtube.rating}").grid(row=5, column=0)
        tk.Button(root, text="To check the description click here", command=lambda: popup(
            youtube), bg="#ff3333", fg="#ffff66").grid(row=6, column=0)
        tk.Button(root, text="Download video (.mp4)", command=lambda: download(
            root, youtube, 1, directory), bg="#ff3333", fg="#ffff66").grid(row=7, column=0)
        tk.Button(root, text="Download the description", command=lambda: download_descriptio(
            root, youtube, directory), bg="#ff3333", fg="#ffff66").grid(row=8, column=0)
        tk.Button(root, text="Download video(360p)(.mp4)", command=lambda: download(
            root, youtube, 18, directory), bg="#ff3333", fg="#ffff66").grid(row=9, column=0)
        tk.Button(root, text="Download audio (.mp4)", command=lambda: download(
            root, youtube, 140, directory), bg="#ff3333", fg="#ffff66").grid(row=10, column=0)
    except Exception as e:
        print(e)
        done = 0
        tk.Label(root, text="Some Error occured while downloading",
                 bg="#ff3333", fg="#ffff66").grid(row=5, column=0)
        root.update()


def main():
    with open("file_path.list", "rb") as f:
        download_path = pickle.load(f)

    root = tk.Tk()
    root.title("YtDownloader")
    root.config(bg="#ff3333")
    path = tk.StringVar()
    path.set(download_path[0])
    tk.Label(text="Enter the url here", bg="#ff3333",
             fg="#ffff66").grid(row=0, column=0)
    e = tk.Entry()
    e.grid(row=1, column=0)
    menu = tk.OptionMenu(root, path, *download_path)
    menu.config(bg="#ff3333", fg="#ffff66")
    menu.grid(row=2, column=0)
    tk.Button(text="Continue", command=lambda: continuee(
        root, e, path, download_path), bg="#ff3333", fg="#ffff66").grid(row=3, column=0)
    root.mainloop()


if __name__ == '__main__':
    main()
