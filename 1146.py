class SnapshotArray:

  def __init__(self, length: int):
    self.snap_id = 0
    self.array = [[[0, 0]] for _ in range(length)]

  def set(self, index: int, val: int) -> None:
    self.array[index].append([self.snap_id, val])

  def snap(self) -> int:
    self.snap_id += 1
    return self.snap_id - 1

  def get(self, index: int, snap_id: int) -> int:
    l, r = 0, len(self.array[index])

    while l < r:
      mid = (l + r) // 2

      if self.array[index][mid][0] > snap_id:
        r = mid
      else:
        l = mid + 1

    return self.array[index][l-1][1]

