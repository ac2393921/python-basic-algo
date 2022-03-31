from collections import defaultdict
from typing import Dict, List


class UnionFind:
    """Union-Find
    """
    def __init__(self, n: int) -> None:
        """init

        Args:
            n (int): 要素数
        """
        self.n = n
        self.parents = [-1] * n

    def find(self, x: int) -> int:
        """要素xが属するグループの根を返す

        Args:
            x (int): 要素

        Returns:
            int: 根
        """
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x: int, y: int) -> None:
        """
        要素xが属するグループと要素yが
        属するグループとを併合する

        Args:
            x (int): 要素
            y (int): 要素
        """
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x: int) -> int:
        """要素xが属するグループのサイズ（要素数）を返す

        Args:
            x (int): 要素

        Returns:
            int: 要素数
        """
        return -self.parents[self.find(x)]

    def same(self, x: int, y: int) -> bool:
        """要素x, yが同じグループに属するかどうかを返す

        Args:
            x (int): 要素
            y (int): 要素

        Returns:
            bool: 判定結果
        """
        return self.find(x) == self.find(y)

    def members(self, x: int) -> List[int]:
        """要素xが属するグループに属する要素をリストで返す

        Args:
            x (int): 要素

        Returns:
            List[int]: 要素のリスト
        """
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self) -> List[int]:
        """すべての根の要素をリストで返す

        Returns:
            List[int]: 根の要素リスト
        """
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self) -> int:
        """グループの数を返す

        Returns:
            int: グループ数
        """
        return len(self.roots())

    def all_group_members(self) -> Dict[int, int]:
        """
        {ルート要素: [そのグループに含まれる要素のリスト], ...}
        のdefaultdictを返す

        Returns:
            Dict[int, int]: ルート要素
        """
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self) -> None:
        """print表示用
        """
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())
