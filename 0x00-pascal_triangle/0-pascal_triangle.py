#!/usr/bin/python3
def pascal_triangle(n):
    """
    Generate Pascal's triangle up to n rows.
    """
    # If n is less than or equal to 0, return an empty list
    if n <= 0:
        return []
    
    # Initialize the triangle with the first row
    triangle = [[1]]
    
    # Generate rows 1 to n-1 (since row 0 is already initialized)
    for i in range(1, n):
        # Start the row with 1
        row = [1]
        
        # Each element (except the first and last) is the sum of the two elements above
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        
        # End the row with 1
        row.append(1)
        
        # Add the row to the triangle
        triangle.append(row)
    
    return triangle

# Test using the provided 0-main.py
def print_triangle(triangle):
    """
    Print the triangle in a formatted way.
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

if __name__ == "__main__":
    # Test the pascal_triangle function with n = 5
    print_triangle(pascal_triangle(5))
