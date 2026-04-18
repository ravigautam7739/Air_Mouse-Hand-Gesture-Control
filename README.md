# 🖱️ Air Mouse (Hand Gesture Cursor Control)

A Python-based **touchless mouse control system** that allows you to move your cursor and click using **hand gestures**.

This project uses your webcam to track your hand and convert finger movements into **real-time cursor control**.

---

# 🚀 Features

✔ Move cursor using index finger
✔ Click using thumb + index finger gesture
✔ Real-time hand tracking
✔ Smooth cursor movement
✔ Touchless computer control

---

# 🛠 Technologies Used

* Python
* OpenCV
* MediaPipe (Hand Tracking)
* PyAutoGUI

---

# 📂 Project Structure

```id="air1"
air-mouse-gesture-control
│
├── main.py
└── README.md
```

👉 Rename your file to **main.py** for clean structure.

---

# ⚙️ Installation

1️⃣ Install Python 3.x

2️⃣ Install required libraries:

```bash id="air2"
pip install opencv-python mediapipe pyautogui
```

---

# ▶️ How to Run

```bash id="air3"
git clone https://github.com/ravigautam7739/air-mouse-gesture-control.git
cd air-mouse-gesture-control
python main.py
```

---

# 🧠 How It Works

1. Webcam captures hand movement
2. MediaPipe detects hand landmarks
3. Index finger controls cursor position

### 📌 Gestures:

* ☝️ Index finger → Move cursor
* 🤏 Thumb + Index close → Click

4. Cursor moves according to finger position
5. Click is triggered when fingers are close

---

# 💻 Example Output

```id="air4"
Move finger → Cursor moves

Pinch fingers →
CLICK
```

---

# 🎯 Use Cases

* Touchless computer control
* Gesture-based UI
* Accessibility tools
* Smart interfaces
* AI/Computer Vision demos

---

# ⚠️ Notes

* Requires webcam
* Works best with good lighting
* Keep hand clearly visible
* May need calibration for accuracy

---

# 🔮 Future Improvements

* Right click gesture
* Drag & drop support
* Multi-hand gestures
* Gesture-based scrolling
* GUI enhancements

---

# ⭐ Support

If you found this project interesting, give it a **star ⭐**.
