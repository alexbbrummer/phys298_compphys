# %% [markdown]
# # Week 01 (Tue) — Intro + your first physics script
#
# Today we’ll:
# - get comfortable running a script
# - use variables + units
# - compute something familiar (constant acceleration)

# %% [markdown]
# ## A tiny “physics calculator”
# We’ll compute the range for a projectile launched from level ground (no drag):
#
# \[
# R = \frac{v_0^2 \sin(2\theta)}{g}
# \]
#
# Later we’ll replace this with a numerical simulation.

# %%
import numpy as np

g = 9.81  # m/s^2
v0 = 12.0 # m/s
theta_deg = 35.0

theta = np.deg2rad(theta_deg)
R = (v0**2 * np.sin(2*theta)) / g
R

# %% [markdown]
# ## Quick check
# Change `theta_deg` to 45° and confirm you get the maximum range.

# %%
theta_deg = 45.0
theta = np.deg2rad(theta_deg)
R = (v0**2 * np.sin(2*theta)) / g
R
