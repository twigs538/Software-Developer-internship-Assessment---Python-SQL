class TestMath:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def test_add(self): 
        return self.x + self.y
    
    def test_subtract(self):
        return self.x - self.y
    
    def test_multiply(self):
        return self.x * self.y

tm = TestMath(10, 10)
print(tm.test_add())
print(tm.test_subtract())
print(tm.test_multiply())