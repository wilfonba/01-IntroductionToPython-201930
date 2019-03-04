"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Ben Wilfong.
"""
########################################################################
# Done: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# Done: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################

import rosegraphics as rg
import math

window = rg.TurtleWindow()

################################################################
# DO: Choose how many snowballs you want your snowman to have!#
snowballs = 3                                                  #
################################################################

#initialize t1
t1 = rg.SimpleTurtle('circle')
t1.pen = rg.Pen('black', 3)
t1.speed = 20
r = int((100/3)*snowballs)
c = int((-200/3)*snowballs)

#create body of snowman
for k in range(snowballs):
    if k == 0:
        #drawing the first snowball
        t1.pen_up()
        t1.go_to(rg.Point(0,c))
        t1.pen_down()
        t1.draw_circle(r)
        r = r - 20
        c = c + 2*r
    if k > 0:
        #calculating start and end angles of each arc for
        #snowballs after the first one
        R = r + 20
        D = 2*r - 20
        d = ((D**2 + r**2 - R**2)/(2*D))
        theta = math.degrees(math.acos(d/r))
        print(r, R, D, d, theta)

        #drawing the snowballs
        t1.pen_up()
        t1.go_to(rg.Point(0,c))
        t1.draw_Arc(r, theta)
        t1.pen_down()
        t1.draw_Arc(r, (360 - 2*theta))
        t1.pen_up()
        t1.draw_Arc(r,theta)
        r = r - 20
        c = c + 2*r

r = r + 20
#use t1 as right eye of snowman
t1.pen_up()
t1.go_to(rg.Point((r)/2 , c))

#redefine initials to draw buttons
c2 = (-200/3)*snowballs
r2 = (100/3)*snowballs

#initialize t2
t2 = rg.SimpleTurtle('circle')
t2.pen = rg.Pen('black', 2)
t2.speed = 20
rb = r2/15

#draw buttons on snowman
buttons = 6

if snowballs <= 2:
    buttons = 3

#draw buttons
for d in range(buttons):
    t2.pen_up()
    t2.go_to(rg.Point(0,c2/2))
    t2.pen_down()
    t2.draw_circle(rb)
    c2 = c2 + (snowballs*(r2))/4

# #make second eye with t2
t2.pen_up()
t2.go_to(rg.Point(-r/2, c))

#initialize t3
t3 = rg.SimpleTurtle('triangle')
t3.pen_up()
t3.speed = 20

#make nose using t3
t3.go_to(rg.Point(0, c - r/2))

window.close_on_mouse_click()
