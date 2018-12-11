# Menu for the A* search python program

### How to run the program

* For single version python installed, use ```python a_star.py -m map_file_path -s output_file_path```

* For parallel versions python installed, use ```python3 a_star.py -m map_file_path -s output_file_path```

### How to build the map

1. The ground should be represented by using ```.```

2. The obstacle should be represented by using ```#```

**Note that the map should be a rectangle.**

### Enter point and exit point

The enter point would be the **left top**, the exit point would be the **right bottom**.

### How to read the solution

In the solution map, the enter point would be mark as **A**, and the exit point would be marked as **Z**. The direction will be marked with **<, >, v, ^**, and it would mark the path from the exit to the entry point.
