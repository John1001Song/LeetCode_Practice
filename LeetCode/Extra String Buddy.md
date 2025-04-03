# 🧩 Problem: Find Buddy Strings and Distinct Strings

## 📝 Description

You are given a list of lowercase English strings. Two strings are considered **buddies** if:

- They have the **same length**, and  
- At every position `i`, the **difference between corresponding characters** is the same constant (modulo 26):


Your task is to:
1. Group all strings into **buddy groups** (each group contains **2 or more** strings).
2. Return all **distinct strings**, sorted in **lexicographical order**.

---

## 📥 Input

- A list of strings: `words`
  - `1 <= len(words) <= 10^4`
  - Each string contains only lowercase English letters `'a'` to `'z'`
  - Length of each string is at most 100

---

## 📤 Output

- A tuple of:
  - `List[List[str]]`: A list of **buddy groups** (only groups with 2 or more members)
  - `List[str]`: A list of all **distinct strings**, in **sorted order**

---

## 🔍 Examples

### Example 1
**Input:**
```python
words = ["ab", "cd", "ef", "az", "yx", "ba", "dc"]
**Output:**
Buddy Groups: [['ab', 'cd', 'ef'], ['az', 'yx']]
Distinct Strings: ['ab', 'az', 'ba', 'cd', 'dc', 'ef', 'yx']

### Example 1
**Input:**
```python
words = ["a", "b", "c", "z", "aa", "bb", "cc"]
**Output:**
Buddy Groups: [['a', 'b', 'c', 'z'], ['aa', 'bb', 'cc']]
Distinct Strings: ['a', 'aa', 'b', 'bb', 'c', 'cc', 'z']

