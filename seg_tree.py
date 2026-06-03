class SegmentTree():
    """
    - arr: 元配列
    - op(left, right): 区間取得時の演算
    - e: 演算の単位元
    """
    def __init__(self, arr, op, e):
        self.n = len(arr)
        self.op = op # 
        self.e = e

        # 木のサイズ（元配列のi番目 = セグ木のsize+i番目）
        self.size = 1
        while self.size < self.n:
            self.size <<= 1

        # 1-indexed の木を使う（インデックス 1..2*size-1 を使用）
        self.data = [self.e] * (2 * self.size)

        # 葉に元配列を代入
        for i in range(self.n):
            self.data[self.size + i] = arr[i]

        # 内部ノードを構築
        for i in range(self.size - 1, 0, -1):
            self.data[i] = self.op(self.data[2 * i], self.data[2 * i + 1])

    # 1点更新
    def set(self, i, val):
        idx = self.size + i
        self.data[idx] = val
        idx //= 2
        while idx >= 1:
            self.data[idx] = self.op(self.data[2 * idx], self.data[2 * idx + 1])
            idx //= 2

    # 区間取得 [l:r)
    def query(self, l, r):
        l += self.size
        r += self.size

        l_val = self.e
        r_val = self.e

        while l < r:
            if l & 1:
                l_val = self.op(l_val, self.data[l])
                l += 1
            if r & 1:
                r -= 1
                r_val = self.op(self.data[r], r_val)
            l //= 2
            r //= 2

        return self.op(l_val, r_val)