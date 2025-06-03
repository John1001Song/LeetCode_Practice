# Pseudocode
## Lomuto Quick Sort (in‑place)

quicksort(nums, low, high):
    if high - low <= 0:            # (1) base case (size ≤ 1)
        return
    p = partition(nums, low, high) # (2) pivot in final position
    quicksort(nums, low,  p-1)     # (3) left side  (< pivot)
    quicksort(nums, p+1, high)     # (4) right side (> pivot)


## Lomuto partition

partition(nums, low, high):        # (A)
    pivot ← nums[high]             # (B) choose tail element
    i ← low - 1                    # (C) end of "< pivot" region
    for j ← low to high - 1:       # (D) scan sub‑array
        if nums[j] < pivot:        # (E) element belongs left
            i ← i + 1              # (F) expand "< pivot" region
            swap nums[i] ↔ nums[j] # (G) place element
    swap nums[i+1] ↔ nums[high]    # (H) drop pivot in place
    return i + 1                   # (I) index of pivot

