import turtle

def draw_hexagon(t, side_length):
    for _ in range(6):
        t.forward(side_length)
        t.right(60)

def draw_honeycomb(rows, cols):
    screen = turtle.Screen()
    t = turtle.Turtle()
    t.speed(0)
    
    side_length = 20
    hex_height = side_length * 3**0.5 / 2  

    for row in range(rows):
        for col in range(cols):
            
            x = col * 1.5 * side_length
            y = row * hex_height * 2
            
            if col % 2 == 1:
                y += hex_height
            
            t.penup()
            t.goto(x, y)
            t.pendown()
            draw_hexagon(t, side_length)
    
    screen.mainloop()
rows=int(input("Enter the no of rows"))
cols=int(input("Enter the no of cols"))
draw_honeycomb(rows, cols)  
