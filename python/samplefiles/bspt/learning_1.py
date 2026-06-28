class Car:
    def __init__(self,name,year,model):
        self.name=name
        self.year=year
        self.model=model
        
    def __str__(self):
        return self.name +" "+ self.model 
    
    def __eq__(self, other):
        return self.year==other.year and self.name==other.name
    def __lt__(self, other):
        return self.year>other.year 
    def __add__(self, other):
        pass
    def __contains__(self, keyword):
        return keyword in self.name or keyword in self.model
    def __getitem__(self, key):
        if key =="name":
            return self.name
        elif key=="year":
            return self.year
        elif key=="model":
            return self.model
        else:
            return f" key {key} is invalid"
        
        
car1=Car("bmw","2026","m8")
car2=Car("bmw","2026","m8")
car3=Car("audi","2025","r8")

print(car1["name"])