from handgesture.gesture_control import update, close, get_controls
import cv2

while True:
    frame = update()

    move, shoot = get_controls()

    print("Move:", move, " Shoot:", shoot)

    if frame is not None:
        cv2.imshow("Gesture Test", frame)

    if cv2.waitKey(1) == 27:   # ESC
        break

close()
cv2.destroyAllWindows()