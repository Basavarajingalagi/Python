import cv2
 
video = cv2.VideoCapture("To Ace LIMITLESS Ideas of Governance. - Ms. Rohini Sindhuri - TEDxGlobalAcademy.mp4");
     
fps = video.get(cv2.CAP_PROP_FPS)
#print ("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))
     
video.release();

total_frames_per_minute = 60*fps
#print('total frames per minute',total_frames_per_minute)


def saveimage(fps,minutes):
    cap = cv2.VideoCapture('To Ace LIMITLESS Ideas of Governance. - Ms. Rohini Sindhuri - TEDxGlobalAcademy.mp4')
    count = 0

    while cap.isOpened():
        ret, frame = cap.read()

        if ret:
            cv2.imwrite('frame{0:f}.jpg'.format(count), frame)
            count += minutes*total_frames_per_minute
            cap.set(1, count)
        else:
            cap.release()
            break


minutes = int(input('enter after how many minutes u want to save the frames:\n'))
saveimage(fps,minutes)
