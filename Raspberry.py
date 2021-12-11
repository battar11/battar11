import cv2
import time
import numpy as np

frameWidth = 320
frameHeight = 240
cap = cv2.VideoCapture(0)
cap1 = cv2.VideoCapture(2)
cap2 = cv2.VideoCapture(4)
cap3 = cv2.VideoCapture(6)

cap.set(3,frameWidth)
cap.set(4,frameHeight)

cap1.set(3,frameWidth)
cap1.set(4,frameHeight)

cap2.set(3,frameWidth)
cap2.set(4,frameHeight)

cap3.set(3,frameWidth)
cap3.set(4,frameHeight)
#GET CONTOURS AND NUMBER OF CARS FOR TRAFFIC ONE
def getContours(img, imgContours):
    _,contours,hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    global Counter
    Counter = 0
    for cnt in contours:

        area = cv2.contourArea(cnt)

        if area > 2000:
            Counter = Counter + 1
            cv2.drawContours(imgContours, contours,-1,(255,0,255), 7)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            x , y , w, h = cv2.boundingRect(approx)

            cv2.rectangle(imgContours,(x,y), (x+w, y +h),(0,255,0),5)
    cv2.putText(imgContours, "Num Cars: " + str(Counter), (70, 320), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 0),
                        2)
    #print(int(Counter))

    return img

#GET CONTOURS AND NUMBER OF CARS FOR TRAFFIC TWO 
def getContours1(img1, imgContours1):
    _, contours1, hierarchy1 = cv2.findContours(img1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    global Counter1
    Counter1 = 0
    for cnt in contours1:

        area1 = cv2.contourArea(cnt)

        if area1 > 2000:
            Counter1 = Counter1 + 1
            cv2.drawContours(imgContours1, contours1,-1,(255,0,255), 7)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            x , y , w, h = cv2.boundingRect(approx)

            cv2.rectangle(imgContours1,(x,y), (x+w, y +h),(0,255,0),5)
    cv2.putText(imgContours1, "Num Cars: " + str(Counter1), (70, 320), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 0),
                        2)
    #print(int(Counter))

    return img1
#GET CONTOURS AND NUMBER OF CARS FOR TRAFFIC THREE
def getContours2(img2, imgContours2):
    _, contours2, hierarchy2 = cv2.findContours(img2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    global Counter2
    Counter2 = 0
    for cnt in contours2:

        area2 = cv2.contourArea(cnt)

        if area2 > 2000:
            Counter2 = Counter2 + 1
            cv2.drawContours(imgContours2, contours2,-1,(255,0,255), 7)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            x , y , w, h = cv2.boundingRect(approx)

            cv2.rectangle(imgContours2,(x,y), (x+w, y +h),(0,255,0),5)
    cv2.putText(imgContours2, "Num Cars: " + str(Counter2), (70, 320), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 0),
                        2)
    #print(int(Counter))

    return img2

#GET CONTOURS AND NUMBER OF CARS FOR TRAFFIC FOUR 
def getContours3(img3, imgContours3):
    _, contours3, hierarchy3 = cv2.findContours(img3, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    global Counter3
    Counter3 = 0
    for cnt in contours3:

        area3 = cv2.contourArea(cnt)

        if area3 > 2000:
            Counter3 = Counter3 + 1
            cv2.drawContours(imgContours3, contours3,-1,(255,0,255), 7)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            x , y , w, h = cv2.boundingRect(approx)

            cv2.rectangle(imgContours3,(x,y), (x+w, y +h),(0,255,0),5)
    cv2.putText(imgContours3, "Num Cars: " + str(Counter3), (70, 320), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 0),
                        2)
    #print(int(Counter))

    return img3



def countdown(numberOfSecTrafficOne):
    while numberOfSecTrafficOne:
        mins, secs = divmod(numberOfSecTrafficOne, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        
        time.sleep(1)
        numberOfSecTrafficOne -= 1
        if numberOfSecTrafficOne >0:
            print("Green light for traffic One ")

    print('TRAFFIC ONE IS RED!!')

def countdown1(numberOfSecTrafficTwo):
    while numberOfSecTrafficTwo:
        mins, secs = divmod(numberOfSecTrafficTwo, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        time.sleep(1)
        numberOfSecTrafficTwo -= 1
        if numberOfSecTrafficTwo >0:
            print("Green light for traffic two ")

    print('Traffic TWO IS RED  ')
# input time in seconds

def countdown2(numberOfSecTrafficThree):
    while numberOfSecTrafficThree:
        mins, secs = divmod(numberOfSecTrafficThree, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
       
        time.sleep(1)
        numberOfSecTrafficThree -= 1
        if numberOfSecTrafficThree >0:
            print("Green light for traffic Three ")

    print('Traffic THREE IS RED')


def countdown3(numberOfSecTrafficFour):
    while numberOfSecTrafficFour:
        mins, secs = divmod(numberOfSecTrafficFour, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        
        time.sleep(1)
        numberOfSecTrafficFour -= 1
        if numberOfSecTrafficFour >0:
            print("Green light for traffic Four ")

    print('Traffic Four IS RED')
while True:
    # SIGNAL ONE
    success, img = cap.read()
    imgContours = img.copy()
    imgBlur = cv2.GaussianBlur(img, (7,7),1)
    imgGray = cv2.cvtColor(imgBlur, cv2.COLOR_BGR2GRAY)
    laplacian = cv2.Laplacian(img, cv2.CV_64F).var()
    #print(laplacian)

    # SIGNAL TWO
    success1, img1 = cap1.read()
    imgContours1 = img1.copy()
    imgBlur1 = cv2.GaussianBlur(img1, (7, 7), 1)
    imgGray1 = cv2.cvtColor(imgBlur1, cv2.COLOR_BGR2GRAY)
    laplacian1 = cv2.Laplacian(img1, cv2.CV_64F).var()

    # Traffic FOUR
    success2, img2 = cap2.read()
    imgContours2 = img2.copy()
    imgBlur2 = cv2.GaussianBlur(img2, (7, 7), 1)
    imgGray2 = cv2.cvtColor(imgBlur2, cv2.COLOR_BGR2GRAY)
    laplacian2 = cv2.Laplacian(img2, cv2.CV_64F).var()

    # Traffic FOUR
    success3, img3 = cap3.read()
    imgContours3 = img3.copy()
    imgBlur3 = cv2.GaussianBlur(img3, (7, 7), 1)
    imgGray3 = cv2.cvtColor(imgBlur3, cv2.COLOR_BGR2GRAY)
    laplacian3 = cv2.Laplacian(img3, cv2.CV_64F).var()

    if laplacian and laplacian1 and laplacian2 and laplacian3 > 0:
        kerrnel = np.ones((5, 5))

        imgCanny = cv2.Canny(imgGray,51, 51)
        imgDil = cv2.dilate(imgCanny, kerrnel, iterations=1)
        getContours(imgDil,imgContours)

        imgCanny1 = cv2.Canny(imgGray1,51, 51)
        imgDil1 = cv2.dilate(imgCanny1, kerrnel, iterations=1)
        getContours1(imgDil1, imgContours1)

        imgCanny2 = cv2.Canny(imgGray2, 51, 51)
        imgDil2 = cv2.dilate(imgCanny2, kerrnel, iterations=1)
        getContours2(imgDil2, imgContours2)

        imgCanny3 = cv2.Canny(imgGray3, 51, 51)
        imgDil3 = cv2.dilate(imgCanny3, kerrnel, iterations=1)
        getContours3(imgDil3, imgContours3)
        sum = Counter+Counter1+Counter2+Counter3
        timer_traffic_one = Counter/sum
        timer_traffic_two = Counter1/sum
        timer_traffic_three = Counter2/sum
        timer_traffic_four = Counter3/sum
        numberOfSecTrafficOne = int(timer_traffic_one*60)
        numberOfSecTrafficTwo = int(timer_traffic_two*60)
        numberOfSecTrafficThree = int(timer_traffic_three*60)
        numberOfSecTrafficFour = int(timer_traffic_four*60)
        countdown(numberOfSecTrafficOne)
        countdown1(numberOfSecTrafficTwo)
        countdown2(numberOfSecTrafficThree)
        countdown3(numberOfSecTrafficFour)

      

        cv2.imshow("Signal Four", imgContours3)
        cv2.imshow("Signal Three", imgContours2)
        cv2.imshow("Signal Two", imgContours1)
        cv2.imshow("Signal One", imgContours)
        #cv2.imshow("Dilate", imgDil)
        #cv2.imshow("Canny", imgCanny)
        #cv2.imshow("img", img)
        #cv2.imshow("Gray", imgGray)
        #cv2.imshow("Blur", imgBlur)

    else:
        #HERE WE CAN RUN THE SEQUENTIAL WAY IN ORDER IF THERE IS BAD WEATHER OR NOT ENOUGH LIGHT
        print("Normal mode is applied")
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# function call


   
