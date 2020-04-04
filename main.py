import time
from tkinter import * #<- なにこれ 書かないと動かない
from tkinter import ttk # こうやって書くとダークモードで字が消えないらしい
#import tkinter as tk 

root = Tk() # .とか=の前って自分で名前変えて良いところ？なおここを変えれば引数内も変える必要はありそう ->動いた！
root.title("タイトル表示場所")
frame1 = ttk.Frame(root)
label1 = ttk.Label(frame1, text="your name:") 

t = StringVar() # Labelに表示するテキストを更新するもの？


root.mainloop()