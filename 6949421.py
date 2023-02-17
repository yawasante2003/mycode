import numpy as np

#span
L = 12
#load intensity
w = 10

# (a)
# At the first end, x=0
x=0
#bending moment
M = (w*(-6*x**2 + 6*L*x-L**2))/12
#shear force
V = w*(L/2 - x)

a= 'The bending moment at x=0 is '
b= 'The shear force at x=0 is '

print('(a.i)', a , str(M))  
print(b + str(V))

# At the other end. x=L=12
x=12
M = (w*(-6*x**2 + 6*L*x-L**2))/12
V = w*(L/2 - x)


a= 'The bending moment at x=L is '
b= 'The shear force at x=L is '

print('(a.ii)' , a + str(M))  
print(b + str(V))
 

# (b)
#When the bending moment is zero, we get an expression x**2 - L*x + L**2/6 = 0
L= 12
#from the expression 
a = 1
b = -L
c = L**2/6
#Using the Almighty formula the two roots are;
discriminant = b**2 - 4*a*c
root_1b = (-b + np.sqrt(discriminant))/2*a
root_2b = (-b - np.sqrt(discriminant))/2*a

a = root_1b
b = root_2b
q= '(b) The points of contra-flexure are'

print(q , str(a), 'and', str(b))

# (c)

#When the shear force is zero, x = L/2

x = L/2
a = '(c) The point at which the shear force, V=0 is'
print(a, str(x))

# (d)

r = 0
t = 0.01
s = L + t
x = np.arange(r,s,t) 
M = (w*(-6*x**2 + 6*L*x-L**2))/12
print()
print('(d) The bending moment at each step in the array is {0}'.format(M))

# (e)
V = w*(L/2 - x)
print()
print('(e) The shear force for each step along the span is {}'.format(V))

# (f)
#Let the absolute value of the bending moment array be Ma
#Let the minimum Ma be m_Ma

Ma = abs(M)
m_Ma = min(Ma)
 
#When the bending moment is m_Ma, the expression is x**2 - Lx + (L**2/6)+(2*m_Ma)/w = 0

#from the above expression 
a = 1
b = -L
c = (L**2/6)+(2*m_Ma)/w
#Using the Quadratic formula, the roots are;
discriminant = b**2 - 4*a*c
root_1f = (-b + np.sqrt(discriminant))/2*a
root_2f = (-b - np.sqrt(discriminant))/2*a
 
u = root_1f
v = root_2f
n = '(f) The points along L at which the absolute values of the bending moment array is minimum are'

print(n, str(u), str(v))   

# (g)

#Let the relative errors be r_e

r_e1 = ((root_1b - root_1f)/root_1b*100) 
r_e2 = ((root_2f - root_2b)/root_2f*100)

error1 = "{:.0%}".format(r_e1)
error2 = "{:.0%}".format(r_e2)
k = '(g) The relative errors between estimated points of contra-flexure are'   

print(k, str(error1),'and', str(error2))

# (h)

#Let the maximum bending moment be max_M and the minimum bending moment be min_M

#for the maximum
max_M = max(M)
 
#When the bending moment is max_M, the expression is x**2 - Lx + (L**2/6)+(2*max_M)/w = 0
a = 1
b = -L
c = (L**2/6)+(2*max_M)/w

#Using the Quadratic formula, the two roots are;
discriminant = b**2 - 4*a*c
root_1 = (-b + np.sqrt(discriminant))/2*a
root_2 = (-b - np.sqrt(discriminant))/2*a

o = root_1
p = root_2
z= '(h.i) The points at which the maximum bending moment occur are'

print(z, o, 'and', p) 

#for the minimum
min_M = min(M)
 
#When the bending moment is min_M, we get an expression x**2 - Lx + (L**2//6)+(2*min_M)/w = 0
a = 1
b = -L
c = (L**2//6)+(2*min_M)/w

#Using the Quadratic formula, the roots are;
discriminant = b**2 - 4*a*c
root_1 = (-b - np.sqrt(discriminant))/2*a
root_2 = (-b + np.sqrt(discriminant))/2*a

e = root_1
f = root_2
g = '(h.ii) The points at which the minimum bending moment occur are'

print(g, str(e), 'and', str(f))


