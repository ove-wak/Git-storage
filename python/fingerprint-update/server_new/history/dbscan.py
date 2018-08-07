import numpy as np


def dbscan(data, e, min_pts, func_d):
    length = len(data)
    category = np.zeros(length)
    visited = np.zeros(length)
    current_class = 1
    for i in range(length):
        if visited[i] == 0:
            if search_same(data, e, min_pts, length, category, int(current_class), i, visited, func_d):
                # print(current_class)
                current_class = current_class + 1
    return category


def search_same(data, e, min_pts, length, category, current_class, index, visited, func_d):
    if visited[index] == 0:
        visited[index] = 1
        close_pts = []
        for i in range(length):
            distance = func_d(data[index], data[i])
            if distance <= e:
                close_pts.append(i)
        if len(close_pts) >= min_pts:
            for j in range(len(close_pts)):
                category[close_pts[j]] = current_class
                search_same(data, e, min_pts, length, category, current_class, close_pts[j], visited, func_d)
            return True
    return False



