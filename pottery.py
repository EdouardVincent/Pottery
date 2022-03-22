import rhinoscriptsyntax as rs
import random

crv = []
cercles = []
intervales = 8

nb_lines = rs.GetInteger('nb lines',10)

for r in range(nb_lines) :
    x=r * 15
    y=0
    z=0
    crv.append(rs.AddCurve(((x,y,z),(x,y,z+20)),1))
    



for h in range(nb_lines) :
    rs.AddLoftSrf(cercles)
    cercles = []
    for x in range(intervales+1) :
        domain = rs.CurveDomain(crv[h])
        step = (domain[1] - domain[0]) / intervales
    
        plan = rs.CurvePerpFrame(crv[h],step * x)
        cercles.append(rs.AddCircle(plan,random.randint(1,3)))
        
rs.AddLoftSrf(cercles) #just for the last cylinder
cercles = []
            
