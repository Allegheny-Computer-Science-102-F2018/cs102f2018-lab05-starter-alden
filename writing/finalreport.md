# Final Report

## Date: 1 Dec 2018
## Group Names: Haeley Griffin, Xingbang Liu, Jordan Wilson, Sweta Rauniyar

### Introduction
In the field of discrete structures, graph theory is a significant concept that involves separate objects that are related to each other. A graph acts as a visual representation where we start with our initial components and figure out pathways to arrive at the final destination. The prominent thing about graphs is that it is not just confined to the world mathematicians or scientists but to people from all walks of life and this is what sets it apart from everything else and links it to the sole purpose of involving in the world of Computer Science: to make people's lives as better and efficient as possible. With visual aid, the relationship between the objects that are vertices and edges in graph theory can help understand the concept in a very efficient manner. The elegant diagrammatic representation and set up provides a framework to deal with a large set of problems, a key concept in the field of Computer Science. With the aim to reduce the time consumption while solving a problem like finding the shortest path, we decided to explore different algorithms and eventually finding the best one for our proposed problem.



### Algorithms
We decided to analyze and compare the different kinds of algorithms including Breadth-First Search, Depth-First Search, Greedy Search,, and A* Search Algorithm. The motive of our project was to find the shortest path and hence comparing them based on their functioning and eventually the drawbacks gave us a keen idea about which would be the best option for us. We researched in deeper for each of the respective algorithm to understand them in a descriptive manner. Studying the Big-O Notation for each of these algorithms gave us a better idea of the functioning of these algorithms.

Table 1. The Big-O Notation for different Algorithms

|      | Breadth-First Search | Depth-First Search | A*     |Greedy|
|------|----------------------|--------------------|--------|------|
| Time | O(b^d + 1)           | O(b^m)             | O(b^d) | n/a  |


Here, 'b' is the branching factor, 'd' is the depth of the shallowest solution, and 'm' is the maximum depth of the search tree.

#### Breadth-First Search
Breadth-First Search Algorithm is one of the widely used traversal technique for searching through the algorithm. In this algorithm, we start with the source node, also called the root node or the tree node. There are nodes connected to the source node, known as the neighbor nodes. These neighbor nodes are explored and then we move on to the next level of the neighbor nodes, further repeating the process all over again until we get to the end of the graph. What's happening in this algorithm is that we move through the entire graph to get to our destination and we do find the shortest path. However, since we are bound to traverse through the entire graph, this process consumes a lot of time and uses a lot of memory space. Hence, we decided that this was not a reliable option for us to work with for our project.

#### Depth-First Search
Depth-First Search is a recursive algorithm. This searching algorithm works by traversing through each node until it reach an end point and then has to back track up the branch until it reaches a node that is not marked as visited, it will then repeat this until it goes through the whole set of nodes. This algorithm can also be implemented as a stack. You select a node that will become the starting node and then all of the other nodes go into the stack. Then you pick the top node which you mark as visited. You then keep completing this till you go through the whole stack. If you do not mark the node as visited than it could create an infinite loop. There are disadvantages to this searching algorithm though.One of those is that it may go down the first branch forever. Another drawback would be that there is no guarantee for a minimum solution. The last drawback is that it may not even find solution .at all. With these draw back this is not the most efficient algorithm.  After drawing these conclusions about depth-first we wanted to continue in our search for the most efficient searching algorithm.

#### Greedy Search

A greedy algorithm is a unique type of algorithm we researched while working on this project. This algorithm is unique because for starters it isn't an actual algorithm at all. It is a type of technique used to run through possible situations at choose what it deems as the best. A greedy algorithm will always pick the highest value in a situation. Also, a greedy algorithm is quite easy to use. When you are on a time-crunch, it is a good and easy way to simplify a problem to come up with a solution. A downside to making greedy algorithm are that they don’t always focus on the entirety of what you are trying to figure out. Greedy algorithms will always choose what is best in a situation but this is not always efficient. With this issue, it is much harder to find and figure out problems that may be inside the code. It is also important to note that most greedy algorithms are not actually correct, they are just a way of simplifying a problem. The solution a greedy algorithm may come up with is not always correct. The greedy algorithm just chooses what it thinks is best, not actually what is best. As we can see, this algorithm may not be the best algorithm when it comes to problem solving.

#### A* Algorithm

A* Search Algorithm is a smart algorithm. To search through a grid the algorithm follows these steps. First it will select the node according to the 'f' value, this is the parameter equal to the sum of the 'g' and 'h' parameter. The 'g' parameter is the cost of the movement to move from starting node to a given node on the grid, follow a path generated to get there. The 'h' parameter is the estimated movement cost to move from the current node to the final node on the grid. The 'h' parameter id often referred to as the heuristic. This is the educated guess. There are generally three approximation heuristics to calculate h, 1) Manhattan Distance, 2) Diagonal Distance, and 3) Euclidean Distance. For our A* program we just used Manhattan Distance because we just wanted to calculate the four way heuristic and the other two calculate the eight way. Manhattan Distance is the sum of absolute values of difference in the goal's x and y coordinates and the current nodes coordinates. When doing research on this algorithm we also found that the time complexity for this search algorithm depends on the heuristic. In the worst case this algorithm is O(b^d) where b is the average number of successors.

### A* Algorithm Application

### Conclusion( overview, include rewards and challenges)

### Team Work Details (what each member did and how we worked together)

In this project, all of our team members worked together efficiently and effectively to create our graph theory idea. We each explored an algorithm to test its capabilities in finding the shortest path. Sweta explored the Breadth-First search algorithm and examined how useful it would be to implement into our program. After research, she came to the conclusion that it would be time and memory consuming so implementing this would not be a good idea. Haeley explored the Depth-First search algorithm to see how useful it would be in our project. After her research, she later then came to the conclusion that this program may not even find a solution at all. Jordan researched the Greedy algorithm. With his findings, he came to realize that the algorithm would find a solution, but it mostly does not find the right solution. Lastly, Sheldon researched the A* Algorithm. With his findings, he thought this would be the best algorithm for us to explore on. Our team worked well on this project because we each individually researched a specific algorithm, then came back with our findings to come up with the solution and idea we decided to do. The divide and conquer technique helped us out tremendously.
