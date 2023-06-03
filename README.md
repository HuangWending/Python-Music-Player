# Python-Music-Player

import tkinter as tk
from tkinter import filedialog
import pygame

导入所需的库：`tkinter`用于创建GUI，`filedialog`用于文件选择对话框，`pygame`用于音乐播放。

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("黄文定音乐播放器")
        self.root.geometry("500x400")

定义一个名为`MusicPlayer`的类，用于创建音乐播放器的窗口。在初始化方法`__init__`中，接受`root`作为参数并将其赋值给`self.root`，设置窗口标题为"黄文定音乐播放器"，并将窗口大小设置为500x400。

        self.selected_file = None
        self.music_playing = False

初始化`selected_file`变量为`None`，用于存储选择的音乐文件的路径。`music_playing`变量用于记录音乐是否正在播放。

        self.label = tk.Label(root, text="选择一个音乐文件")
        self.label.pack(pady=10)

创建一个标签组件，显示文本为"选择一个音乐文件"，并将其放置在窗口中间，使用`pack`方法设置间距为10。

        self.select_button = tk.Button(root, text="选择文件", command=self.select_file)
        self.select_button.pack(pady=5)

创建一个按钮组件，显示文本为"选择文件"，并将其放置在窗口中间，使用`pack`方法设置间距为5。点击该按钮会调用`select_file`方法。

        self.play_button = tk.Button(root, text="点击播放", command=self.play_music, state=tk.DISABLED)
        self.play_button.pack(pady=5)

创建一个按钮组件，显示文本为"点击播放"，并将其放置在窗口中间，使用`pack`方法设置间距为5。点击该按钮会调用`play_music`方法。初始状态为禁用状态。

    def select_file(self):
        self.selected_file = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3")])
        if self.selected_file:
            self.label.config(text="Selected file: " + self.selected_file)
            self.play_button.config(state=tk.NORMAL)

`select_file`方法被调用时，会弹出文件选择对话框，允许用户选择一个音乐文件。如果用户选择了文件，将文件的路径存储在`selected_file`变量中，并更新标签的文本以显示所选文件的路径。同时，将播放按钮的状态设置为可用。

    def play_music(self):
        if not self.music_playing:
            pygame.mixer.init()
            pygame.mixer.music.load(self.selected_file)
            pygame.mixer.music.play()
            self.play_button.config(text="停止播放")
            self.music_playing = True
        else:
            pygame.mixer.music.stop()
            self.play_button.config(text="点击播放

")
            self.music_playing = False

`play_music`方法被调用时，如果音乐没有正在播放，则初始化`pygame.mixer`，加载所选音乐文件，开始播放音乐，并将播放按钮的文本设置为"停止播放"，同时将`music_playing`变量设置为`True`表示音乐正在播放。如果音乐已经在播放，则停止音乐播放，将播放按钮的文本设置为"点击播放"，并将`music_playing`变量设置为`False`表示音乐停止播放。

root = tk.Tk()
music_player = MusicPlayer(root)
root.mainloop()

创建一个`Tk`对象作为根窗口，然后创建一个`MusicPlayer`对象，并将根窗口作为参数传递给`MusicPlayer`对象。最后，通过调用`mainloop`方法来启动主事件循环，使窗口保持显示状态。音乐播放器
