Dynamic Programming (DP) vs Greedy Algorithm (GA)
Dynamic Programming
Core Principles:
Optimal Substructure: The optimal solution to a problem contains optimal solutions to subproblems
Overlapping Subproblems: Subproblems are solved multiple times, so we use memoization
Global Optimization: Finds the globally optimal solution by solving all subproblems
Characteristics:
Requires storing intermediate results (memoization)
Usually higher time complexity but guarantees optimal solution
Suitable for problems with overlapping subproblems
Bottom-up or top-down approach
Classic Examples:
Fibonacci sequence
Knapsack problem
Longest Common Subsequence
Shortest path problems
Greedy Algorithm
Core Principles:
Local Optimization: Makes the locally optimal choice at each step
No Backtracking: Current choice doesn't affect previous choices
May Not Be Globally Optimal: Can result in suboptimal solutions
Characteristics:
Simple and efficient, usually lower time complexity
No need to store intermediate states
Cannot guarantee optimal solution
Requires proof of greedy strategy correctness
Classic Examples:
Coin change problem (in some cases)
Activity selection problem
Minimum Spanning Tree (Kruskal, Prim)
Huffman coding
Key Differences
Aspect	Dynamic Programming	Greedy Algorithm
Optimality	Guarantees global optimum	May only be locally optimal
Complexity	Usually higher	Usually lower
Storage	Requires storing intermediate results	No additional storage needed
Applicability	Problems with overlapping subproblems	Problems with greedy choice property
Proof	Need to prove optimal substructure	Need to prove greedy strategy correctness
When to Use Which?
Use Dynamic Programming when:
You need the globally optimal solution
The problem has overlapping subproblems
The problem can be broken down into subproblems
You can afford higher time/space complexity
Use Greedy Algorithm when:
Local optimal choices lead to global optimum
You need a fast "good enough" solution
The problem has the greedy choice property
Time/space efficiency is critical