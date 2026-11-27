from dataclasses import dataclass


@dataclass
class Motorconfig:

    steps_per_revolutions: int = 200
    max_speed: float = 20.0
    microstepping: int = 8
    gear_ratio: int


class steppermotor:

    def __init__(self, config:Motorconfig, driver):

        self.config = config
        self.driver = driver

        self.position = 0.0
        self.target_position = 0.0

        self.is_homed = False
        self.is_moving = False

        pass

    def distance_to_steps(self, distance):

        #converting steps into mm
        # formula = Steps = S * M * G / T

        steps_per_mili = (

            (self.config.steps_per_revolutions * self.config.microstepping * self.config.gear_ratio) / self.config.travel_per_revolution
        )

        return (distance * steps_per_mili)
    

    def set_speed(self, speed):

        if speed < 0 :
            print("speed cannot be negative")


        #speed cannot exceed maximum speed
        if speed > self.config.max_speed:

            print("cannot exceed max speed")

        
        self.speed = speed
        
        pass

    #def set_accelaration(self, accelaration):
    # might implement an acceleration curve/ max accelaration.
    # between pictures the movement might just be linear
    
    def move(self, distance):

       target = self.target_position + distance

       self.move_to(target)

    pass

    def move_to(self, position):

        distance = position - self.position

        steps = self.distance_to_steps(distance)

        self.target_position = position

        self.driver.move_steps(steps, self.speed) 

        pass

   
    def home(self):

        #move towards microswitch, check state of switch, stop the motor. set position to zero


        pass

    def reset_position(self):

        self.position = 0.0
        self.target_position = 0.0
        self.is_homed = True

        pass

    