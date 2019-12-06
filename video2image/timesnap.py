import cv2
import time

def displaycam(num):    
    cap = cv2.VideoCapture(0)
    count = 0
    start_time = time.time()
    while(True):
        ret, frame = cap.read()
        #show = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        cv2.imshow('camera',frame)

        if time.time() - start_time >= num: 
            img_name = "opencv_frame_{}.png".format(count)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(count))
            start_time = time.time()
            count += 1
    
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

num = int(input('enter the seconds after which u want take snap'))
displaycam(num)
