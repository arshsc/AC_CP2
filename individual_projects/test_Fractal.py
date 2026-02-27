import turtle

def draw_tri(length, recursion):
    if recursion == 1:
        return 1
    else:
        for i in range(3):
            for i in range(3):
                turtle.forward(length/2)
                draw_tri(length/2, recursion-1)
                turtle.forward(length/2)
                turtle.left(120)
            draw_tri(length/2, recursion-1)


        
        
turtle.tracer(0,0)
draw_tri(250, 4)
turtle.update()
turtle.done()
