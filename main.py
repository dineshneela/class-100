class Car(object):
    def __init__(self,model,color,company,speed_limit):
        self.color=color
        self.company=company
        self.speed_limit=speed_limit
        self.model=model
    def start(self):
        print("started")
    def stop(self):
        print("stop")
    def accelerate(self):
        print("accelerating")
    def change_gear(self):
        print("gearchanged")
tesla=Car("x","white","tesla","100")
print(tesla.color)
tesla.change_gear()