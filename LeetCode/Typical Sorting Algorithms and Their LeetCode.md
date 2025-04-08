# Typical Sorting Algorithms and Their LeetCode Applications

This document provides an overview of some common sorting algorithms and lists relevant LeetCode problems where sorting plays an important role. Even if you're not asked to implement these sorts from scratch during an interview, understanding them is crucial for reasoning about time and space tradeoffs and for using sorting as a preprocessing step in many problems.

---

## Common Sorting Algorithms

### 1. Bubble Sort
- **Concept:**  
  Repeatedly compares adjacent elements and swaps them if they are in the wrong order. This “bubbles” the largest element to the end of the array in each pass.
- **Time Complexity:**  
  \(O(n^2)\)
- **Usage:**  
  Mainly an educational tool. It’s rarely used in production or interviews due to its inefficiency.

---

### 2. Selection Sort
- **Concept:**  
  Scans for the smallest (or largest) element in the unsorted portion and swaps it with the element at the beginning of that portion.
- **Time Complexity:**  
  \(O(n^2)\)
- **Usage:**  
  Simple and intuitive but inefficient for large datasets. Generally not asked as a standalone problem.

---

### 3. Insertion Sort
- **Concept:**  
  Builds the sorted array one element at a time by comparing each new element with those already sorted and inserting it in the correct position.
- **Time Complexity:**  
  \(O(n^2)\) (efficient for small or nearly sorted datasets)
- **Usage:**  
  Discussed in interviews for small arrays or nearly sorted data.

---

### 4. Merge Sort
- **Concept:**  
  A divide-and-conquer algorithm that splits the array into halves, recursively sorts each half, and then merges the sorted halves.
- **Time Complexity:**  
  \(O(n \log n)\)
- **Usage:**  
  - Frequently cited as an example of a stable, reliable sort.
  - **LeetCode Examples:**
    - **Merge Intervals (#56):** Often starts by sorting intervals.
    - **Reverse Pairs (#493):** Can be solved by modifying merge sort to count inversions.

---

### 5. Quick Sort
- **Concept:**  
  Selects a pivot and partitions the array into elements less than and greater than the pivot, then recursively sorts the partitions.
- **Time Complexity:**  
  Average: \(O(n \log n)\); Worst-case: \(O(n^2)\) with poor pivot selection.
- **Usage:**  
  Commonly used in many libraries as a default sort.  
  - **LeetCode Examples:**
    - **Sort an Array (#912):** You can implement quick sort to solve this problem.
    - **Largest Number (#179):** Requires a custom comparator based on sorting.

---

### 6. Heap Sort
- **Concept:**  
  Converts the array into a heap and then repeatedly extracts the maximum (or minimum) to form the sorted order.
- **Time Complexity:**  
  \(O(n \log n)\)
- **Usage:**  
  Useful in scenarios where you need efficient retrieval of the largest or smallest element.  
  - **LeetCode Examples:**
    - **Top K Frequent Elements (#347):** Typically solved using a heap.
    - **Find Median from Data Stream (#295):** Uses a combination of max-heap and min-heap.

---

### 7. Counting Sort / Bucket Sort
- **Concept:**  
  Non-comparison-based sorting methods that work well when the range of input data is limited.
- **Time Complexity:**  
  \(O(n)\) under the right conditions.
- **Usage:**  
  Best applied when the input values fall within a small range.  
  - **LeetCode Examples:**
    - **Sort Colors (#75):** Often solved using techniques that resemble counting sort or the Dutch National Flag algorithm.

---

## How Sorting Appears in LeetCode Problems

1. **Direct Implementation Problems:**  
   - **Sort an Array (#912):** Requires you to implement a sorting algorithm.
   - Others may ask you to code up a custom sort algorithm.

2. **Preprocessing Step in Problem Solving:**  
   Sorting is often the first step before applying further logic:
   - **Merge Intervals (#56):** Intervals are sorted before being merged.
   - **Kth Largest Element in an Array (#215):** Can be solved by sorting or using heap-based methods.
   - **Largest Number (#179):** Involves defining a custom comparator for sorting.

3. **Specialized Sorting Approaches:**  
   Some problems require non-comparison-based sorting like bucket sort, which are essential when input constraints favor these approaches.

---

## Next Steps for Practice

- **Implement Standard Sorting Algorithms:**  
  Practice coding Bubble Sort, Selection Sort, Insertion Sort, Merge Sort, Quick Sort, and Heap Sort. This will solidify your understanding of each algorithm.

- **Solve Sorting-Related LeetCode Problems:**  
  Work on problems like **Sort Colors (#75)** and **Sort an Array (#912)** to see how these sorting concepts are used in various contexts.

- **Explore Custom Comparator Problems:**  
  Work on problems like **Largest Number (#179)** to learn how to define custom sorting criteria.

Understanding these sorting techniques will prepare you for both sorting-specific questions and problems where sorting serves as a key preprocessing step.

Happy coding!
