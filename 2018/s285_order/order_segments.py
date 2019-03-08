def order_segments(unord):
    # first sort the segments
    p0, p1 = unord.pop()
    ord = [(p0, p1)]
    while unord:
        for pair in unord:
            if p0 in pair or p1 in pair:
                ord.append(pair)
                unord.remove(pair)
                p0, p1 = pair[0], pair[1]
                break
        else:  # break a possible infinite while
            print("malformed edge sequence")
            break
##    # now fix each segment's internal vertex order
##    unord = ord
##    p0, p1 = unord.pop(0)
##    if p1 != unord[0][0]:
##        p1, p0 = p0, p1
##    ord = [(p0, p1)]
##    for pair in unord:
##        if p1 == pair[0]:
##            p0, p1 = pair[0], pair[1]        
##        else:
##            p0, p1 = pair[1], pair[0]
##    ord.append((p0, p1))
    # if you want the vertex points only :)
    p0, p1 = ord.pop(0)
    if p1 != ord[0][0]:
        p1, p0 = p0, p1
    points = [p0]
    for pair in ord:
        if p1 == pair[0]:
            p0, p1 = pair[0], pair[1]        
        else:
            p0, p1 = pair[1], pair[0]
        points.append(p0)
        
    return points
