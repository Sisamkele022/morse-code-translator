# 🔐 Morse Code Translator

Hey there! 👋  
This is a fun little Morse Code Translator I built (yeah, like the one R2-D2 would use to prank C-3PO).  
It converts plain text ➡️ Morse code and back again.

---

## ✨ Features

- 🔤 Translate text to Morse code
- 📻 Decode Morse code back to normal text
- 🖥️ Clean and simple GUI (no terminal stress)
- 😵 Handles spaces, punctuation, numbers — the whole squad
- 🚫 No crashes on empty input

---

## ⚙️ How to Use It

### 1. Clone the repo

```bash
git clone https://github.com/Sisamkele022/morse-code-translator.git
cd morse-code-translator
````

### 2. Run the app

Make sure you have Python installed. Then just:

```bash
python main.py
```

Yup. That’s it.

> Note: GUI is built with `tkinter` (which comes with Python by default).

---

## 🧠 What It Can Do

### 🧾 Text → Morse

```python
lettersToMorseCode("Darth Vader is Luke’s father")
# Output:
# "-.. .- .-. - .... / ...- .- -.. . .-. / .. ... / .-.. ..- -.- . .----. ... / ..-. .- - .... . .-."
```

### 📡 Morse → Text

```python
morseCodeToLetters(".... . .-.. .-.. --- / - .... . .-. .")
# Output:
# "HELLO THERE"
```

---

## 🧪 Example Use Cases

* 🔒 Send secret messages to your bestie
* 👻 Confuse your friends in the group chat
* 💥 Hide spoilers from nosy people
* 🤖 Teach a robot how to flirt

---

## 🗂️ Project Structure

```bash
morse-code-translator/
├── main.py            # GUI and app launcher
├── translator.py      # The logic behind the translator
├── README.md          # You’re reading it right now
└── requirements.txt
```

---

## 🚧 Future Upgrades?

If I get extra time or feel fancy:

* [ ] Add beep sounds for each Morse character
* [ ] Build a command-line version
* [ ] Add dark mode 🌚
* [ ] Let users copy Morse code with one click

---

## 🧑🏽‍💻 Built by

**Sisamkele Vava**
Just a dev building cool stuff and dodging the Empire.
[GitHub Profile](https://github.com/Sisamkele022)

---

## 🛸 Peace Out

Hope you enjoy it.
Wanna collab or give ideas? Drop me a DM or PR.
This is the way. ✌️

````

---

### ✅ Next Steps:

1. Save this into `README.md`
2. Then commit and push it:

```bash
git add README.md
git commit -m "Add fun README with my own style"
git push origin readme-file
````
