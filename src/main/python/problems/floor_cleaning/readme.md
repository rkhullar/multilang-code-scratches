## Overview
The floor plan for a building is represented via 2D matrix of character cells. Each cell can be either clean `.`, dirty
`*`, or be blocked `#`. What is the minimal number of passes required for a robot to clean the floor?

### Example 1
#### input
```python
['.#.*', '..#.']
```

#### Visual
|   | # |   | x |
|---|---|---|---|
|   |   | # |   |

#### Output
```python
1
```

### Example 2
#### input
```python
['*#..', '####', '.**.']
```

#### Visual
| x | # |   |   |
|---|---|---|---|
| # | # | # | # |
|   | x | x |   |

#### Output
```python
2
```

### Links
- https://youtu.be/OyaHANapsh0?si=W5dhymNTWLHCy4mI
