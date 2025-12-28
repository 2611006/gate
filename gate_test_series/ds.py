# data_structures.py

questions = {
    "easy": [
        {"q": "Time complexity to access i-th element in an array?", "options": ["O(1)", "O(n)", "O(log n)", "O(n^2)"], "correct": "O(1)"},
        {"q": "Which DS follows LIFO principle?", "options": ["Queue", "Stack", "Linked List", "Tree"], "correct": "Stack"},
        {"q": "Time complexity to insert at the head of a Singly Linked List?", "options": ["O(n)", "O(1)", "O(log n)", "O(n log n)"], "correct": "O(1)"},
        {"q": "Which of these is a non-linear data structure?", "options": ["Stack", "Array", "Graph", "Queue"], "correct": "Graph"},
        {"q": "In-order traversal of a BST gives elements in:", "options": ["Descending order", "Ascending order", "Random order", "Level order"], "correct": "Ascending order"},
        {"q": "Which DS is used for BFS traversal of a graph?", "options": ["Stack", "Queue", "Heap", "Tree"], "correct": "Queue"},
        {"q": "Height of a complete binary tree with n nodes?", "options": ["n", "log2(n)", "n^2", "sqrt(n)"], "correct": "log2(n)"},
        {"q": "Condition for a Circular Queue (size N) to be full?", "options": ["rear == front", "(rear+1)%N == front", "rear == N-1", "front == 0"], "correct": "(rear+1)%N == front"},
        {"q": "DS used for implementing recursion?", "options": ["Queue", "Stack", "Array", "Graph"], "correct": "Stack"},
        {"q": "Load factor of a hash table with n elements and m slots?", "options": ["n+m", "n/m", "m/n", "n*m"], "correct": "n/m"}
    ],
    "medium": [
        {"q": "Binary tree has 20 leaf nodes. Nodes of degree 2?", "options": ["19", "20", "21", "10"], "correct": "19"},
        {"q": "Time complexity to build a Max-Heap of size n?", "options": ["O(n log n)", "O(n)", "O(log n)", "O(n^2)"], "correct": "O(n)"},
        {"q": "Postfix form of A + B * C?", "options": ["ABC*+", "AB+C*", "ABC+*", "+ABC*"], "correct": "ABC*+"},
        {"q": "Primary clustering is a problem in:", "options": ["Chaining", "Linear Probing", "Double Hashing", "Quadratic Probing"], "correct": "Linear Probing"},
        {"q": "Height of an AVL tree with n nodes is approximately:", "options": ["log n", "1.44 log n", "2 log n", "n"], "correct": "1.44 log n"},
        {"q": "Distinct BSTs possible with 3 distinct keys?", "options": ["3", "4", "5", "6"], "correct": "5"},
        {"q": "Sum of degrees of all vertices in a graph with E edges?", "options": ["E", "V", "2E", "E^2"], "correct": "2E"},
        {"q": "Max nodes at level 'i' of a binary tree (root is level 0)?", "options": ["2^i", "2^(i+1)", "2i", "i^2"], "correct": "2^i"},
        {"q": "Which traversal gives postfix from an expression tree?", "options": ["Pre-order", "In-order", "Post-order", "Level-order"], "correct": "Post-order"},
        {"q": "Best case time for searching in a BST?", "options": ["O(1)", "O(log n)", "O(n)", "O(n log n)"], "correct": "O(log n)"}
    ],
    "hard": [
        {"q": "Pre-order of BST: 10, 5, 1, 7, 40, 50. Post-order?", "options": ["1, 7, 5, 50, 40, 10", "7, 1, 5, 40, 50, 10", "1, 5, 7, 10, 40, 50", "50, 40, 7, 5, 1, 10"], "correct": "1, 7, 5, 50, 40, 10"},
        {"q": "Address of A[5][10] in Row-Major (A[1..10][1..15], Base 100, Size 1)?", "options": ["169", "170", "159", "160"], "correct": "169"},
        {"q": "Min keys in a non-root internal B-Tree node of order m?", "options": ["ceil(m/2)", "ceil(m/2)-1", "m/2", "m-1"], "correct": "ceil(m/2)-1"},
        {"q": "Worst case search time in Hash Table with Chaining?", "options": ["O(1)", "O(log n)", "O(n)", "O(n^2)"], "correct": "O(n)"},
        {"q": "A graph is bipartite if it contains no:", "options": ["Cycles", "Odd Cycles", "Even Cycles", "Self-loops"], "correct": "Odd Cycles"},
        {"q": "Max edges in an acyclic undirected graph with n vertices?", "options": ["n", "n-1", "n(n-1)/2", "2n"], "correct": "n-1"},
        {"q": "2nd smallest element in a Min-Heap of size n is at level:", "options": ["0", "1", "2", "log n"], "correct": "1"},
        {"q": "Recurrence T(n) = T(n-1) + n belongs to:", "options": ["Quick Sort (Worst)", "Merge Sort", "Binary Search", "Heapify"], "correct": "Quick Sort (Worst)"},
        {"q": "Nodes in a full binary tree with L leaves?", "options": ["2L", "2L-1", "L+1", "2L+1"], "correct": "2L-1"},
        {"q": "Number of pointers in a Skip List node of height h?", "options": ["1", "h", "2h", "log h"], "correct": "h"}
    ]
}