previous_mode = None
def control(temp, people):
    global previous_mode
    if people == 0:
        target = "OFF"
    elif temp < 18:
        target = "HEAT"
    elif temp > 25:
        target = "COOL"
    else:
        target = "OFF"
    command = target != previous_mode
    previous_mode = target
    return target, command
tests = [
    (20, 1),
    (20, 1),
    (18, 1),
    (25, 1),
    (27, 1),
    (27, 1),
    (22, 0)
]
for temp, people in tests:
    old = previous_mode
    target, command = control(temp, people)
    print("Previous:", old,
      "| Percept:", temp, people,
      "| Target:", target,
      "| Result:", "SEND" if command else "NO COMMAND")
