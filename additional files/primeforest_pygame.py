import pygame, json, math, time

with open('primes_100k', 'r') as file:
    prime_list = json.load(file)

prime_list = prime_list[:(len(prime_list)//2)]
frame = 0
line_width = 1
running = True
maxX = 500
maxY = 500
offset_amplitude = 4


pygame.init()
window = pygame.display.set_mode([maxX, maxY])
pygame.display.set_caption('treeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee')



def update_pos(pos, i):
    global prime_list, orientation
    orientation += 72 + prime_list[i] % 36
    length = prime_list[i+1]-prime_list[i]
    stopx = pos[0] + length * math.sin(orientation)
    stopy = pos[1] + length * math.cos(orientation)
    return (stopx, stopy)


while running:
    pos = (0, 0)
    #movement off the 'forest'
    offsety = offset_amplitude * math.sin(frame+1)
    offsetx = offset_amplitude * math.cos(frame*.78)
    orientation = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    window.fill((255, 255, 255))
    for i in range(len(prime_list)-1):
        old_pos_shift = (pos[0] + offsetx, pos[1] + offsety)
        color = (0, i/len(prime_list)*255, 0)
        pos = update_pos(pos, i)
        pos_shift = (pos[0]+offsetx, pos[1]+offsety)
        pygame.draw.line(window, color, pos_shift, old_pos_shift, line_width)
        if pos[0] > maxX + offset_amplitude:
            pos = (-offset_amplitude, pos[1])
        elif pos[0] < -offset_amplitude:
            pos = (maxX + offset_amplitude, pos[1])
        if pos[1] > maxY + offset_amplitude:
            pos = (pos[0], -offset_amplitude)
        elif pos[1] < -offset_amplitude:
            pos = (pos[0], maxY + offset_amplitude)
    pygame.display.flip()
    frame += 1

