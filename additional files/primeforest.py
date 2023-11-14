import tkinter, json, math, time

with open('primes_100k', 'r') as file:
    prime_list = json.load(file)

frame = 0
line_width = 2
running = True
maxX = 2048
maxY = 1024


root_window = tkinter.Tk()
canvas = tkinter.Canvas(root_window, width=maxX, height=maxY, bg='red')
canvas.pack()


def get_color(color_dec_tuple):
    colorstring = str(hex(color_dec_tuple[0]*1000000 + color_dec_tuple[1]*1000 + color_dec_tuple[2]))[2:]
    colorstring = '0'*(9-len(colorstring)) + colorstring
    return '#' + colorstring


def update_pos(pos, i):
    global prime_list, orientation
    orientation += 72 + prime_list[i] % 36
    length = prime_list[i+1]-prime_list[i]
    stopx = pos[0] + length * math.sin(orientation)
    stopy = pos[1] + length * math.cos(orientation)
    return (stopx, stopy)


while running:
    #global orientation, prime_list, maxX, maxY
    pos = (0, 0)
    orientation = 0
    for i in range(len(prime_list)-1):
        #Koordinaten
        startx = pos[0]
        starty = pos[1]
        color = get_color((255, 0, 255))
        pos = update_pos(pos, i)
        stopx = pos[0]
        stopy = pos[1]
        #Linie gezeichnet
        canvas.create_line(startx, starty, stopx, stopy, fill=color, width=line_width)

        if pos[0] > maxX:
            pos = (0, pos[1])
        elif pos[0] < 0:
            pos = (maxX, pos[1])
        if pos[1] > maxY:
            pos = (pos[0], 0)
        elif pos[1] < 0:
            pos = (pos[0], maxY)
    frame += 1
    print(frame)
    root_window.update()

print('leg started')
#root_window.mainloop()
print('leg ended')


#root_window.mainloop()
