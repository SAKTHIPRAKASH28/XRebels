
def calculate_energy_savings(yesterday, today):
    total_savings = 0
    for appliance, consumption_today in today.items():
        if appliance in yesterday:
            consumption_yesterday = yesterday[appliance]
            savings = consumption_yesterday - consumption_today
            total_savings += savings
    return total_savings


def calculate_points(savings):
    points = 0
    if savings > 0:
        points += int(savings * 10)
        if savings > 1:

            bonus_points = int((savings - 1) * 5)
            points += bonus_points
    else:
        points -= 1
    return points
