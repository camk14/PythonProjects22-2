from graphics import *

def lab_05(win):
    # your code here
    txt1 = Text(Point(80,10),"There are 10 shapes in the file.")
    txt2 = Text(Point(98,30),"Which one do you want to draw first?")
    input = Entry(Point(215,30),5)                      #input area here
    txt1.draw(win)                                      #these all actually draw in the window
    txt2.draw(win)
    input.draw(win)
    win.setBackground("sky blue")
    win.getMouse()

    shapenumber = int(input.getText())
    #print(shapenumber)
    infile = open("shapes.txt","r")                     #open file to read

    for i in range(shapenumber-1):
        infile.readline()                       #read line on file ---> build into loop
    data = infile.readline()                    #how to read/draw the data once received ---> 128/128/128 300 200, 330 230, 350 202, 330 240
    data = data.replace(",","")
                                                #convert to drawing a polygon
    list = data.split()
    print(list)
    RGB = list[0].split('/')                                  #poly.setfill(RGB)
    points = list[1:len(list)]                      #poly = Polygon(data)  use print to show the list
    p = []
    for i in range(0,len(points),2):
        x = int(points[i])
        y = int(points[i + 1])
        point = Point(x, y)
        p.append(point)

    poly = Polygon(p)
    poly.setFill(color_rgb(int(RGB[0]),int(RGB[1]),int(RGB[2])))

    #print(RGB)


    poly.draw(win)

def main():
    win = GraphWin("Shapes!", 500, 500)
    while True:
        lab_05(win)


main()