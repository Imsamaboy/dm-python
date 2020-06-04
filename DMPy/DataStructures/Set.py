
class Set:
    def __init__(self, iterable = []):
        sorted_input = sorted(list(iterable))
        if len(sorted_input) == 0:
            self.data = []
            return
        self.data = [sorted_input[0]]
        for i in range(1, len(sorted_input)): # Удаляем дубликаты
            if sorted_input[i] != sorted_input[i-1]:
                self.data.append(sorted_input[i])

    def __contains__(self, elem):
        return elem in self.data

    def __iter__(self):
        return iter(self.data)

    def cup(self, B):
        res = []
        p1 = 0
        p2 = 0
        while p1 < len(self.data) or p2 < len(B.data):
            if p1 == len(self.data):
                res.append(B.data[p2])
                p2 += 1
            elif p2 == len(B.data):
                res.append(self.data[p1])
                p1 += 1
            elif self.data[p1] < B.data[p2]:
                res.append(self.data[p1])
                p1 += 1
            elif B.data[p2] < self.data[p1]:
                res.append(B.data[p2])
                p2 += 1
            else:
                res.append(self.data[p1])
                p1 += 1
                p2 += 1
        return Set(res)

    def cap(self, B):
        res = []
        p1 = 0
        p2 = 0
        while p1 < len(self.data) and p2 < len(B.data):
            if self.data[p1] < B.data[p2]:
                p1 += 1
            elif B.data[p2] < self.data[p1]:
                p2 += 1
            else:
                res.append(self.data[p1])
                p1 += 1
                p2 += 1
        return Set(res)
    
    def equals(self, B):
        if len(self.data) != len(B.data):
            return False
        for i in range(len(self.data)):
            if self.data[i] != B.data[i]:
                return False
        return True

    def __str__(self):
        return str(self.data)
