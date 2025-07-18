#فخارصادقي علي

import cv2 as cv
import argparse
import numpy as np
import pandas as pd
    
df = pd.read_csv("colors.csv" , encoding = 'latin1' , header = None)

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--format')
parser.add_argument('-i', '--file')
args = parser.parse_args()

name = s = ""

def mouse(event, x, y, flags, param):
        global img, s, name

        r = int(img[y,x,2])
        g = int(img[y,x,1])
        b = int(img[y,x,0])
                
        if event == cv.EVENT_LBUTTONDBLCLK :
                img1[:,:,0] = b
                img1[:,:,1] = g
                img1[:,:,2] = r
                
                m = ( b + g + r)  / 3
                mini = min(255 - m , m)
                        
                if mini == 255 -m:
                        color = 0
                else:
                        color = 255
                                                
                s = 'R = ' + str(r) + '  G = ' + str(g) + '  B = ' + str(b) 
                cv.putText(img1, s , (75, 50),cv.FONT_HERSHEY_DUPLEX , 0.5, (color,color,color), 1)
                
                o=255
                for i in range(0,865):
                        df1 = list(df.iloc[i])[0]
                        df1 = df1.split(',')
                        r1 = int(df1[3])
                        g1 = int(df1[4])
                        b1 = int(df1[5][:-1])
                        m1 = ((r - r1) ** 2 + (g - g1) ** 2 + (b - b1) ** 2) ** 0.5

                        if m1 < o:
                                o = m1
                                name = df1[1][1:-1]
                cv.putText(img1, name , (120, 100),cv.FONT_HERSHEY_DUPLEX , 0.5, (color,color,color), 1)

        if event == cv.EVENT_RBUTTONDOWN:
                print(s , name)

        if args.format == 'pic':
                cv.imshow('img' , img)
                
        cv.imshow('img1', img1)
        
if args.format == 'pic':
        img = cv.imread(args.file)
        img = cv.resize(img, dsize=(800, 600))
        img1 = np.zeros((200,400, 3), np.uint8)

        while (1):
            cv.imshow('img' , img)
            cv.setMouseCallback('img' , mouse)
            
            if cv.waitKey(1) & 0xFF == 27:
                    break
                
if args.format == 'vid':
        cap = cv.VideoCapture(args.file)
        img1 = np.zeros((200,400, 3), np.uint8)

        while (cap.isOpened()):
                ret, img = cap.read()
                
                if ret==True :
                        (w, h, r) = img.shape
                        cv.imshow('img' , img)
                        cv.setMouseCallback('img' , mouse)

                        if cv.waitKey(50) & 0xFF == 27:
                              break

                        if cv.waitKey(50) & 0xFF == ord('a'):
                              cv.waitKey()
                else:
                        break

        cap.release()

cv.destroyAllWindows()
