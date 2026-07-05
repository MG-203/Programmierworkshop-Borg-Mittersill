import cv2
import mediapipe as mp
import os
import threading
from . import Recognisers as rg

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "..", "model", "hand_landmarker.task")

BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

latest_result = None
latest_move = "NONE"
latest_shoot = False

timestamp = 0
running = False
cap = None
landmarker = None
lock = threading.Lock()


def result_callback(result, output_image, timestamp_ms):
    global latest_result, latest_move, latest_shoot

    move = "NONE"
    shoot = False

    if result.hand_landmarks:
        hand = result.hand_landmarks[0]

        angle = rg.thumbsUpAngle(hand)

        if angle != -200:
            if angle < -20:
                move = "LEFT"
            elif angle > 20:
                move = "RIGHT"

        if rg.isOpenHand(hand):
            shoot = True

    with lock:
        latest_result = result
        latest_move = move
        latest_shoot = shoot


def camera_loop():
    global timestamp, running, cap, landmarker

    while running:
        ret, frame = cap.read()
        if not ret:
            continue

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        image = mp.Image(
            image_format=mp.ImageFormat.SRGB,
            data=rgb
        )

        landmarker.detect_async(image, timestamp)
        timestamp += 1

        cv2.imshow("Hand Gesture", frame)
        cv2.waitKey(1)


def start():
    global running, cap, landmarker

    options = HandLandmarkerOptions(
        base_options=BaseOptions(model_asset_path=MODEL_PATH),
        running_mode=VisionRunningMode.LIVE_STREAM,
        result_callback=result_callback,
        num_hands=1
    )

    landmarker = HandLandmarker.create_from_options(options)
    cap = cv2.VideoCapture(0)

    running = True
    thread = threading.Thread(target=camera_loop, daemon=True)
    thread.start()


def get_controls():
    with lock:
        return latest_move, latest_shoot


def close():
    global running, cap

    running = False

    if cap is not None:
        cap.release()

    cv2.destroyAllWindows()