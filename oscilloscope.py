import beaglebone_pru_adc as adc
import time
import motors

def oscilloscope(capture, offset, filename, numsamples=10000):
	
	capture.oscilloscope_init(offset, numsamples)
	
	for _ in range(10):
	    if capture.oscilloscope_is_complete():
	        break
	    print '.'
	    time.sleep(0.1)
	
	with open(filename, 'w') as f:
	    for x in capture.oscilloscope_data(numsamples):
	        f.write(str(x) + '\n')

capture = adc.Capture()
capture.start()

print 'Capturing AIN0 at rest'
oscilloscope(capture, adc.OFF_VALUES, 'data_ain0_atrest.csv')

with motors.motor_setup(*motors.RIGHT_MOTOR_PINS) as run:
	run(80) # run motor forward
	time.sleep(2.0) # let it settle

	print 'Capturing AIN0 at run (forward)'
	oscilloscope(capture, adc.OFF_VALUES, 'data_ain0_forward.csv')
	
	run(0)
	time.sleep(2.0)
	
	run(-80)
	print 'Capturing AIN0 at run (reverse)'
	oscilloscope(capture, adc.OFF_VALUES, 'data_ain0_backward.csv')

	run(0)
	time.sleep(2.0)
	
print 'Capturing AIN2 at rest'
oscilloscope(capture, adc.OFF_VALUES + 8, 'data_ain2_atrest.csv')

with motors.motor_setup(*motors.LEFT_MOTOR_PINS) as run:
	run(80) # run motor forward
	time.sleep(2.0) # let it settle

	print 'Capturing AIN2 at run (forward)'
	oscilloscope(capture, adc.OFF_VALUES+8, 'data_ain2_forward.csv')
	
	run(0)
	time.sleep(2.0)
	
	run(-80)
	print 'Capturing AIN2 at run (reverse)'
	oscilloscope(capture, adc.OFF_VALUES+8, 'data_ain2_backward.csv')

	run(0)
	time.sleep(2.0)

capture.stop()
capture.wait()
capture.close()

print 'done'

