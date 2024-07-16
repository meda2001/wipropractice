class ParkingSystem:
    def __init__(self, big, medium, small):
        self.spaces = [big, medium, small]
    
    def addCar(self, carType):
        if self.spaces[carType - 1] > 0:
            self.spaces[carType - 1] -= 1
            return True
        return False

# Example usage:
parkingSystem = ParkingSystem(1, 1, 0)
print(parkingSystem.addCar(1))  # Output: True
print(parkingSystem.addCar(2))  # Output: True
print(parkingSystem.addCar(3))  # Output: False
print(parkingSystem.addCar(1))  # Output: False
