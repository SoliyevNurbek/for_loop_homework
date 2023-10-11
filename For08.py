def main(N):
    """
    The number N is given. Calculate the sum below: 1 + 1/2 + 1/3 + … + 1/N.
    Args:
        N: int
    Returns:
        float: return  answer
    """
    s=float(0)
    for i in range(1,N,1):
        s+=1/i
    return float(s)
print(main(3))