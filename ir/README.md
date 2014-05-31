My Quickbot v1 has problem: IR sensors are very noisy. I traced the problem to the voltage dividers. 
Seems like instead of using 20kOhm + 10kOhm divider we should use 2kOhm + 1kOhm (or even 1kOhm+470Ohm).

An experiment: connect AIN0 to the ground via 10kOhm resistor (no IR, just trying to "ground" the 
AIN0 input expecting 0 digital reading from ADC). Result is:

![ir-10k-pulldown.png](https://raw.github.com/pgmmpk/qb_research/master/ir/ir-10k-pulldown.png)

When grounding AIN0 with 470Ohm the result is much cleaner:

![ir-470-pulldown.png](https://raw.github.com/pgmmpk/qb_research/master/ir/ir-470-pulldown.png)

Conclusion: 10kOhm is not enough to reliably pull down ADC input. Use 1kOhm or lower.

I was not able to find official recommendations regarding the impedance of ADC and IR. Some sources suggest that 
ADC input should be pulled down with 1kOhm or lower. This makes sense, given the pictures above.

In any case, I replaced all IR voltage divider circuits with 1kOhm + 470Ohm circuits. The voltage
divider for the wheel encoder was replaced with 2kOhm + 2kOhm circuit. In case of wheel encoders it does
not seem to make any difference for me. But IR signals are much cleaner now.
