import fit_black_box as bb
import math
import numpy as np

def linear (m, x, b):
    return m * x + b

init_guess = (0, 1)
font_size = 20
xlabel = "(lambda - lambda_0)^-1"
ylabel = "y"
title = "Callibration"

lambda_0 = 286.0
lambda_0err = 2.0
wavelength = [447.1, 471.3, 492.2, 501.6, 587.6, 667.8, 434.0, 486.1, 656.3]
y = np.array([13.0, 11.85, 11.5, 11.25, 8.85, 7.5, 15.65, 12.15, 7.65])

x_inv = [w - lambda_0 for w in wavelength]

x = np.array([1.0 / x for x in x_inv])
xerr = np.array([0.0001] * len(x))
yerr = np.array([0.01] * len(y))



popt, puncert = bb.plot_fit(linear, x, y, xerr, yerr, init_guess=init_guess, font_size=font_size, title=title,
            xlabel=xlabel, ylabel=ylabel)

m, b = popt
merr, berr = puncert

