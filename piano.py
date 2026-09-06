import cv2

import mediapipe as mp
import mediapipe.python.solutions.hands as mp_hands
import mediapipe.python.solutions.drawing_utils as mp_drawing
import mediapipe.python.solutions.drawing_styles as mp_drawing_styles
import time
import pygame
pygame.mixer.init()

def run_hand_tracking_on_webcam():
    cap = cv2.VideoCapture(index=0)

    with mp_hands.Hands(
        model_complexity=0,
        max_num_hands=2,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5,
    ) as hands:
        while cap.isOpened():
            success, frame = cap.read()
            if not success:
                print("Ignoring empty camera frame...")
                continue

            # Check the frame for hands
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = hands.process(frame_rgb)

            # Draw the hand annotations on the image
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(
                        image=frame,
                        landmark_list=hand_landmarks,
                        connections=mp_hands.HAND_CONNECTIONS,
                        landmark_drawing_spec=mp_drawing_styles.get_default_hand_landmarks_style(),
                        connection_drawing_spec=mp_drawing_styles.get_default_hand_connections_style(),
                    )

            cv2.imshow("Hand Tracking", cv2.flip(frame, 1))
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

            b4_note = '/Users/vanisha/Downloads/piano-note-b4-bright-one-shot_100bpm_B_minor.wav' # replace with ur own path
            c5_note = '/Users/vanisha/Downloads/piano-note-c5-bright-one-shot_99bpm_F_minor.wav'
            a4_note = '/Users/vanisha/Downloads/piano-note-a4-bright-one-shot_91bpm_A_minor.wav'
            g4_note = '/Users/vanisha/Downloads/piano-note-g4-bright-one-shot_92bpm_G_minor.wav'

            
            if(hand_landmarks.landmark[11].y + 0.1 < hand_landmarks.landmark[8].y ):
                print("first finger is pressed")
                pygame.mixer.music.load(b4_note)
                pygame.mixer.music.play()
                time.sleep(0.3)

            if(hand_landmarks.landmark[15].y < hand_landmarks.landmark[12].y):
                print("second finger is pressed")
                pygame.mixer.music.load(c5_note)
                pygame.mixer.music.play()
                time.sleep(0.3)

            if(hand_landmarks.landmark[19].y < hand_landmarks.landmark[16].y):
                print("third finger is pressed")
                pygame.mixer.music.load(a4_note)
                pygame.mixer.music.play()
                time.sleep(0.3)
                pygame.mixer.music.load(g4_note)
                pygame.mixer.music.play()
                time.sleep(0.3)

            # if(hand_landmarks.landmark[4].y + 0.2 > hand_landmarks.landmark[11].y and hand_landmarks.landmark[3].y > hand_landmarks.landmark[15].y and hand_landmarks.landmark[3].y > hand_landmarks.landmark[19].y):
            #     print(hand_landmarks.landmark[4].x, hand_landmarks.landmark[11].x, "volume is increased") // didnt work out... but i will try later


    cap.release()

if __name__ == "__main__":
    run_hand_tracking_on_webcam()
