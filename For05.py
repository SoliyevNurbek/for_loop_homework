def main(A,B):
    """
    Return the numbers from B to A in the form of a list.
    Args:
        A: int
        B: int
    Returns:
        list: return  answer
    """
    s=[]
    for i in range(B,A,1):
        s.append(i)
    return s[::-1]
print(main(9,1))