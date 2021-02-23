def largestAltitude(self, gain: List[int]) -> int:
    alti = [0]
    i = 0
    for j in gain:
        alti.append(alti[i] + j)
        i += 1
    return max(alti)