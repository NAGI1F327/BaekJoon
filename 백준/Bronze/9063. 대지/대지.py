def min_rectangle_area():
    N = int(input())

    coords = []
    for i in range(N):
        x, y = map(int, input().split())
        coords.append((x, y))
    
    min_x = coords[0][0]
    max_x = coords[0][0]
    min_y = coords[0][1]
    max_y = coords[0][1]
    
    for i in range(1, N):
        x, y = coords[i]
    
        if x < min_x:
            min_x = x
        if x > max_x:
            max_x = x
    
        if y < min_y:
            min_y = y
        if y > max_y:
            max_y = y
    
    area = (max_x - min_x) * (max_y - min_y)
    return area
    
print(min_rectangle_area())