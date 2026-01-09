# %% [markdown]
# # Week 01 (Thu Lab) — First steps + translating formulas into code
#
# **Goal:** Write a script that computes and prints a few physics quantities with units.
#
# Work in pairs. One person “drives”, the other “navigates”.

# %% [markdown]
# ## Task A — Basic calculations
# Compute:
# - kinetic energy: \(K = \tfrac12 m v^2\)
# - gravitational potential change: \(\Delta U = m g \Delta y\)

# %%
g = 9.81  # m/s^2

m = 0.150   # kg
v = 8.0     # m/s
dy = 1.2    # m

# TODO: compute K and dU
K = 0.5 * m * v**2
dU = m * g * dy

print("K =", K, "J")
print("ΔU =", dU, "J")

# %% [markdown]
# ## Task B — Make it reusable with a function
# Write a function `kinetic_energy(m, v)` that returns \(\tfrac12 m v^2\).

# %%
def kinetic_energy(m, v):
    """Return kinetic energy (J) for mass m (kg) and speed v (m/s)."""
    return 0.5 * m * v**2

print(kinetic_energy(0.150, 8.0))

# %% [markdown]
# ## Task C — Challenge
# Ask the user for `m` and `v` (input), compute K, and print a friendly sentence.
# (Remember: `input()` returns a string; convert to `float`.)
