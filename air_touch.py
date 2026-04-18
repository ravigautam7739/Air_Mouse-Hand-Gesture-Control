import cv2
import mediapipe as mp
import pyautogui

cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

screen_w, screen_h = pyautogui.size()

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)

                if id == 8:  # Index finger
                    screen_x = int(screen_w * lm.x)
                    screen_y = int(screen_h * lm.y)
                    pyautogui.moveTo(screen_x, screen_y)

                    cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)

                if id == 4:  # Thumb tip
                    thumb_x, thumb_y = int(lm.x * w), int(lm.y * h)

                    if abs(cx - thumb_x) < 30 and abs(cy - thumb_y) < 30:
                        pyautogui.click()
                        cv2.putText(img, "CLICK", (50, 100),
                                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("Air Mouse", img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()