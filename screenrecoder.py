import cv2
import numpy  as np
from PIL import ImageGrab 

def screenRecoder():
    fourcc = cv2.VideoWriter_fourcc(*'XVID') # or use other codecs like MJPG, XVID etc.
    out = cv2.VideoWriter('output.avi', fourcc, 10.0, (854, 480))# you can change the resolution here
    
    while True:
        img = ImageGrab.grab() # this is a simple bound
        img_np = np.array(img)
        frame = cv2.cvtcolor(im_np, cv2.COLOR_BAYER_BG2BGR)
        cv2.imshow("Screen Recoder", frame)
        out.write(frame)
        
        if cv2.waitKey(1) ==27:
            break
        
    out.release()
    cv2.destroyAllWindows()
    
screenRecoder()

