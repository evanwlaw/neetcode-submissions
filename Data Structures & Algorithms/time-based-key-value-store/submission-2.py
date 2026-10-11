class TimeMap:
    """
    return the value of key

    alice : [happy, 1], [sad, 3]

    in the get, we need to get the one with prevtimestamp <=  timestamp.

    timestamps in set are strictly increasing -> sorted
    binary search for a value <= timestampe
    """

    def __init__(self):
        self.store = {} # key : [val, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        items = self.store.get(key, []) # [[val, 1], [val2, 2]]
        l, r = 0, len(items) - 1
        res = ""
        while l <= r:
            m = l + (r - l) // 2
            
            if items[m][1] <= timestamp:
                res = items[m][0]
                l = m + 1
            else:
                r = m - 1

        return res