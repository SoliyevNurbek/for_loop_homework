def main(price):
    """
    The price of a kilogram of sweets is given. Return the price of a dessert from one to ten kg in the form of a list.
    Args:
        price: int
    Returns:
        list: return  answer
    """
    s=[]
    for i in range(1,price,1):
        s.append(price*i)
    return s
print(main(5))