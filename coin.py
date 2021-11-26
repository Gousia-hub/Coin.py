import random
    

class Rupee:

    def __init__(self,rare = False):
        self.rare = rare

        if self.rare:
            self.value = 1.25
        else:
            self.value = 10.0

        self.colour = "silver"
        self.num_edges = 1
        self.diameter= 22.5
        self.thickness = 3.15
        self.heads  =True

    def __del__(self):
        print("Coin spent!")

    def rust(self):
        self.colour = "brownish"
        
    def clean(self):
        self.colour = "silver"
        
    def flip(self):
        heads_options  = [True , False]
        choice = random.choice(heads_options)
        self.heads = choice

    

    
    



        
