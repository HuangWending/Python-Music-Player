import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("黄文定音乐播放器")
        self.root.geometry("500x400")

        self.selected_file = None
        self.music_playing = False

        self.label = tk.Label(root, text="选择一个音乐文件")
        self.label.pack(pady=10)

        self.select_button = tk.Button(root, text="选择文件", command=self.select_file)
        self.select_button.pack(pady=5)

        self.play_button = tk.Button(root, text="点击播放", command=self.play_music, state=tk.DISABLED)
        self.play_button.pack(pady=5)

    def select_file(self):
        self.selected_file = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3")])
        if self.selected_file:
            self.label.config(text="Selected file: " + self.selected_file)
            self.play_button.config(state=tk.NORMAL)

    def play_music(self):
        if not self.music_playing:
            pygame.mixer.init()
            pygame.mixer.music.load(self.selected_file)
            pygame.mixer.music.play()
            self.play_button.config(text="停止播放")
            self.music_playing = True
        else:
            pygame.mixer.music.stop()
            self.play_button.config(text="点击播放")
            self.music_playing = False

root = tk.Tk()
music_player = MusicPlayer(root)
root.mainloop()
