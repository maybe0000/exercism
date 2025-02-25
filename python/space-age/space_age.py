class SpaceAge:
    divideby = 60*60*24*365.25
        
    planet_days = {
            "Mercury": 0.2408467,
            "Venus": 0.61519726,
            "Earth": 1.0,
            "Mars": 1.8808158,
            "Jupiter": 11.862615,
            "Saturn": 29.447498,
            "Uranus": 84.016846,
            "Neptune": 164.79132
    }
    
    def __init__(self, seconds):
        self.seconds = seconds
        
        for planet, ratio in self.planet_days.items():
            setattr(self, f'on_{planet.lower()}', self.create_method(ratio))
    
    def create_method(self, ratio):
        return lambda: round(self.seconds / (self.divideby * ratio), 2)