import math as m

def vertical_matrix(matrix):
    matrix_temp = []
    for i in range(0, len(matrix)):
        matrix_temp.append(matrix[::-1][i])
    return matrix_temp

def checkValid(m,matrix):
    matrix_temp = vertical_matrix(matrix)
    valid = ""
    if m[0] - 1 <= 0 or matrix_temp[m[1]][m[0] - 1] != 0:
        valid += "L"
    if m[0] + 1 >= len(matrix[0]) - 1 or matrix_temp[m[1]][m[0] + 1] != 0:
        valid += "R"
    if m[1] - 1 <= 0 or matrix_temp[m[1] - 1][m[0]] != 0:
        valid += "U"
    if m[1] + 1 >= len(matrix) - 1 or matrix_temp[m[1] + 1][m[0]] != 0:
        valid += "D"
    return valid

def BFS(start, goal,matrix):
    returnPath = []
    queue = []
    visited = []
    valid =""
    visited.append(start)
    queue.append(start)
    while queue:
        m = queue.pop(0)
        returnPath.append(m)
        if m == goal:
            break
        for i in ["L", "R", "U", "D"]:
            valid = checkValid(m,matrix)
            
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
    return returnPath
                
def UCS(start, goal, matrix):
    returnPath = []
    frontier = []
    visited = []
    valid =""
    visited.append(start)
    frontier.append(start)
    gn = [0]
    visitedgn = [0]
    while frontier:
        index_min = gn.index(min(gn))
        mgn = gn.pop(index_min)
        mq = frontier.pop(index_min)
        returnPath.append(mq)
        if mq == goal:
            break
        for i in ["L", "R", "U", "D"]:
            valid = checkValid(mq,matrix)
            if i == "L" and i not in valid:
                n = [mq[0] - 1, mq[1]]
                gn.append(mgn + 1)
                visitedgn.append(mgn + 1)
                if n not in visited:
                    visited.append(n)
                    frontier.append(n)
                else:
                    for i in range(len(visited) - 1):
                        if visited[i][0] == n[0] and visited[i][1] == n[1] and visitedgn[i] > mgn + 1:
                            for j in len(frontier) - 1:
                                if n == frontier[j]:
                                    gn[j] = mgn + 1
                                    break
                                    break
            if i == "R" and i not in valid:
                n = [mq[0] + 1, mq[1]]
                gn.append(mgn + 1)
                visitedgn.append(mgn + 1)
                if n not in visited:
                    visited.append(n)
                    frontier.append(n)
                else:
                    for i in range(len(visited) - 1):
                        if visited[i][0] == n[0] and visited[i][1] == n[1] and visitedgn[i] > mgn + 1:
                            for j in len(frontier) - 1:
                                if n == frontier[j]:
                                    gn[j] = mgn + 1
                                    break
                                    break
            if i == "U" and i not in valid:
                n = [mq[0], mq[1] - 1]
                gn.append(mgn + 1)
                visitedgn.append(mgn + 1)
                if n not in visited:
                    visited.append(n)
                    frontier.append(n)
                else:
                    for i in range(len(visited) - 1):
                        if visited[i][0] == n[0] and visited[i][1] == n[1] and visitedgn[i] > mgn + 1:
                            for j in len(frontier) - 1:
                                if n == frontier[j]:
                                    gn[j] = mgn + 1
                                    break
                                    break
            if i == "D" and i not in valid:
                n = [mq[0], mq[1] + 1]
                gn.append(mgn + 1)
                visitedgn.append(mgn + 1)
                if n not in visited:
                    visited.append(n)
                    frontier.append(n)
                else:
                    for i in range(len(visited) - 1):
                        if visited[i][0] == n[0] and visited[i][1] == n[1] and visitedgn[i] > mgn + 1:
                            for j in len(frontier) - 1:
                                if n == frontier[j]:
                                    gn[j] = mgn + 1
                                    break
                                    break
    return returnPath
        
def IDS(start, goal,matrix, limit_depth):
    returnPath = []
    stack = []
    visited = []
    valid =""
    visited.append(start)
    stack.append(start)
    depthNode = [0]
    while stack:
        m = stack.pop()
        returnPath.append(m)
        if m == goal:
            break
        depth = depthNode.pop()
        if depth < limit_depth:
            for i in ["L", "R", "U", "D"]:
                valid = checkValid(m,matrix)
                
                if i == "L" and i not in valid:
                    n = [m[0] - 1, m[1]]
                    if n not in visited:
                        visited.append(n)
                        stack.append(n)
                        depthNode.append(depth + 1)
                if i == "R" and i not in valid:
                    n =[m[0] + 1, m[1]]
                    if n not in visited:
                        visited.append(n)
                        stack.append(n)
                        depthNode.append(depth + 1)
                if i == "U" and i not in valid:
                    n = [m[0], m[1] - 1]
                    if n not in visited:
                        visited.append(n)
                        stack.append(n)
                        depthNode.append(depth + 1)
                if i == "D" and i not in valid:
                    n = [m[0], m[1] + 1]
                    if n not in visited:
                        visited.append(n)
                        stack.append(n)
                        depthNode.append(depth + 1)
        else:
            break
    return returnPath
    
def GBFS(start, goal, matrix):
    returnPath = []
    frontier = []
    visited = []
    valid =""
    visited.append(start)
    frontier.append(start)
    hn = [m.sqrt((goal[1] - start[1])**2 + (goal[0] - start[0])**2)]
    while frontier:
        index_min = hn.index(min(hn))
        mhn = hn.pop(index_min)
        mq = frontier.pop(index_min)
        returnPath.append(mq)
        if mq == goal:
            break
        for i in ["L", "R", "U", "D"]:
            valid = checkValid(mq,matrix)
            if i == "L" and i not in valid:
                n = [mq[0] - 1, mq[1]]
                if n not in visited:
                    visited.append(n)
                    frontier.append(n)
                    hn.append(m.sqrt((goal[1] - n[1])**2 + (goal[0] - n[0])**2))
            if i == "R" and i not in valid:
                n = [mq[0] + 1, mq[1]]
                if n not in visited:
                    visited.append(n)
                    frontier.append(n)
                    hn.append(m.sqrt((goal[1] - n[1])**2 + (goal[0] - n[0])**2))
            if i == "U" and i not in valid:
                n = [mq[0], mq[1] - 1]
                if n not in visited:
                    visited.append(n)
                    frontier.append(n)
                    hn.append(m.sqrt((goal[1] - n[1])**2 + (goal[0] - n[0])**2))
            if i == "D" and i not in valid:
                n = [mq[0], mq[1] + 1]
                if n not in visited:
                    visited.append(n)
                    frontier.append(n)
                    hn.append(m.sqrt((goal[1] - n[1])**2 + (goal[0] - n[0])**2))
    return returnPath
    
def A_star(start, goal, matrix):
    returnPath = []
    frontier = []
    visited = []
    valid =""
    gn = [0]
    visited.append(start)
    frontier.append(start)
    fn = [m.sqrt((goal[1] - start[1])**2 + (goal[0] - start[0])**2) + gn[0]]
    visitedfn = [m.sqrt((goal[1] - start[1])**2 + (goal[0] - start[0])**2) + gn[0]]
    while frontier:
        print(gn)
        print(fn)
        print(frontier)
        index_min = fn.index(min(fn))
        fn.pop(index_min)
        mgn = gn.pop(index_min)
        mq = frontier.pop(index_min)
        returnPath.append(mq)
        if mq == goal:
            break
        for i in ["L", "R", "U", "D"]:
            valid = checkValid(mq,matrix)
            if i == "L" and i not in valid:
                n = [mq[0] - 1, mq[1]]
                gn.append(mgn + 1)
                if n not in visited:
                    visited.append(n)
                    frontier.append(n)
                    fn.append(m.sqrt((goal[1] - n[1])**2 + (goal[0] - n[0])**2) + gn[-1])
                    visitedfn.append(m.sqrt((goal[1] - n[1])**2 + (goal[0] - n[0])**2) + gn[-1])
                else:
                    for i in range(len(visited) - 1):
                        if visited[i][0] == n[0] and visited[i][1] == n[1] and visitedfn[i] > (m.sqrt((goal[1] - n[1])**2 + (goal[0] - n[0])**2) + (mgn + 1)):
                            for j in len(frontier) - 1:
                                if n == frontier[j]:
                                    fn[j] = (m.sqrt((goal[1] - n[1])**2 + (goal[0] - n[0])**2) + (mgn + 1))
                                    gn[j] = gn[-1]
                                    gn.pop(-1)
                                    break
                                    break
                        elif visited[i][0] == n[0] and visited[i][1] == n[1] and visitedfn[i] <= (m.sqrt((goal[1] - n[1])**2 + (goal[0] - n[0])**2) + (mgn + 1)):
                            gn.pop(-1)
            if i == "R" and i not in valid:
                n = [mq[0] + 1, mq[1]]
                gn.append(mgn + 1)
                if n not in visited:
                    visited.append(n)
                    frontier.append(n)
                    fn.append(m.sqrt((goal[1] - n[1])**2 + (goal[0] - n[0])**2) + gn[-1])
                    visitedfn.append(m.sqrt((goal[1] - n[1])**2 + (goal[0] - n[0])**2) + gn[-1])
                else:
                    for i in range(len(visited) - 1):
                        if visited[i][0] == n[0] and visited[i][1] == n[1] and visitedfn[i] > (m.sqrt((goal[1] - n[1])**2 + (goal[0] - n[0])**2) + (mgn + 1)):
                            for j in len(frontier) - 1:
                                if n == frontier[j]:
                                    fn[j] = (m.sqrt((goal[1] - n[1])**2 + (goal[0] - n[0])**2) + (mgn + 1))
                                    gn[j] = gn[-1]
                                    gn.pop(-1)
                                    break
                                    break
                        elif visited[i][0] == n[0] and visited[i][1] == n[1] and visitedfn[i] <= (m.sqrt((goal[1] - n[1])**2 + (goal[0] - n[0])**2) + (mgn + 1)):
                            gn.pop(-1)
            if i == "U" and i not in valid:
                n = [mq[0], mq[1] - 1]
                gn.append(mgn + 1)
                if n not in visited:
                    visited.append(n)
                    frontier.append(n)
                    fn.append(m.sqrt((goal[1] - n[1])**2 + (goal[0] - n[0])**2) + gn[-1])
                    visitedfn.append(m.sqrt((goal[1] - n[1])**2 + (goal[0] - n[0])**2) + gn[-1])
                else:
                    for i in range(len(visited) - 1):
                        if visited[i][0] == n[0] and visited[i][1] == n[1] and visitedfn[i] > (m.sqrt((goal[1] - n[1])**2 + (goal[0] - n[0])**2) + (mgn + 1)):
                            for j in len(frontier) - 1:
                                if n == frontier[j]:
                                    fn[j] = (m.sqrt((goal[1] - n[1])**2 + (goal[0] - n[0])**2) + (mgn + 1))
                                    gn[j] = gn[-1]
                                    gn.pop(-1)
                                    break
                                    break
                        elif visited[i][0] == n[0] and visited[i][1] == n[1] and visitedfn[i] <= (m.sqrt((goal[1] - n[1])**2 + (goal[0] - n[0])**2) + (mgn + 1)):
                            gn.pop(-1)
            if i == "D" and i not in valid:
                n = [mq[0], mq[1] + 1]
                gn.append(mgn + 1)
                if n not in visited:
                    visited.append(n)
                    frontier.append(n)
                    fn.append(m.sqrt((goal[1] - n[1])**2 + (goal[0] - n[0])**2) + gn[-1])
                    visitedfn.append(m.sqrt((goal[1] - n[1])**2 + (goal[0] - n[0])**2) + gn[-1])
                else:
                    for i in range(len(visited) - 1):
                        if visited[i][0] == n[0] and visited[i][1] == n[1] and visitedfn[i] > (m.sqrt((goal[1] - n[1])**2 + (goal[0] - n[0])**2) + (mgn + 1)):
                            for j in len(frontier) - 1:
                                if n == frontier[j]:
                                    fn[j] = (m.sqrt((goal[1] - n[1])**2 + (goal[0] - n[0])**2) + (mgn + 1))
                                    gn[j] = gn[-1]
                                    gn.pop(-1)
                                    break
                                    break
                        elif visited[i][0] == n[0] and visited[i][1] == n[1] and visitedfn[i] <= (m.sqrt((goal[1] - n[1])**2 + (goal[0] - n[0])**2) + (mgn + 1)):
                            gn.pop(-1) 
    return returnPath   
    
def RealReturnedPath(start, goal, path):
    pathReturn = []
    curr = goal
    path_temp = path[::-1]
    for i in path_temp:
        if curr[0] == i[0] - 1 and curr[1] == i[1] or curr[0] == i[0] + 1 and curr[1] == i[1] or curr[1] == i[1] - 1 and curr[0] == i[0]or curr[1] == i[1] + 1 and curr[0] == i[0] or curr == i:
            curr = i
            pathReturn.append(curr)
    return pathReturn[::-1]
        
        
if __name__ == "__main__":
    start = [1,1]
    goal = [1,5]
    matrix = [[0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0],
              [0, 1, 1, 0, 0, 0],
              [0, 1, 0, 0, 0, 0],
              [0, 0, 0, 1, 0, 0], 
              [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0]]
    expandedNodeBFS = BFS(start, goal, matrix)
    pathBFS = RealReturnedPath(start,goal,expandedNodeBFS)
    print("BFS Expanded Node = " , expandedNodeBFS)
    print("BFS Returned Path = " , pathBFS)
    expandedNodeUCS = UCS(start, goal, matrix)
    pathUCS = RealReturnedPath(start,goal,expandedNodeUCS)
    print("\nUCS Expanded Node = " , expandedNodeUCS)
    print("UCS Returned Path = " , pathUCS)
    expandedNodeIDS = IDS(start, goal, matrix,4)
    pathIDS = RealReturnedPath(start,goal,expandedNodeIDS)
    print("\nIDS Expanded Node = " , expandedNodeIDS)
    if len(pathIDS) > 0:
        print("IDS Returned Path = " , pathIDS)
    else:
        print("Goal not found in IDS. \nAdvice: increase limit depth")
    expandedNodeGBFS = GBFS(start, goal, matrix)
    pathGBFS = RealReturnedPath(start,goal,expandedNodeGBFS)
    print("\nGBFS Expanded Node = " , expandedNodeGBFS)
    print("GBFS Returned Path = " , pathGBFS)
    expandedNodeA_star = A_star(start, goal, matrix)
    pathA_star = RealReturnedPath(start,goal,expandedNodeA_star)
    print("\nA* Expanded Node = " , expandedNodeA_star)
    print("A* Returned Path = " , pathA_star)