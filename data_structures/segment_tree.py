class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (2 * self.n)
        # Build the segment tree
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, index, value):
        pos = index + self.n
        self.tree[pos] = value
        while pos > 1:
            pos //= 2
            self.tree[pos] = self.tree[2 * pos] + self.tree[2 * pos + 1]

    def query(self, left, right):
        left += self.n
        right += self.n + 1
        sum_val = 0
        while left < right:
            if left % 2 == 1:
                sum_val += self.tree[left]
                left += 1
            if right % 2 == 1:
                right -= 1
                sum_val += self.tree[right]
            left //= 2
            right //= 2
        return sum_val
