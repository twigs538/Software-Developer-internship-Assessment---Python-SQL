def main():
    qty = None
    cost = None
    def fetch_quantity():
        """
        Returns a number, any number
        """
        ...
        return ...
    def fetch_cost():
        """
        Returns a number, any number
        """
        ...
        return ...
    def compute_cost_per_quantity():
        try:
            qty = fetch_quantity()
        except Exception as e:
            print(e)
            exit()
        try:
            cost = fetch_cost()
            cost_per_quantity = cost/qty
        except Exception as e:
            cost_per_quantity = 0
        return cost_per_quantity
    cost_per_quantity = compute_cost_per_quantity()
    a = 1 + 2 + cost_per_quantity
    b = 4 + 5
    print(a+b)