from typing import List, Tuple
from collections import defaultdict

class Solution:
    def get_signature(self, s: str) -> Tuple[int]:
        if len(s) < 2:
            return ()  # empty tuple for 1-char strings
        diff = (ord(s[1]) - ord(s[0])) % 26
        for i in range(2, len(s)):
            if (ord(s[i]) - ord(s[i - 1])) % 26 != diff:
                return None  # Not a constant delta
        return (len(s), diff)  # Use both length and delta for uniqueness

    def findBuddiesAndDistinct(self, words: List[str]) -> Tuple[List[List[str]], List[str]]:
        signature_dict = defaultdict(list)
        distinct_words = set(words)

        for word in words:
            sig = self.get_signature(word)
            if sig is not None:
                signature_dict[sig].append(word)

        # Only return groups that have at least 2 members
        buddy_groups = [group for group in signature_dict.values() if len(group) > 1]

        return buddy_groups, sorted(distinct_words)

# Example usage
solution = Solution()
words = ["ab", "cd", "ef", "az", "yx", "ba", "dc"]
buddies, distinct = solution.findBuddiesAndDistinct(words)
print("Buddy Groups:", buddies)
print("Distinct Strings:", distinct)
