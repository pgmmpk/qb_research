import contextlib
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM

RIGHT_MOTOR_PINS  = 'P8_12', 'P8_10', 'P9_14'
LEFT_MOTOR_PINS = 'P8_14', 'P8_16', 'P9_16'

@contextlib.contextmanager
def motor_setup(dir1_pin, dir2_pin, pwm_pin):
    """
        Sets up context for operating a motor.
        """
    # Initialize GPIO pins
    GPIO.setup(dir1_pin, GPIO.OUT)
    GPIO.setup(dir2_pin, GPIO.OUT)
    
    # Initialize PWM pins: PWM.start(channel, duty, freq=2000, polarity=0)
    PWM.start(pwm_pin, 0)
    
    def run_motor(speed):
        if speed > 100:
            speed = 100
        elif speed < -100:
            speed = -100
        
        if speed > 0:
            GPIO.output(dir1_pin, GPIO.LOW)
            GPIO.output(dir2_pin, GPIO.HIGH)
            PWM.set_duty_cycle(pwm_pin, abs(speed))
        elif speed < 0:
            GPIO.output(dir1_pin, GPIO.HIGH)
            GPIO.output(dir2_pin, GPIO.LOW)
            PWM.set_duty_cycle(pwm_pin, abs(speed))
        else:
            GPIO.output(dir1_pin, GPIO.LOW)
            GPIO.output(dir2_pin, GPIO.LOW)
            PWM.set_duty_cycle(pwm_pin, 0)
    
    yield run_motor

    PWM.set_duty_cycle(pwm_pin, 0)
    
    GPIO.cleanup()
    PWM.cleanup()
