class cars:
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color
        print(f'The car is:',brand)
    
car1=cars("bmw","black")
print(car1)
print(car1.brand)
print(car1.color)