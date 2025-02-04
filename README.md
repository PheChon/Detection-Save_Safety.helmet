# Safety Hardhat Detection Program

## Overview
This program is designed to detect whether a person is wearing a safety hardhat in real-time using machine learning. The detection system utilizes a YOLO-based model to analyze live camera feeds and determine compliance with safety regulations.

## Features
- **User Authentication:** Users must log in before accessing the system.
- **Registration System:** New users can register through the interface.
- **Real-time Hardhat Detection:** Uses YOLO for detecting safety hardhats.
- **Sound Alerts:** Provides audio feedback based on detection results.
- **Image Capture and Storage:** Saves detected images for future reference.
- **Login Status Check:** Tracks user login times and statuses.

## Requirements
- Python 3.x
- OpenCV (`cv2`)
- Tkinter (built-in with Python)
- Ultralytics YOLO (`ultralyticsplus`)
- Google Text-to-Speech (`gTTS`)

## Installation
1. Clone or download the repository:
   ```sh
   git clone https://github.com/PheChon/Detection-Save_Safety.helmet
   cd your-repository-folder
   ```
2. Install dependencies manually using:
   ```sh
   pip install opencv-python gtts ultralyticsplus
   ```
3. Ensure `username.txt` and `password.txt` exist in the directory for user authentication.

## Usage
1. Run the program:
   ```sh
   python minipro_ui_realfinal.py
   ```
2. **User Authentication:**
   - If you are a new user, register using the registration window.
   - Enter your username and password to log in.
3. **Detection Process:**
   - Once logged in, the program will prompt you to start the safety hardhat detection.
   - The camera feed will analyze safety compliance in real time.
   - If a safety hardhat is detected, the system will provide a confirmation alert.
   - If no safety hardhat is detected, an alert will sound, and an image may be saved for documentation.
4. **Data Storage:**
   - Login times are recorded in `check_time.txt`.
   - Images of detections are stored in separate folders (`img_detecting_Have` and `img_detecting_No-Have`).

## File Structure
- `minipro_ui_realfinal.py`: Main application script.
- `username.txt`: Stores registered usernames.
- `password.txt`: Stores registered passwords in `username:password` format.
- `check_time.txt`: Logs user login times.
- `img_detecting_Have/`: Stores images where a hardhat is detected.
- `img_detecting_No-Have/`: Stores images where a hardhat is not detected.

## Notes
- Users must create an account before logging in.
- The program saves images of detections into categorized folders.
- Hardhat detection is powered by a YOLOv8 model.
- Ensure the camera is properly connected before running the program.

## License
This project is open-source under the MIT License. Feel free to modify and improve it!

## Author
- **Pha.Chon (Teeraphop Chantra)**