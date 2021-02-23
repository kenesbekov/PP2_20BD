def subtractProductAndSum(self, n: int) -> int:
    product, sumdig = 1, 0
    while n:
        dig = n % 10
        product *= dig
        sumdig += dig
        n //= 10
    return product - sumdig