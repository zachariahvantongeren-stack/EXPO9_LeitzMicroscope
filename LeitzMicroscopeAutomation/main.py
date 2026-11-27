from classes.MotorClass import Motorconfig
from classes.MotorClass import steppermotor




def main():

    #configure motors:

    x_config, y_config, z_config = Motorconfig

    x_motor = steppermotor(x_config, driver=None)
    y_motor = steppermotor(y_config, driver=None)
    z_motor = steppermotor(z_config, driver=None)


if __name__ == "__main__":
    
    main()


    
    