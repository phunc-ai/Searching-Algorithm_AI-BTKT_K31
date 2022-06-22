def make_convex_block(p1, p2):
    is_right = p2[1] > p1[1]
    is_below = p2[0] > p1[0]
    w = p2[1] - p1[1]
    h = p2[0] - p1[0]
    hor = abs(w) - abs(h)
    is_hor = hor >= 0

    # print(is_right, is_below, is_hor, hor, w, h)


    pts = []
    if is_right and is_below and is_hor:
        for i in range(1, hor + 1):
            x = p1[0]
            y = p1[1] + i
            pts.append([x, y])
        
        for j in range(1, h):
            x = p1[0] + j
            y = p1[1] + hor + j
            pts.append([x, y])
        

    if is_right and is_below and (not is_hor):
        for i in range(1, w + 1):
            x = p1[0] + i
            y = p1[1] + i
            pts.append([x, y])
        
        for j in range(1, abs(hor)):
            x = p1[0] + w + j
            y = p1[1] + w
            pts.append([x, y])


    if is_right and (not is_below) and is_hor:
        for i in range(1, abs(h) + 1):
            x = p1[0] - i
            y = p1[1] + i
            pts.append([x, y])
        
        for j in range(1, hor):
            x = p1[0] - abs(h)
            y = p1[1] + abs(h) + j
            pts.append([x, y])


    if is_right and (not is_below) and (not is_hor):
        for i in range(1, abs(hor) + 1):
            x = p1[0] - i
            y = p1[1]
            pts.append([x, y])
        
        for j in range(1, w):
            x = p1[0] - abs(hor) - j
            y = p1[1] + j
            pts.append([x, y])


    if (not is_right) and is_below and is_hor:
        for i in range(1, h + 1):
            x = p1[0] + i
            y = p1[1] - i
            pts.append([x, y])
        
        for j in range(1, abs(hor)):
            x = p1[0] + h
            y = p1[1] - h - j
            pts.append([x, y])


    if (not is_right) and is_below and (not is_hor):
        for i in range(1, abs(hor) + 1):
            x = p1[0] + i
            y = p1[1]
            pts.append([x, y])
        
        for j in range(1, abs(w)):
            x = p1[0] + abs(hor) + j
            y = p1[1] - j
            pts.append([x, y])


    if (not is_right) and (not is_below) and is_hor:
        for i in range(1, hor + 1):
            x = p1[0]
            y = p1[1] - i
            pts.append([x, y])
        
        for j in range(1, abs(h)):
            x = p1[0] - j
            y = p1[1] - hor - j
            pts.append([x, y])



    if (not is_right) and (not is_below) and (not is_hor):
        for i in range(1, abs(w) + 1):
            x = p1[0] - i
            y = p1[1] - i
            pts.append([x, y])
        
        for j in range(1, abs(hor)):
            x = p1[0] - abs(w) - j
            y = p1[1] - abs(w)
            pts.append([x, y])
        
    return pts


if __name__ == '__main__':
    p1 = [6, 6]
    p2 = [1, 3]
    pts = make_convex_block(p1, p2)
    print(pts)