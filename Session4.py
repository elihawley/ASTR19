class Cat:
    def __init__(self, arms, legs, eyes, tail, furry):
        self.arms = 3.456
        self.legs = 3.587
        self.eyes = 2
        self.tail = True
        self.furry = True

    def printValues(self):
        print("arm length: " + self.arms)
        print("leg length: " + self.legs)
        print("amount of eyes " + self.eyes)
        if (self.tail):
            print("has tail")
        else:
            print("no tail")
        if (self.furry):
            print("is furry")
        else:
            print("not furry")
