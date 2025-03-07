import cv2
import numpy as np
import matplotlib.pyplot as plt
def make_coordinates(image,line_parameters):
    slope,intercept=line_parameters
    y1=image.shape[0] #height of the image(bottom)
    y2=int(y1*(3/5))
    x1=int((y1-intercept)/slope) #calc x coordinates
    x2=int((y2-intercept)/slope)
    return np.array([x1,y1,x2,y2])

def average_of_slope_intercept(image,lines): #average of slope and intercept for left and right
    left_fit=[]
    right_fit=[]
    for line in lines:
        x1,y1,x2,y2=line.reshape(4)
        parameters=np.polyfit((x1,x2),(y1,y2),1)#determine slope and intercept
        slope=parameters[0]
        intercept=parameters[1]
        if slope <0:
            left_fit.append((slope,intercept))
        else:
            right_fit.append((slope,intercept))
    left_average=np.average(left_fit,axis=0)#averge of all value at left fit
    right_average=np.average(right_fit,axis=0)#average of all val at rght fit
    left_line=make_coordinates(image,left_average)
    right_line=make_coordinates(image,right_average)
    return np.array([left_line,right_line])
def canny(image):  #for canny edge detection
    gray=cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    blur=cv2.GaussianBlur(gray,(5,5),0)
    canny=cv2.Canny(blur,50,150)
    return canny

def display_lines(image,lines): #displaying lines
    line_image=np.zeros_like(image)
    if lines is not None:
        for x1,y1,x2,y2 in lines:
            cv2.line(line_image,(x1,y1),(x2,y2),(255,0,0),10)#blue
    return line_image

def region_of_interest(image):
    height=image.shape[0]
    polygons=np.array([ #array of polygons
    [(200,height),(1100,height),(550,250)]
    ])
    mask=np.zeros_like(image)
    cv2.fillPoly(mask,polygons,255)
    masked_image=cv2.bitwise_and(image,mask)#to only show region of interest
    return masked_image


image=cv2.imread('test_image.jpg')
lane_image=np.copy(image)
canny_image=canny(lane_image)
cropped_image=region_of_interest(canny_image)
lines=cv2.HoughLinesP(cropped_image,1,np.pi/180,100,minLineLength=40,maxLineGap=5)
averaged_lines=average_of_slope_intercept(lane_image,lines)
line_image=display_lines(lane_image,averaged_lines)
combo_image=cv2.addWeighted(lane_image,0.8,line_image,1,1)#combine the images
cv2.imshow("result",combo_image)
cv2.waitKey(0)
