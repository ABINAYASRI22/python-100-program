import math
class point():
            def__init__(self,a,b,c):
                     self.x=a
                     self.y=b
                     self.z=c
            def distancefromorigin(self):
                      return((self.x**2)+(self.y**2)+(self.z**2))**0.5
            def distance(self,point2):
                       xdiff=self.x-point2.x
                       ydiff=self.y-point2.y
                       zdiff=self.z-point2.z
                       dist=math.sqrt(xdiff**2+ydiff**2+zdiff**2)
                       return dist
        x1,y1,z1=(input("Enter the coordinates of a first point p1(x1,y1,z1):")).split()
        x1,y1,z1=[int(x1),int(y1),int(z1)]
        x2,y2,z2=(input("Enter the coordinates of a second point p2(x2,y2,z2):")).split()
        x2,y2,z2=[int(x2),int(y2),int(z2)]
        #p1 and p2 are objects of point class
        p1=point(x1,y1,z1)
        p2=point(x2,y2,z2)
        print('Distance from origin to p1:',p1.distancefromorigin())
        print('Distance from origin to p2:',p2.distancefromorigin())
        print('Distance from p1 to p2:',p1.distance(p2))
        
