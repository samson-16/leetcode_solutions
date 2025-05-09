# Last updated: 5/9/2025, 6:18:08 PM
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        email_to_name = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        for acc in accounts:
            name = acc[0]
            first_email = acc[1]
            for email in acc[1:]:
                if email not in parent:
                    parent[email] = email
                union(email, first_email)
                email_to_name[email] = name

        groups = defaultdict(list)
        for email in parent:
            root = find(email)
            groups[root].append(email)

        res = []
        for root in groups:
            name = email_to_name[root]
            res.append([name] + sorted(groups[root]))

        return res