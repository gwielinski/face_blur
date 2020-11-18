import cv2
import dlib
import numpy as np
from hogBlur import face_blur


def main():
    cap = cv2.VideoCapture('../../media/groupVid.mp4')
    face_detect = dlib.get_frontal_face_detector()

    if cap.isOpened() == 0:
        print("Error opening the video file")

    while cap.isOpened():
        ret, frame = cap.read()

        if np.shape(frame) == ():
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.resize(gray, (0, 0), fx=0.25, fy=0.25)

        if ret == 1:
            if cap.get(1) % 10 == 0:
                print("---------------------------------------")
                print("Frame:", cap.get(1))
                faces = face_detect(gray, 1)
                face_blur(frame, faces)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        else:
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
