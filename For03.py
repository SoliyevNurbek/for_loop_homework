def main(k,n):
    """
    Repeat the number k n times and return to the list view.
    Args:
        k: int
        n: int
    Returns:
        list: return  answer
    """
    s=[]
    for i in range(n):
        s.append(k)
    return s
print(main(7,7))