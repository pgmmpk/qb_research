qb_research
===========

Researching why left wheel encoder does not work properly.

## Requirements

Beaglebone Black computer with wheel encoders.

1. `Adafruit_BBIO Python` library installed
2. My [`beaglebone_pru_adc`](https://github.com/pgmmpk/beaglebone_pru_adc) library installed

## Description

Running `oscilloscope.py` will operate motors and perform encoder data capture into 6 CSV files.

You then transfer these CSV files to host machine (that does have display) and run `plot.py` to plot the
results.

## My results so far
...are disappointing as one encoder is unacceptably noisy.

![ain0.png](https://raw.github.com/pgmmpk/qb_research/master/ain0.png)

![ain2.png](https://raw.github.com/pgmmpk/qb_research/master/ain2.png)


## Happy Ending
Found a mechanical problem that caused these noisy signals. Re-attached encoder wheels, aligned them
properly, and this is what I get now:

![good_ain0.png](https://raw.github.com/pgmmpk/qb_research/master/good_ain0.png)

![good_ain2.png](https://raw.github.com/pgmmpk/qb_research/master/good_ain2.png)

