class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        transdict = defaultdict(list)

        # Parse and group by name
        for idx , transaction in enumerate(transactions):
            name, time, amount, city = transaction.split(",")
            transdict[name].append((idx, int(time), int(amount), city, transaction))
        invalid_check = [False] * len(transactions)
        invalid = []

        # Process each person
        for name, vals in transdict.items():
            vals.sort(key=lambda x: x[1])  # sort by time

            for i in range(len(vals)):
                idx, time_i, amount_i, city_i, original_i = vals[i]

                # Rule 1: Amount > 1000
                if amount_i > 1000:
                    if invalid_check[idx] ==False:
                        invalid.append(transactions[idx])
                        invalid_check[idx] = True

                # Rule 2: Within 60 min in different city
                for j in range(len(vals)):
                    if i != j:
                        idx_j , time_j, _, city_j, original_j = vals[j]
                        if abs(time_i - time_j) <= 60 and city_i != city_j:                 
                             if invalid_check[idx] ==False:
                                invalid.append(transactions[idx])
                                invalid_check[idx] = True
        return list(invalid)

                