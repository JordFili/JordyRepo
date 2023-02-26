import math

class Track:
    def __init__(self, px, py, pz, energy):
        self.__px = px
        self.__py = py
        self.__pz = pz
        self.__energy = energy
    
    def pt(self):
        return math.sqrt(self.__px**2 + self.__py**2)
    
    def eta(self):
        cos_theta = self.__pz / math.sqrt(self.__px**2 + self.__py**2 + self.__pz**2)
        return -math.log(math.tan(math.acos(cos_theta)/2))

    def get_momentum(self):
        return (self.__px, self.__py, self.__pz, self.__energy)
