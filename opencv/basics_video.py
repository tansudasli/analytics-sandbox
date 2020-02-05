import cv2
import numpy as np
import time

# requires camera access approval!

capture = cv2.VideoCapture(0) #0-1st camera

# get some parameter values of active camera
def decodeFourcc(fourcc):
    return "".join([chr((int(fourcc) >> 8 * i) & 0xFF) for i in range(4)])

def getCameraInfo():
    frame_width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
    frame_height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
    fps = capture.get(cv2.CAP_PROP_FPS)
    fourcc = capture.get(cv2.CAP_PROP_FOURCC)
    buffsize = capture.get(cv2.CAP_PROP_BUFFERSIZE)

    print(f"fourcc {fourcc}")  
    print(f"FPS of capture {fps}")
    print(f"Buffer size {buffsize}")

    return (frame_width, frame_height, fps)


frame_width, frame_height, fps = getCameraInfo()

# Check if camera opened successfully
if capture.isOpened() == False:
    print("Error opening the camera")

out = cv2.VideoWriter('out.avi', \
                      cv2.VideoWriter_fourcc('X', 'V', 'I', 'D'), \
                      int(fps), \
                      (int(frame_width), int(frame_height)), \
                      True)

while capture.isOpened():
    # Capture frame-by-frame from the camera
    ret, frame = capture.read()

    if ret:
        processing_start = time.time()

        # Display the captured frame:
        cv2.imshow('Input frame from the camera', frame)

        frame_index = 0

        processing_end = time.time()
        FPS = 1 / (processing_end - processing_start)
      
        # menu
        key = cv2.waitKey(20) & 0xFF

        if key == ord('q'):       # quit
            break
        elif key == ord('i'):    # info
            print(f"FPS {FPS}")
        elif key == ord('s'):    # save as image
            print('saving...')
            cv2.imwrite(f"camera_frame_{frame_index}.png", frame)
            frame_index += 1
        elif key == ord('r'):    # record as video
            print('recording...')
            out.write(frame)
    # Break the loop
    else:
        break


# close sources
capture.release()
out.release()
cv2.destroyAllWindows()