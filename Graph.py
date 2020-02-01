import random

def rand(size):
    points = [(i, random.uniform(0, 1), random.uniform(0, 1)) for i in range(size)]
    return points

def connect_points(node_matrix):
    for i in range(len(node_matrix)):
        for j in range(len(node_matrix)):
            if node_matrix[i] is not node_matrix[j]:
                slope = calculate_slope(node_matrix[i], node_matrix[j])
                print(slope)


def calculate_slope(x, y):
    return (y[2] - x[2]) / (y[1] - x[1])


p = rand(5)
for i in p:
    print(i)

connect_points(p)


