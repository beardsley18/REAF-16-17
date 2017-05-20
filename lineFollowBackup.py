#Sends commands to the arduino for thruster movement based on the points
#marking the corners of the line that are in the camera frame


#points is an array containing four arrays with x, y point values
# points = [ [x1,y1], [x2,y2], [x3, y3], [x4, y4] ]

#the x,y points should be taken so that there are only two distinct y values.

from math import *

def lineFollow(points):
    ymax = points[0][1]
    bottomPoints = []
    topPoints = []

    #find the largest y value
    for i in range(1, 4):
        if (points[i][1] > ymax):
            ymax = points[i][1]

    print(ymax)

    #place the points with the largest y value together as bottom corners
    #and place the points without this y value together as top corners
    for j in range(0,4):
        print(points[j])
        if (points[j][1] == ymax):
            bottomPoints.append(points[j])
        else:
            topPoints.append(points[j])


    if not bottomPoints:
        print("error empty bottom points list")
    else:
        bottomLeft = bottomPoints[0]
        bottomRight = bottomPoints[1]
    if not topPoints:
        print("error empty top points list")
    else:
        topLeft = topPoints[0]
        topRight = topPoints[1] 


    #check to make sure that right and left are correct
    if (topLeft[0] > topRight[0]):
        print("swapping top")
        #if incorrect, swap them
        temp = topRight
        topRight = topLeft
        topLeft = temp
    if (bottomLeft[0] > bottomRight[0]):
        print("swapping bottom")
        #if incorrect, swap them
        temp = bottomRight
        bottomRight = bottomLeft
        bottomLeft = temp

    print('top left : ')
    print(topLeft)
    print('top right : ')
    print(topRight)
    print('bottom left : ')
    print(bottomLeft)
    print('bottom right : ')
    print(bottomRight)



    #Now that points are sorted, determine what to do

    #Case where there is only one edge of the line in the frame
    #if this happens, either the right side points or the left side points
    #should be the corners of the camera frame
    
    xmax = 5 #width of the image
    #Case where line is on the left side of the frame
    if (topLeft[0] == 0) and (bottomLeft[0] == 0):
        print('turn left')
    #Case where line is on the right side of the frame
    elif (topRight[0] == xmax) and (bottomRight[0] == xmax):
        print('turn right')        
    
    #Case where all the corners are on the screen
    else:
        theta = degrees(atan((bottomLeft[1]-topLeft[1])/(topLeft[0] - bottomLeft[0])))
        print(theta)
        if (theta > 0):
            print('turn left')
        if (theta < 0):
            print('turn right')
        else:
            print('go straight')
