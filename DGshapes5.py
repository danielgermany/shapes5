from graphics import *

shapesWin = GraphWin("Shapes 5", 300, 300)
shapesWin.setCoords(0, 0, 600, 600)

bTri = Polygon(Point(10, 10), Point(50,100), Point(100,10))
bTri.setFill(color_rgb(30,30,230))
bTri.draw(shapesWin)

gSquare = Polygon(Point(10,590),Point(100,590),Point(100,500),Point(10,500))
gSquare.setFill(color_rgb(30,230,30))
gSquare.draw(shapesWin)

rRect = Polygon(Point(490,550),Point(590,550),Point(590,490),Point(490,490))
rRect.setFill(color_rgb(230,30,30))
rRect.draw(shapesWin)

pPentagon = Polygon(Point(490,10),Point(470,110),Point(520,150),Point(570,110),Point(550,10))
pPentagon.setFill(color_rgb(230,230,30))
pPentagon.draw(shapesWin)
