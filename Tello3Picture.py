#
# --- (c) 02/2020 f41ardu
#
# Tello cam using opencv proof of concept
#
#

# import opencv 4.2.0
import cv2

telloVideo = cv2.VideoCapture("udp://@0.0.0.0:11111")


# wait for frame
ret = False
# scale down
scale = 3

while(True):
    # Capture frame-by-framestreamon
    ret, frame = telloVideo.read()
    if(ret):
    # Our operations on the frame come here
        height , width , layers =  frame.shape
        new_h=int(height/scale)
        new_w=int(width/scale)
        resize = cv2.resize(frame, (new_w, new_h)) # <- resize for improved performance
        # Display the resulting frame
        cv2.imshow('Tello',resize)
        
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("test.jpg",resize) # writes image test.bmp to disk
        print("Take Picture")
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
telloVideo.release()
cv2.destroyAllWindows()