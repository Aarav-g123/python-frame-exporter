import cv2

# Open Video File
video_capture = cv2.VideoCapture("Video.mp4")

# Check if video file opened successfully
if not video_capture.isOpened():
    print("Error: Video file not found or cannot be opened.")
    print("Ensure that the Video file is named Video.mp4 and is in the same folder as the python script")
    exit()

# Frame counter
i = 0

while True:
    ret, frame = video_capture.read()

    if ret:
        i += 1
        img_number = str(i).zfill(5)
        name = './img/frame_' + str(img_number) + '.png'  # Use '.png' extension
        print('Creating ' + name)

        # Writing the extracted images
        cv2.imwrite(name, frame)
    else:
        break

video_capture.release()
cv2.destroyAllWindows()
