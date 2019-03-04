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
# TODO: 2.
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

window = rg.TurtleWindow()

#Choose how many snowballs you want your snowman to have!
snowballs = 3

#initialize t1
t1 = rg.SimpleTurtle('circle')
t1.pen = rg.Pen('black', 3)
t1.speed = 20
r = (100/3)*snowballs
c = (-200/3)*snowballs

#create body of snowman
for k in range(snowballs):
    print(c)
    if k == 0:
        t1.pen_up()
        t1.go_to(rg.Point(0,c))
        t1.pen_down()
        t1.draw_circle(r)
        r = r - (20/3)*snowballs
        c = c + 2*r
    if k > 0 and k < (snowballs-1):
        t1.pen_up()
        t1.go_to(rg.Point(0,c))
        t1.draw_Arc(r, 45 + 10*(k-1))
        t1.pen_down()
        t1.draw_Arc(r, 270 - 20*(k-1))
        t1.pen_up()
        t1.draw_Arc(r,45 + 10*(k-1))
        r = r - 20
        c = c + 2*r
    if k == (snowballs - 1):
        t1.pen_up()
        t1.go_to(rg.Point(0, c))
        t1.draw_Arc(r, 45 + 10 * (k - 1))
        t1.pen_down()
        t1.draw_Arc(r, 270 - 20 * (k - 1))
        t1.pen_up()
        t1.draw_Arc(r, 45 + 10 * (k - 1))

#use t1 as right eye of snowman
t1.pen_up()
t1.go_to(rg.Point(r/2 , 2*c))

#redefine initials to draw buttons
c = (-200/3)*snowballs
r = (100/3)*snowballs

#initialize t2
t2 = rg.SimpleTurtle('circle')

t2 = rg.SimpleTurtle('circle')
t2.pen = rg.Pen('black', 2)
t2.speed = 20
rb = r/15

for k in range(2*snowballs):
    t2.pen_up()
    t2.go_to(rg.Point(0,c))
    t2.pen_down()
    t2.draw_circle(rb)
    c = c + r/4

window.close_on_mouse_click()
