"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    if (
        temperature < 800
        and neutrons_emitted > 500
        and temperature * neutrons_emitted < 500000
    ):
        return True
    else:
        return False
    pass


def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power = voltage * current
    reactor_efficiency = (generated_power / theoretical_max_power) * 100

    if reactor_efficiency >= 80:
        return "green"
    elif reactor_efficiency >= 60:
        return "orange"
    elif reactor_efficiency >= 30:
        return "red"
    else:
        return "black"
    """Assess reactor efficiency zone.

    Parameters:
        voltage (int or float): Voltage value.
        current (int or float): Current value.
        theoretical_max_power (int or float): The power level that corresponds to a 100% efficiency.

    Returns:
        str: One of ('green', 'orange', 'red', or 'black').

    Note:
        Efficiency can be grouped into 4 bands:
            1. green -> efficiency of 80% or more,
            2. orange -> efficiency of less than 80% but at least 60%,
            3. red -> efficiency below 60%, but still 30% or more,
            4. black ->  less than 30% efficient.

        The percentage value is calculated as
        (generated power/ theoretical max power)*100
        if 
        where generated power = voltage * current
        
    """

    pass


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    valor = temperature * neutrons_produced_per_second

    if valor < threshold * 0.9:
        return "LOW"
    elif valor <= threshold * 1.1:
        return "NORMAL"
    else:
        return "DANGER"
    """Assess and return status code for the reactor.

    Parameters:
        temperature (int or float): The value of the temperature in kelvin.
        neutrons_produced_per_second (int or float): The neutron flux.
        threshold (int or float): The threshold for the category.

    Returns:
        str: One of ('LOW', 'NORMAL', 'DANGER').

    Note:
        1. 'LOW' -> `temperature * neutrons per second` < 90% of `threshold`
        2. 'NORMAL' -> `temperature * neutrons per second` +/- 10% of `threshold`
        3. 'DANGER' -> `temperature * neutrons per second` is not in the above-stated ranges
    """

    pass
