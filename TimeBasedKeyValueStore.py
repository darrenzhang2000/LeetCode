class TimeMap:

    def __init__(self):
        self.times = collections.defaultdict(list)
        self.values = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.times[key].append(timestamp)
        self.values[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        i = bisect.bisect(self.times[key], timestamp)
        return self.values[key][i - 1] if i else ''
'''
class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ht = DefaultDict(list)
        

    # O(1)
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.ht[key].append((timestamp, value))

    # O(logn)
    def get(self, key: str, timestamp: int) -> str:
        arr = self.ht[key]
        left, right = 0, len(arr) - 1
        while left <= right:
            m = left + (right - left) // 2
            if arr[m][0] <= timestamp and (m + 1 == len(arr) or arr[m + 1][0] > timestamp):
                return arr[m][1]
            elif timestamp > arr[m][0]:
                left = m + 1
            else:
                right = m - 1
        return ""
'''
