import tkinter as tk
from tkinter import messagebox
import pygame
import pyperclip
import os
import time
from morse.logic import text_to_morse

# Initialize Pygame for sound
pygame.init()
pygame.mixer.init()

# Play background music
pygame.mixer.music.load("assets/background_music.mp3")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)  # loop

# Morse beep
def beep_morse(morse_code):
    dot = pygame.mixer.Sound("assets/dot.wav")
    dash = pygame.mixer.Sound("assets/dash.wav")

    for char in morse_code:
        if char == ".":
            dot.play()
            time.sleep(0.2)
        elif char == "-":
            dash.play()
            time.sleep(0.3)
        elif char == " ":
            time.sleep(0.2)
        elif char == "/":
            time.sleep(0.6)

# GUI
root = tk.Tk()
root.title("🛰️ Star Wars Morse Translator")
root.geometry("600x400")
root.resizable(False, False)

# Sci-fi Background
bg_img = tk.PhotoImage(file="assets/background.png")
bg_label = tk.Label(root, image=bg_img)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Font
FONT = ("Star Jedi", 16)
FONT_PATH = os.path.abspath("assets/starjedi.ttf")
tk.font.Font(family="Star Jedi", size=16)

# Title
title = tk.Label(root, text="MORSE TRANSLATOR", font=FONT, fg="gold", bg="#000000")
title.pack(pady=10)

# Entry
entry = tk.Entry(root, font=("Arial", 14), width=40, bg="black", fg="lime")
entry.pack(pady=10)

# Morse Display
output = tk.Text(root, height=5, font=("Courier", 14), bg="black", fg="cyan")
output.pack(pady=10)

def translate():
    text = entry.get()
    if not text:
        messagebox.showwarning("Empty", "Please enter some text.")
        return
    morse = text_to_morse(text)
    output.delete(1.0, tk.END)
    output.insert(tk.END, morse)
    beep_morse(morse)

def copy_to_clipboard():
    pyperclip.copy(output.get("1.0", tk.END).strip())
    messagebox.showinfo("Copied", "Morse code copied to clipboard!")

# Buttons
btn_frame = tk.Frame(root, bg="black")
btn_frame.pack()

translate_btn = tk.Button(btn_frame, text="Translate", command=translate, bg="gray20", fg="white", font=FONT)
translate_btn.grid(row=0, column=0, padx=10)

copy_btn = tk.Button(btn_frame, text="Copy", command=copy_to_clipboard, bg="gray20", fg="white", font=FONT)
copy_btn.grid(row=0, column=1, padx=10)

root.mainloop()
