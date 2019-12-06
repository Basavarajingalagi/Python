import cv2
video = cv2.VideoCapture(0);     

fps = video.get(cv2.CAP_PROP_FPS)
print ("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))

def savecamimage(fps,sec):
    cap = cv2.VideoCapture(0)
    count = 0

    while(True):
        ret, frame = cap.read()
        cv2.imshow('camera',frame)

        if ret:
            cv2.imwrite('frame{0:f}.jpg'.format(count), frame)
            count += sec*fps
            cap.set(1, count)
            
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

sec = int(input('after how many seconds u want to capture snap'))
savecamimage(fps,sec)
