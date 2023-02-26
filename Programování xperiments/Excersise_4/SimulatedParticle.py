class SimulatedParticle(Track):
    def __init__(self, px, py, pz, energy, particle_id, parent_particle_id):
        super().__init__(px, py, pz, energy)
        self.__particle_id = particle_id
        self.__parent_particle_id = parent_particle_id
    
    def get_particle_id(self):
        return self.__particle_id
    
    def get_parent_particle_id(self):
        return self.__parent_particle_id
