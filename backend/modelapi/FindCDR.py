import cv2
import numpy as np
from PIL import Image, ImageEnhance
import os

#TODO: use to take user_image dynamically
class FindCDRatio:
    def __init__(self):
        print("FIND CDR Class is been instanced")
    
    def calculateCDR(self, image_path:str):
    
        # resources_dir = os.path.join('resources')
        # merge_image_path = os.path.join(resources_dir, 'merge_oc.jpg')
        # image_colored_oc_image_path = os.path.join(resources_dir, 'image_colored_oc.jpg')

        # print('===========MergeImagePath======', merge_image_path)
        # print('===========MergeImagePathTYPE======', type(merge_image_path))
        user_image = cv2.imread(image_path)

        image = cv2.resize(user_image, (256,256), interpolation=cv2.INTER_AREA)

        orig = image.copy()

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)   

        gray = cv2.GaussianBlur(gray, (3, 3), 0) 

        #applying gaussian blur
        (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)

        cv2.circle(image, maxLoc, 80, (0, 0, 0), 2)
        disc = 3.14 * 80 * 80

        print('Area of Disc:'+str(disc))

        r,g,b = cv2.split(orig)

        kernel = np.ones((5,5), np.uint8) 
        img_dilation = cv2.dilate(g, kernel, iterations=1) 

        #stretching
        minmax_img = np.zeros((img_dilation.shape[0],img_dilation.shape[1]),dtype = 'uint8')

        # Loop over the image and apply Min-Max formulae
        for i in range(img_dilation.shape[0]):
            for j in range(img_dilation.shape[1]):
                minmax_img[i,j] = 255*(img_dilation[i,j]-np.min(img_dilation))/(np.max(img_dilation)-np.min(img_dilation))

        merge = cv2.merge((r,minmax_img,b))

        HSV_img = cv2.cvtColor(merge,cv2.COLOR_RGB2HSV)
        h,s,v = cv2.split(HSV_img)

        median = cv2.medianBlur(s,5)
        merge1 = cv2.merge((h,s,median))

        #cv2.imwrite('merge_oc.jpg',merge1)
        image_merge = Image.open('merge_oc.jpg')

        enh_col = ImageEnhance.Color(image_merge)
        image_colored_oc = enh_col.enhance(7)


        #cv2.imwrite('image_colored_oc.jpg', np.float32(image_colored_oc))
        image_c_oc = cv2.imread('image_colored_oc.jpg')


        lab = cv2.cvtColor(image_c_oc, cv2.COLOR_BGR2LAB)

        Z = lab.reshape((-1,3))
        Z = np.float32(Z)

        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

        K=2
        ret, label1, center1 = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
        center1 = np.uint8(center1)
        res1 = center1[label1.flatten()]
        output1 = res1.reshape((lab.shape))

        bilateral_filtered_image = cv2.bilateralFilter(output1, 5, 175, 175)
        edge_detected_image = cv2.Canny(bilateral_filtered_image, 75, 200)

        contours, _= cv2.findContours(edge_detected_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contour_list = []
        for contour in contours:
            approx = cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)
            area = cv2.contourArea(contour)
            if ((len(approx) > 8) & (area > 30) ):
                contour_list.append(contour)
        cv2.drawContours(image, contour_list,  -1, (255,0,0), 1)


        ellipse = cv2.fitEllipse(contour)
        cv2.ellipse(image,ellipse,(0,0,0),1,cv2.LINE_AA)
        (x, y), (MA, ma), angle = cv2.fitEllipse(contour)

        cuparea = (3.14/3) * MA * ma
        print('Area of cup:'+str(cuparea))
        cdr = cuparea / disc
        print('Cup to Disc Ratio:'+str(cdr))

        #cv2.imwrite('.', image)
