import math

def rotation_matrix_x(angle):
   r = math.radians(angle)
   return [
       [1,0,0],
       [0,math.cos(r),-math.sin(r)],
       [0,math.sin(r),math.cos(r)]
   ]


def rotation_matrix_y(angle):
   r = math.radians(angle)
   return [
       [math.cos(r),0,math.sin(r)],
       [0,1,0],
       [-math.sin(r),0,math.cos(r)]
   ]
