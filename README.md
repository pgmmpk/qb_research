qb_research
===========

Researching why left wheel encoder does not work properly.

## Requirements

Beaglebone Black computer with wheel encoders.

1. `Adafruit_BBIO Python` library installed
2. My `beaglebone_pru_adc` library installed

## Description

Running `oscilloscope.py` will operate motors and perform encoder data capture into 6 CSV files.

You then transfer these CSV files to host machine (that does have display) and run `plot.py` to plot the
results.

## My results so far
...are disappointing as one encoder is unacceptably noisy.

