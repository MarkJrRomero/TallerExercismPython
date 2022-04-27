def is_criticality_balanced(temperature, neutrons_emitted):
    if temperature >= 800 or neutrons_emitted <= 500:
        return False
    else:
        if temperature * neutrons_emitted < 500000:
            return True
        else:
            return False
def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power = voltage * current
    percentage_value = (generated_power / theoretical_max_power)*100
    if percentage_value >= 80:
        return "green"
    elif percentage_value >= 60:
        return "orange"
    elif percentage_value >= 30:
        return "red"
    else:
        return "black"
def fail_safe(temperature, neutrons_produced_per_second, threshold):
    if temperature * neutrons_produced_per_second < (0.9*threshold):
        return "LOW"
    elif (threshold * 0.9) <= temperature * neutrons_produced_per_second and (threshold*1.1) >= temperature * \
            neutrons_produced_per_second:
        return "NORMAL"
    else:
        return "DANGER"
