def dist(pi, pj):
   return ((pi[0] - pj[0])**2 +(pi[1] - pj[1])**2)**0.5

def sort(p):
    n = len(p)
    if(n == 1):
        return p, p
    
    nby2 = n // 2
    lx, ly = sort(p[:nby2])
    rx, ry = sort(p[nby2:])
    
    ix, jx, iy, jy = 0, 0, 0, 0
    px, py = [], []
    for k in range(n):
        if(jx >= len(rx) or (ix < len(lx) and lx[ix][0] < rx[jx][0])):
            px.append(lx[ix])
            ix += 1
        else:
            px.append(rx[jx])
            jx += 1
        if(jy >= len(ry) or (iy < len(ly) and ly[iy][1] < ry[jy][1])):
            py.append(ly[iy])
            iy += 1
        else:
            py.append(ry[jy])
            jy += 1        
    return px, py

def closestSplitPair(px, py, delta):
    n = len(px)
    ref = px[n // 2 - 1][0]
    
    section = []
    for pi in py:
        if pi[0] > ref - delta and pi[0] < ref + delta:
            section.append(pi)
    
    p3, q3 = None, None
    best = delta
    
    for i in range(len(section) - 1):
        for j in range(i + 1, min(len(section), i + 7)):
            dst = dist(section[i], section[j])
            if(dst <= best):
                p3, q3 = section[i], section[j]
                best = dst
    return p3, q3

def closestPair(px, py):
    n = len(px)
    if(n == 3):
        dist1 = dist(px[0], px[1])
        dist2 = dist(px[1], px[2])
        dist3 = dist(px[0], px[2])
        if(dist1 <= dist2 and dist1 <= dist3):
            return px[0], px[1]
        elif(dist2 <= dist1 and dist2 <= dist3):
            return px[1], px[2]
        else:
            return px[0], px[2]
    elif(n == 2):
        return px[0], px[1]
    
    
    nby2 = n // 2
    qx = px[:nby2]
    rx = px[nby2:]
    qy, ry = [], []
    
    for k in range(n):
 #       if(py[k] in qx):
        if(py[k][0] <= qx[-1][0]):
            qy.append(py[k])
        else:
            ry.append(py[k])
    
    p1, q1 = closestPair(qx, qy)
    p2, q2 = closestPair(rx, ry)
    dist1 = dist(p1, q1)
    dist2 = dist(p2, q2)
    delta = dist1 if dist1 <= dist2 else dist2
    p3, q3 = closestSplitPair(px, py, delta)
    if p3 is not None:
        return p3, q3
    elif dist1 <= dist2:
        return p1, q1
    else:
        return p2, q2

def bruteForceClosestPair(px):
    if(len(px) < 2):
        return None
    
    bestPair = px[0], px[1]
    bestDist = dist(px[0], px[1])
    
    for i in range(len(px) - 1):
        for j in range(i + 1, len(px)):
            dst = dist(px[i], px[j])
            if(dst <= bestDist):
                bestDist = dst
                bestPair = px[i], px[j]
    
    return bestPair

px, py = sort([[1,2],[4,4],[8,7],[2,3],[6,8],[10,20],[3,6],[5,5],[9,10],[11,11]])
print(closestPair(px, py))
print(bruteForceClosestPair(px))
