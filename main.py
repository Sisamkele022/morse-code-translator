import tkinter as tk
from tkinter import messagebox
from translator import letters_to_morse, morse_to_letters

def encode_text():
    text = input_text.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Empty Input", "Please enter some text to encode.")
        return
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, letters_to_morse(text))


def decode_text():
    text = input_text.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Empty Input", "Please enter Morse code to decode.")
        return
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, morse_to_letters(text))


# GUI setup
window = tk.Tk()
window.title("🚀 R2-D2's Morse Code Translator")
window.geometry("600x400")
window.configure(bg="#1c1c1c")

title = tk.Label(window, text="R2-D2's Morse Code Translator", font=("Courier", 16, "bold"), fg="#FFD700", bg="#1c1c1c")
title.pack(pady=10)

input_text = tk.Text(window, height=5, width=60, font=("Courier", 12))
input_text.pack(pady=10)

button_frame = tk.Frame(window, bg="#1c1c1c")
button_frame.pack()

encode_btn = tk.Button(button_frame, text="🔐 Encode", command=encode_text, bg="#007BFF", fg="white", padx=10)
encode_btn.grid(row=0, column=0, padx=10)

decode_btn = tk.Button(button_frame, text="🔓 Decode", command=decode_text, bg="#28A745", fg="white", padx=10)
decode_btn.grid(row=0, column=1, padx=10)

output_text = tk.Text(window, height=5, width=60, font=("Courier", 12), bg="#f5f5f5")
output_text.pack(pady=10)

window.mainloop()
