def main():
    qty = None
    cost = None

def fetch_quantity():
    """
    Returns a number, any number
    """
    #...
    #return 5
    return ...

def fetch_cost():
    """
    Returns a number, any number
    """
    #...
    #return 4
    return ...

def compute_cost_per_quantity():
    try:
        qty = fetch_quantity()
    except:
        raise "fetch_quantity() function has an error! Terminating."

    try:
        cost = fetch_cost()
    except:
        pass
    
    try:
        cost_per_quantity = cost/qty
    except:
        raise "cost_per_quantity = cost/qty has an error! Terminating. "
    return cost_per_quantity

cost_per_quantity = compute_cost_per_quantity()
a = 1 + 2 + cost_per_quantity
b = 4 + 5
print(a+b)