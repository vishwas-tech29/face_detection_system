

### ✅ `README.md`

```markdown
# 🧠 Face Detection & Logging System

A real-time intelligent face detection and recognition system built with Python, OpenCV, and face_recognition. This tool automatically detects faces from a webcam, identifies known individuals, logs the detection details, saves the full image, and plays a sound alert — all in a single seamless process.

> ⚡ Auto-detects faces → Saves full image → Logs name, time, image → Plays sound → Exits after first detection

---

## 📸 Features

- 🎯 Real-time face recognition from webcam
- 🧠 Compares with known faces using face encodings
- 📂 Saves full frame image on detection
- 📅 Logs `Name`, `Timestamp`, and `Image Filename` into a CSV
- 🔔 Plays sound alert when face is successfully detected
- 🛑 Automatically exits after first successful recognition (can be modified)
- 🗂️ Simple, production-ready folder structure

---

## 🗃️ Folder Structure

```

FACE\_DETECTION\_SYSTEM/
├── known\_faces/              # Images of known people (name.jpg/png)
├── logs/
│   ├── detections.csv        # Logged entries
│   └── images/               # Full-frame image captures
├── assets/
│   └── detected.mp3          # Alert sound
├── utils/
│   └── logger.py             # Helper for CSV logging
├── main.py                   # Main script
└── requirements.txt          # Project dependencies

````

---

## 📦 Requirements

- Python 3.7 or higher
- OpenCV (`opencv-python`)
- face_recognition
- numpy
- playsound

Install all dependencies:

```bash
pip install -r requirements.txt
````

> ⚠️ For Windows users: If `playsound` fails, use `.wav` format or switch to `simpleaudio`

---

## 🚀 Getting Started

### 1. Add Known Faces

Place images of known individuals in the `known_faces/` folder.
✅ File name should be the person’s name (e.g., `vishwas.jpg`)

### 2. Add a Sound File

Put an alert sound in `assets/` directory named `detected.mp3`.
You can use `.wav` if `playsound` fails and update the code accordingly.

### 3. Run the Program

```bash
python main.py
```

### 4. What Happens on Detection?

* Detects and matches face from webcam
* Saves full webcam image to `logs/images/`
* Logs data in `logs/detections.csv`:

  ```
  Name,Timestamp,Image
  vishwas,2025-06-28 01-12-34,vishwas_2025-06-28 01-12-34.jpg
  ```
* Plays the alert sound
* Exits the application

---

## 🧪 Demo

![screenshot](assets/demo_preview.png)

> Want a GIF or real-time video demo? Just ask.

---

## 🛠️ Customization Options

* 🟢 Detect multiple people before exit
* 🔁 Add a time-based cooldown for re-detection
* 🧑‍💻 Add GUI using Tkinter or PyQt
* ☁️ Sync logs/images to cloud
* 📲 Send alerts to mobile/email

Let me know if you'd like to add these — I’ll help step-by-step.

---


## 👨‍💻 Author

**Rallapalli Vishwas**
Final Year Major Project — Face AI Logging System

---

## ⭐️ Feedback or Support?

Open an issue or ping me via [LinkedIn]([https://linkedin.com](https://www.linkedin.com/in/rallapalli-vishwas/)) or GitHub.
If this project helped you — drop a ⭐️!

```
