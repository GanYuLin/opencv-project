import cv2 as cv
import numpy as np
from skimage import io

def template_demo():
    tpl=io.imread("D:/Pycharm/Project/spider3/opencv-Project/data/土族刺绣2.jpg")
    target=io.imread("D:/Pycharm/Project/spider3/opencv-Project/data/土族刺绣1.jpg")

    # x,y=tpl.shape[:2]
    # tpl1 = cv.resize(tpl, (int(x*2.3),int(y*1.9)))
    cv.imshow("Template Image",tpl)

    cv.imshow("Target image",target)
    # method
    # methods=[cv.TM_SQDIFF_NORMED,cv.TM_SQDIFF,cv.TM_CCORR_NORMED,cv.TM_CCORR,cv.TM_CCOEFF_NORMED,cv.TM_CCOEFF]
    # methods=[cv.TM_SQDIFF_NORMED,cv.TM_CCORR_NORMED,cv.TM_CCOEFF_NORMED]
    methods=[cv.TM_SQDIFF,cv.TM_CCORR,cv.TM_CCOEFF]
    th,tw=tpl.shape[:2]
    for md in methods:
        print(md)
        result=cv.matchTemplate(target,tpl,md)
        min_val,max_val,min_loc,max_loc=cv.minMaxLoc(result)
        if(md==cv.TM_CCOEFF):
            tl=min_loc
        else:
            tl=max_loc
        br=(tl[0]+tw,tl[1]+th)
        cv.rectangle(target,tl,br,(0,0,255),2)
        cv.imshow("match-"+np.str(md),target)


print("--------Output-------")
# src=cv.imread("D:/Pycharm/Project\spider3/opencv-Project/data/土族刺绣1.jpg")
# cv.namedWindow("Input image",cv.WINDOW_AUTOSIZE)
# cv.imshow("Input image",src)
template_demo()
cv.waitKey(0)

cv.destroyAllWindows()







