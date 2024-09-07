import cv2
import numpy as np

width = 480
height = 320
brightness = 100

web_vid = cv2.VideoCapture(0)
web_vid.set(3, width)  # Set width
web_vid.set(4, height) # Set height
web_vid.set(10, brightness) # Set brightnes

my_colors =[[0, 107, 0, 19, 255, 255],
            [133,56,0,159,156,255],
            [57,76,0,100,255,255]]

my_draw_color = [[51,153,255],
                 [255,0,255],
                 [0,255,0]]

my_points = []  #[x , y , my_colorId]


def find_color(img,my_colors,my_draw_color):
    img_HSV  = cv2.cvtColor(img , cv2.COLOR_BGR2HSV)
    count = 0
    new_points  = []

    for color in my_colors:
        lower = np.array(color[0:3])
        higher  = np.array(color[3:6])
        img_mask = cv2.inRange(img_HSV, lower , higher)
        x_point , y_points  = find_contour(img_mask)
        cv2.circle(img_copy , (x_point,y_points) , 10 , my_draw_color[count] , cv2.FILLED)
        if x_point != 0 and y_points != 0:
             new_points.append([x_point,y_points,count])
        count  = count + 1

    return new_points



def find_contour(mask_img):
    contour, hierarchy = cv2.findContours(mask_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0

    for cnt in contour:
        area = cv2.contourArea(cnt)
        if area > 200:
            #qcv2.drawContours(img_copy, cnt, -1, (255, 0, 0), 3)
            perimeter = cv2.arcLength(cnt, True)
            corner_points = cv2.approxPolyDP(cnt, 0.02 * perimeter, True)
            x, y, w, h = cv2.boundingRect(corner_points)

    # Optionally, handle the case where no contour met the area threshold
    if w == 0 and h == 0:
        # If no contour is found, return a default or handle the error
        return None, None

    return x + w // 2, y


def draw_on_canvas(my_points,my_draw_color):
    for point in my_points:
        cv2.circle(img_copy , (point[0],point[1]) , 10 , my_draw_color[point[2]] , cv2.FILLED)


while True:
    ret, img = web_vid.read()
    img_copy = img.copy()
    new_points  = find_color(img, my_colors , my_draw_color)

    if len(new_points) != 0:
        for newP in new_points:           
            my_points.append(newP)

    if len(my_points) != 0:
        draw_on_canvas(my_points ,my_draw_color)
    
    cv2.imshow('window_web_cam', img_copy)

    if cv2.waitKey(2) & 0xFF == ord('q'):  # Corrected logical check
        break

web_vid.release()
cv2.destroyAllWindows()
