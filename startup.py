import tkinter as tk
import sys

def create_bsod(message):
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(bg='black')
    root.attributes('-topmost', True)
    label = tk.Label(root, text=message, bg='Black', fg='white', font=('Arial', 30), padx=20, pady=20)
    label.pack(expand=True)

    def on_closing():
        root.destroy()
        sys.exit()

    root.protocol('WM_DELETE_WINDOW', on_closing)

    root.bind('<Escape>', lambda e: on_closing())

    root.mainloop()

message = "楽しかった?www\nみんなはこんなクソみたいなratに引っかからない用にね...\nこの画面はescで閉じれます！\n※一切データは取得していません。bsodはフェイクです。"
create_bsod(message)
