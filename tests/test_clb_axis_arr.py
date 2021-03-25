import pyspacemouse
import time


pyspacemouse.open(dof_callback_arr=[
    pyspacemouse.DofCallback("x", lambda state, axis: print(f"X plus {axis}"), 0.01, lambda state, axis: print(f"X minus {axis}")),
    pyspacemouse.DofCallback("y", lambda state, axis: print(f"Y plus {axis}"), 0.01, lambda state, axis: print(f"Y minus {axis}"), 0.5),
])


while True:
    out = pyspacemouse.read()
    # print(out.x)
    time.sleep(0.0001)

