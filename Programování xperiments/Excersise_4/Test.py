track = Track(10, 20, 30, 40)     # Something to track


print("Track pt:", track.pt())
print("Track eta:", track.eta())


simulated_particle = SimulatedParticle(10, 20, 30, 40, 11, 22)


print("SimulatedParticle pt:", simulated_particle.pt())
print("SimulatedParticle eta:", simulated_particle.eta())


print("Particle ID:", simulated_particle.get_particle_id())
print("Parent Particle ID:", simulated_particle.get_parent_particle_id())