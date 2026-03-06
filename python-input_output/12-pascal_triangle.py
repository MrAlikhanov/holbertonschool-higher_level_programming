#!/usr/bin/python3
"""Module for pascal_triangle function."""


def pascal_triangle(n):
    """Returns a list of lists of integers representing Pascal's triangle of n."""
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    return triangle
```

The logic mirrors how Pascal's triangle is built by hand:

- Every row starts and ends with `1`
- Each interior value is the sum of the two values directly above it (left and right) from the previous row: `triangle[i-1][j-1] + triangle[i-1][j]`
- Row `i` has `i+1` elements, so interior indices run from `1` to `i-1`
```
Row 0:  [1]
Row 1:  [1, 1]
Row 2:  [1, 2, 1]        2 = 1+1
Row 3:  [1, 3, 3, 1]     3=1+2, 3=2+1
Row 4:  [1, 4, 6, 4, 1]  4=1+3, 6=3+3, 4=3+1
