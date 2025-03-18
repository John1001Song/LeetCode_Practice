## 🌲 DFS vs BFS in Trees

| Aspect | DFS (Depth-First Search) | BFS (Breadth-First Search) |
|--------|--------------------------|----------------------------|
| **Order of Exploration** | Explores as deeply as possible along each branch before backtracking. | Explores level-by-level, starting from shallow levels moving deeper. |
| **Data Structure** | **Stack** or recursion | **Queue** |
| **Typical Uses** | Tree traversal orders (Preorder, Inorder, Postorder), calculating tree depth | Level-order traversal, shortest paths in unweighted trees, minimum tree depth |
| **LeetCode Example** | [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) |

---

## 📈 DFS vs BFS in Graphs

| Aspect | DFS (Depth-First Search) | BFS (Breadth-First Search) |
|--------|--------------------------|----------------------------|
| **Order of Exploration** | Explores each path as far as possible, then backtracks. | Explores all neighbors at the current depth before moving deeper. |
| **Data Structure** | **Stack** or recursion | **Queue** |
| **Cycle Detection** | Efficient at detecting cycles. | Also efficient, often used for cycle detection in directed graphs. |
| **Shortest Path** | Typically not optimal; explores paths deeply first. | Ideal for shortest paths in **unweighted graphs**. |
| **Topological Sorting** | Commonly used (DFS-based) for Directed Acyclic Graphs (DAGs). | Also possible (Kahn’s Algorithm), but DFS is more common. |
| **Memory Usage** | Lower (stack or recursion depth). | Higher (due to queue maintenance). |
| **LeetCode Example** | [200. Number of Islands](https://leetcode.com/problems/number-of-islands/) | [207. Course Schedule](https://leetcode.com/problems/course-schedule/) |

---

## 🎯 Key Differences Summarized:

- **DFS**:
  - Deep path exploration first.
  - Useful for exhaustive search, backtracking, and recursion-friendly problems.
  - Good for cycle detection and topological sorting.

- **BFS**:
  - Level-by-level exploration.
  - Optimal for shortest path and minimum-depth problems.
  - Typically uses more memory due to queue.

---

## 🚩 When to Choose DFS or BFS?

### ✅ **Use DFS**:
- Exhaustive searches, pathfinding deeply, backtracking problems.
- Cycle detection and topological sorts.

### ✅ **Use BFS**:
- Shortest path searches in unweighted graphs or trees.
- Level-based traversals or minimum-level problems.

---

This concise guide should clearly outline the differences and typical applications of DFS and BFS in trees and graphs.
