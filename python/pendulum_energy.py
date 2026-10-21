"""Inverted pendulum pivoting at the wrists, no control torque (tau = 0).

Integrates  I * theta'' = m*g*h*sin(theta)  with a 4th-order Runge-Kutta scheme
and plots kinetic, potential and total energy over time.

Run:  python pendulum_energy.py
"""
import numpy as np
import matplotlib.pyplot as plt

g = 9.81            # gravitational acceleration (m/s^2)
L = 1.8             # body length, modelled as a uniform rod (m)
h = L / 2           # pivot-to-centre-of-mass distance (m)
k = g * h / (L**2 / 3)   # mgh / I for a uniform rod pivoting at one end (1/s^2)

theta0 = np.radians(10)  # initial tilt
dt = 0.001               # time step (s)
theta_end = np.radians(80)


def deriv(state):
    theta, omega = state
    return np.array([omega, k * np.sin(theta)])


def rk4_step(state, dt):
    a = deriv(state)
    b = deriv(state + dt / 2 * a)
    c = deriv(state + dt / 2 * b)
    d = deriv(state + dt * c)
    return state + dt / 6 * (a + 2 * b + 2 * c + d)


state = np.array([theta0, 0.0])
t, theta, omega = [0.0], [theta0], [0.0]
while theta[-1] < theta_end:
    state = rk4_step(state, dt)
    t.append(t[-1] + dt)
    theta.append(state[0])
    omega.append(state[1])

t, theta, omega = map(np.array, (t, theta, omega))

# energies normalised by m*g*h
Ep = np.cos(theta)
Ek = omega**2 / (2 * k)
E = Ep + Ek

print(f"Fall time from 10 to 80 degrees: {t[-1]:.2f} s")
print(f"Max energy drift: {np.ptp(E):.2e}")

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(t, Ep, "k", label="$E_p$")
ax.plot(t, Ek, "k--", label="$E_k$")
ax.plot(t, E, "k", lw=3, label="$E = E_k + E_p$")
ax.set_xlabel("t (s)")
ax.set_ylabel("Energy (normalised by mgh)")
ax.legend(frameon=False)
for side in ("top", "right"):
    ax.spines[side].set_visible(False)
fig.tight_layout()
fig.savefig("../assets/img/pendulum_energy.png", dpi=150)
print("Saved ../assets/img/pendulum_energy.png")
