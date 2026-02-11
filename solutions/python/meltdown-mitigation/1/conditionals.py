"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    """Verify criticality is balanced.

    :param temperature: int or float - temperature value in kelvin.
    :param neutrons_emitted: int or float - number of neutrons emitted per second.
    :return: bool - is criticality balanced?

    A reactor is said to be critical if it satisfies the following conditions:
    - The temperature is less than 800 K.
    - The number of neutrons emitted per second is greater than 500.
    - The product of temperature and neutrons emitted per second is less than 500000.
    """
    product = temperature*neutrons_emitted
    if temperature < 800 and neutrons_emitted > 500 and product < 500000:
        return True
    return False


def reactor_efficiency(voltage, current, theoretical_max_power):
    """Assess reactor efficiency zone.

    :param voltage: int or float - voltage value.
    :param current: int or float - current value.
    :param theoretical_max_power: int or float - power that corresponds to a 100% efficiency.
    :return: str - one of ('green', 'orange', 'red', or 'black').

    Efficiency can be grouped into 4 bands:

    1. green -> efficiency of 80% or more,
    2. orange -> efficiency of less than 80% but at least 60%,
    3. red -> efficiency below 60%, but still 30% or more,
    4. black ->  less than 30% efficient.

    The percentage value is calculated as
    (generated power/ theoretical max power)*100
    where generated power = voltage * current
    """

    generated_power = voltage * current
    #float convert
    print('check a1',generated_power)
    print('check a2',type(generated_power))
    per = (generated_power/theoretical_max_power)*100
    a = float(per)
    print('check a3',a)
    print('check a4',type(a))
    print('check a5',a <= 30)
    print('check a6',a < 60 and a >= 30)
    print('check a7',a < 80 and a >= 60)
    print('chech a8',a >= 80)
    if a == 80 or a > 80:
        print('green')
        return 'green'
    elif a < 80 and a >= 60:
        print('orange')
        return 'orange'
    elif a < 60 and a >= 30:
        print('red')
        return 'red'
    elif a < 30:
        print('black')
        return 'black'
    
   
    
    
    
def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess and return status code for the reactor.

    :param temperature: int or float - value of the temperature in kelvin.
    :param neutrons_produced_per_second: int or float - neutron flux.
    :param threshold: int or float - threshold for category.
    :return: str - one of ('LOW', 'NORMAL', 'DANGER')

    1. 'LOW' -> `temperature * neutrons per second` < 90% of `threshold`
    2. 'NORMAL' -> `temperature * neutrons per second` +/- 10% of `threshold`
    3. 'DANGER' -> `temperature * neutrons per second` is not in the above-stated ranges
    """
    print('debug a1',temperature, neutrons_produced_per_second, threshold)
    new_threshold = 90/100 * threshold
    sec_threshold = 10/100 * threshold
    print('debug a2',new_threshold,type(new_threshold))
    print('debug a3',sec_threshold,type(sec_threshold))
    print('debug a4',temperature * neutrons_produced_per_second < new_threshold)
    print('debug a5',temperature * neutrons_produced_per_second > sec_threshold or temperature * neutrons_produced_per_second < sec_threshold)
    print('debug a6',temperature * neutrons_produced_per_second)
    if temperature * neutrons_produced_per_second < new_threshold:
        print('low')
        return 'LOW'
    elif (temperature * neutrons_produced_per_second > (threshold - sec_threshold) and temperature * neutrons_produced_per_second < threshold) or temperature * neutrons_produced_per_second == threshold or (temperature * neutrons_produced_per_second < (threshold + sec_threshold) and temperature * neutrons_produced_per_second > threshold):
    
        print('NORMAL')
        return 'NORMAL'
    else:
        print('DANGER')
        return 'DANGER'