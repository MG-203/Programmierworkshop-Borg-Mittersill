from handgesture.gesture_control import update, close
import cv2

while True:
    frame = update()

    if frame is not None:
        cv2.imshow("Camera Test", frame)

    if cv2.waitKey(1) & 0xFF == 27:   # ESC
        break

close()
cv2.destroyAllWindows()