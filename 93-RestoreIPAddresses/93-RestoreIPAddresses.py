# Last updated: 5/21/2025, 7:44:26 PM
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        def backtrack(start, path):
            if len(path) == 4:
                if start == len(s):
                    res.append(".".join(path))
                return

            for end in range(start + 1, min(start + 4, len(s) + 1)):
                segment = s[start:end]
                if (segment.startswith('0') and len(segment) > 1) or int(segment) > 255:
                    continue
                backtrack(end, path + [segment])

        backtrack(0, [])
        return res