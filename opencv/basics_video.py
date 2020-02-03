import cv2
import numpy as np
import time

# requires camera access approval!

capture = cv2.VideoCapture(0) #0-1st camera

frame_width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = capture.get(cv2.CAP_PROP_FPS)

print(f"FPS of capture {FPS}")


# Check if camera opened successfully
if capture.isOpened() == False:
    print("Error opening the camera")

while capture.isOpened():
    # Capture frame-by-frame from the camera
    ret, frame = capture.read()

    if ret:
        processing_start = time.time()

        # Display the captured frame:
        cv2.imshow('Input frame from the camera', frame)

        # Convert the frame captured from the camera to grayscale: 
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the grayscale frame:
        cv2.imshow('Grayscale input camera', gray_frame)
 
        frame_index = 0
        if cv2.waitKey(20) & 0xFF == ord('s'):
            cv2.imwrite(f"camera_frame_{frame_index}.png", frame)
            frame_index += 1

        # Press q on keyboard to exit the program
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break

        processing_end = time.time()
        FPS = 1 / (processing_end - processing_start)

        print(f"FPS {FPS}")

    # Break the loop
    else:
        break


# close sources
capture.release()
cv2.destroyAllWindows()