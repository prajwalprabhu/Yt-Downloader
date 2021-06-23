from tkinter import Button, Entry, Label, Tk

from pytube.__main__ import YouTube
from tkinter import messagebox
from time import perf_counter

import os


class app:
    def __init__(self):
        home = os.path.expanduser("~")
        print(home)
        self.file_path = f"{home}/Downloads/Yt/"
        self.root = Tk()
        self.root.title("Yt Downloader")
        Label(text="Enter Your url here").grid(row=0, column=0)
        self.entry = Entry()
        self.entry.grid(row=1, column=0)
        Button(text="Continue",
               command=self.get_data).grid(row=3, column=0)

        # self.entry = Entry()
        self.root.mainloop()

    def download(self, mp4):
        initial = perf_counter()
        if mp4 == 1:
            self.youtube.streams.first().download(self.file_path)
        elif mp4 == 140:
            a = self.youtube.streams.get_by_itag(mp4).download(self.file_path)

        else:
            a = self.youtube.streams.get_by_itag(mp4)
            a.download(self.file_path)
        final = perf_counter()
        Label(
            self.root, text=f"Done in{round((final-initial),2)}seconds").grid(row=11, column=0)

    def popup(self):
        messagebox.showinfo("Description Of  The Video ",
                            self.youtube.description)

    def get_data(self):
        print(self.entry.get())
        try:

            self.youtube = YouTube(self.entry.get())
            Label(self.root,
                  text=f"Title : {self.youtube.title}\n Duration :{round((self.youtube.length)/60,2)} \n Author : {self.youtube.author} \n Views : {self.youtube.views} \n Average Ratings :{self.youtube.rating}").grid(row=5, column=0)
            Button(self.root, text="To check the description click here",
                   command=self.popup,).grid(row=6, column=0)
            Button(self.root, text="Download video (.mp4)", command=lambda: self.download(
                1),).grid(row=7, column=0)
            Button(self.root, text="Download the description",
                   command=self.download_description).grid(row=8, column=0)
            Button(self.root, text="Download video(360p)(.mp4)", command=lambda: self.download(
                18),).grid(row=9, column=0)
            Button(self.root, text="Download audio (.mp4)", command=lambda: self.download(
                140),).grid(row=10, column=0)
        except Exception as e:
            print(e)
            done = 0
            Label(self.root, text="Some Error occured while downloading",
                  ).grid(row=5, column=0)
            self.root.update()

    def download_description(self):
        try:

            title = self.youtube.title.replace("|", "_")
            title = self.youtube.title.replace("||", "_")
            title = self.youtube.title.replace("&", "_")
            title = self.youtube.title.replace("!", "_")
            print("replaced")
            file = self.file_path+"/"+title+"_discreption.txt"
            with open(file, "wb") as f:
                f.write(self.youtube.description.encode())
        except:
            title = "Youtube_video"
            file = self.file_path+"/"+title+"_discreption.txt"
            with open(file, "wb") as f:
                f.write(self.youtube.description.encode())


if __name__ == "__main__":
    app()
