# -*- coding: utf-8 -*-
import cv2

if __name__ == '__main__':
    print('Func_called - main')
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FPS,30)
    while(True):
        ret, img_color = cap.read()
        if ret == False:
            continue
        img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
        try:
            img_dif = cv2.absdiff(img_gray ,img_temp)
            cv2.imshow("Dif", img_dif)
        except:
            pass
        '''
        From the second cycle, 
        images are printed by calculating the difference from the previous picture.
        '''
        img_edges = cv2.Canny(img_color,90,150,3)
        '''
        Can detect edge of img
        '''
        #cv2.imshow("Color", img_color)
        #cv2.imshow("Gray", img_gray)
        cv2.imshow("Edge", img_edges)

        img_temp = img_gray
        #save previous img
        if(cv2.waitKey(1)&0xFF == 27):
            break
            #if press "ESC", this code will be end
    cap.release()
    cv2.destroyAllWindows()
else:
    print('Func_called - imported')
    
