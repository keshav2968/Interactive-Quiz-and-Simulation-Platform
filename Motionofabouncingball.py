from vpython import *
#Web VPython 3.2
print("The following are the graphs based on the motion of a bouncing ball")

scene = canvas(align="left")
scene.width = 250
scene.height = 450

tmax = 10
graphpos = True
graphvel = True
grapherg = True
graphacc = True


cres = 1
grav = -10
g = vec(0,grav,0) 
m = 1


h0 = vec(0,-0.5,0)
ground = box(pos=h0, size=0.4*vec(1,0.1,1), color=color.white, opacity=0.5)




h = h0+vec(0,1,0)
v = vec(0,0,0)
a = sphere(pos=h, radius=0.04, color=color.red, opacity=1)


if graphpos:
  g1 = graph(scroll=True,align="right",width=480,height=150,ytitle="position",xmin=0,xmax=tmax)
  f1 = gcurve(graph=g1, interval=10, color=color.red) 
if graphvel:
  g2 = graph(scroll=True,align="right",width=480,height=150,ytitle="velocity",xmin=0,xmax=tmax)
  f2 = gcurve(graph=g2, interval=10, color=color.blue) 
if graphacc:
  g4 = graph(scroll=True,align="right",width=480,height=150,ytitle="acceleration",xmin=0,xmax=tmax)
  f4 = gcurve(graph=g4, interval=10, color=color.green) 

if grapherg:
  g3 = graph(scroll=True,align="right",width=480,height=150,xtitle="time",ytitle="energy",xmin=0,xmax=tmax)
  fp3 = gcurve(graph=g3, interval=10, color=color.red, label="PE")
  fk3 = gcurve(graph=g3, interval=10, color=color.blue, label="KE") 
  ft3 = gcurve(graph=g3, interval=10, color=color.black, label="Total") 

t = 0
dt = 0.0001
while t < tmax: 
  rate(1/dt)
  v += g*dt
  h += v*dt
  a.pos = h
  
  if a.pos.y < ground.pos.y + 0.1:
    grav = 100
  else:
    grav = 9.8

  if a.pos.y < ground.pos.y:
    v = cres*vec(0,mag(v),0)

  t += dt
  
  if graphpos:
    f1.plot(data=[t,h.y-ground.pos.y])
  
  if graphvel:
    f2.plot(data=[t,v.y])

  if graphacc:
    f4.plot(data=[t,grav])
  
  pe = m*(-g.y)*(h.y-ground.pos.y)
  ke = 0.5*m*v.y*v.y
  
  if grapherg:
    fp3.plot(data=[t,pe])
    fk3.plot(data=[t,ke])
    ft3.plot(data=[t,pe+ke])
