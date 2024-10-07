#!/usr/bin/python3
"""A script to determine pascal's triangle for any number"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle of n rows.
    
    Args:
        n (int): The number of rows for Pascal's triangle.
        
    Returns:
        List[List[int]]: A list of lists representing the Pascal's triangle.
    """
    triangle = []

    # return (trianlgle if n <= 0)
    if n <= 0:
        return triangle
    for i in range(n):
        temp_list = []

        for j in range(i+1):
            if j == 0 or j == i:
                temp_list.append(1)
            else:
                temp_list.append(triangle[i-1][j-1] + triangle[i-1][j])
        triangle.append(temp_list)
    # print(triangle)
    return triangle