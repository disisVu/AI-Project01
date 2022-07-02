def checkValid(m, mainmap):
    valid = ""
    if m[0] - 1 < 0:
        valid += "L"
    if m[0] + 1 > mainmap[0]:
        valid += "R"
    if m[1] - 1 < 0:
        valid += "U"
    if m[1] + 1 > mainmap[1]:
        valid += "D"
    return valid

def BFS(mainmap, start, goal):
    returnpath = []
    queue = []
    visited = []
    valid =""
    visited.append(start)
    queue.append(start)
    while queue:
        m = queue.pop(0)
        returnpath.append(m)
        if m == goal:
            break
        for i in ["L", "R", "U", "D"]:
            valid = checkValid(m,mainmap)
            
            if i == "L" and i not in valid:
                n = [m[0] - 1, m[1]]
                if n not in visited:
                    visited.append(n)
                    queue.append(n)
            if i == "R" and i not in valid:
                n =[m[0] + 1, m[1]]
                if n not in visited:
                    visited.append(n)
                    queue.append(n)
            if i == "U" and i not in valid:
                n = [m[0], m[1] - 1]
                if n not in visited:
                    visited.append(n)
                    queue.append(n)
            if i == "D" and i not in valid:
                n = [m[0], m[1] + 1]
                if n not in visited:
                    visited.append(n)
                    queue.append(n)
    return returnpath
                
def UCS(mainmap, start, goal):
    returnpath = []
    queue = []
    visited = []
    valid =""
    visited.append(start)
    queue.append(start)
    gn = [0]
    visitedgn = [0]
    while queue:
        index_min = gn.index(min(gn))
        mgn = gn.pop(index_min)
        mq = queue.pop(index_min)
        returnpath.append(mq)
        if mq == goal:
            break
        for i in ["L", "R", "U", "D"]:
            valid = checkValid(mq,mainmap)
            if i == "L" and i not in valid:
                n = [mq[0] - 1, mq[1]]
                gn.append(mgn + 1)
                visitedgn.append(mgn + 1)
                if n not in visited:
                    visited.append(n)
                    queue.append(n)
                else:
                    index = 0
                    for i in range(len(visited) - 1):
                        if visited[i][0] == n[0] and visited[i][1] == n[1] and visitedgn[index] > gn[index]:
                            gn[index] = visitedgn[index]
                            break
                        index += 1
            if i == "R" and i not in valid:
                n = [mq[0] + 1, mq[1]]
                gn.append(mgn + 1)
                gn.append(mgn + 1)
                visitedgn.append(mgn + 1)
                if n not in visited:
                    visited.append(n)
                    queue.append(n)
                else:
                    index = 0
                    for i in range(len(visited) - 1):
                        if visited[i][0] == n[0] and visited[i][1] == n[1] and visitedgn[index] > gn[index]:
                            gn[index] = visitedgn[index]
                            break
                        index += 1
            if i == "U" and i not in valid:
                n = [mq[0], mq[1] - 1]
                gn.append(mgn + 1)
                visitedgn.append(mgn + 1)
                if n not in visited:
                    visited.append(n)
                    queue.append(n)
                else:
                    index = 0
                    for i in range(len(visited) - 1):
                        if visited[i][0] == n[0] and visited[i][1] == n[1] and visitedgn[index] > gn[index]:
                            gn[index] = visitedgn[index]
                            break
                        index += 1
            if i == "D" and i not in valid:
                n = [mq[0], mq[1] + 1]
                gn.append(mgn + 1)
                visitedgn.append(mgn + 1)
                if n not in visited:
                    visited.append(n)
                    queue.append(n)
                else:
                    index = 0
                    for i in range(len(visited) - 1):
                        if visited[i][0] == n[0] and visited[i][1] == n[1] and visitedgn[index] > gn[index]:
                            gn[index] = visitedgn[index]
                            break
                        index += 1
    return returnpath
        
    
    
    
    
    
    
if __name__ == "__main__":
    mainmap = [2,3]
    start = [0,0]
    goal = [1,2]
    path = UCS(mainmap,start,goal)
    print(path)
    