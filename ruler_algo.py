def drawline(tick_len, label=''):
    tick='-'*tick_len
    print(tick, label)

def interval(center_len):
    if center_len>0:
        interval(center_len-1)
        drawline(center_len)
        interval(center_len-1)

def draw_ruler(inches,length):
    drawline(length, '0')
    for j in range(1,inches+1):
        interval(length-1)
        drawline(length,str(j))

draw_ruler(4,3)
