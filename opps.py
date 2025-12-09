# opps concepts

class Factory:
    def  __init__(self,material,pockets,zips,):
        self.material=material
        self.pockets=pockets
        self.zips=zips

    def show(self):
        print(f"your objects detail are {self.material},{self.pockets},{self.zips}")

reebok = Factory("leather",3,3) 
campus = Factory("naylon",3,3) 



reebok.show()