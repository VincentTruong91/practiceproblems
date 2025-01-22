class TimeMap:

    def __init__(self):
        #constructor
        self.store = {} #key=string, value=[list of [value, timestamp]]
        #key: list of [value, timestamp]
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, [])

        #binary search
        l = 0
        r = len(values) - 1
        while l <= r:
            m = (l + r) // 2 # // = integer division
            if values[m][1] <= timestamp: #this is the closes valid that we see so far
                res = values[m][0]
                l = m + 1
            else: #greater than timestamp not allowed
                #not valid so wont set res
                r = m - 1
        return res
