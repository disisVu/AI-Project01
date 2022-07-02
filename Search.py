def checkValidBFS(m, mainmap):
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
    queue = []
    visited = []
    valid =""
    visited.append(start)
    queue.append(start)
    while queue:
        m = queue.pop(0)
        print(m, end = " ")
        if m == goal:
            break
        for i in ["L", "R", "U", "D"]:
            valid = checkValidBFS(m,mainmap)
            
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
                
                
        
    
    
    
    
    
    
if __name__ == "__main__":
    mainmap = [2,2]
    start = [0,0]
    goal = [2,2]
    BFS(mainmap,start,goal)