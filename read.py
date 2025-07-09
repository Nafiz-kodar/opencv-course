import cv2 as cv

# cat= cv.imread('/Volumes/Work/opencv-course/Resources/Photos/cat_large.jpg')
# cv.imshow('bigcat', cat)
# cv.waitKey(0)

capture=cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break 

capture.release()
cv.destroyAllWindows()