import fit_black_box as bb
import math
import numpy as np

lambda_0 = 286.0
lambda_0err = 2.0
wavelength = [447.1, 471.3, 492.2, 501.6, 587.6, 667.8, 434.0, 486.1, 656.3]
wav_err = [0.0000022, 0.0000024, 0.0000025, 0.000003, 0.000003, 0.000003, 0.0006, 0.0000024, 0.000007]

def linear (m, x, b):
    return m * x + b

def calibrate(plot):

    init_guess = (0, 1)
    font_size = 20
    xlabel = "(lambda - lambda_0)^-1 [nm^-1]"
    ylabel = "y"
    title = "Calibration"


    y = np.array([13.0, 11.85, 11.5, 11.25, 8.85, 7.5, 15.65, 12.15, 7.65])
    x_inv = [w - lambda_0 for w in wavelength]
    x = np.array([1.0 / x for x in x_inv])

    yerr = np.array([0.15] * len(y))
    xerr = [math.sqrt(wav_err[i]**2 + lambda_0err**2) / (wavelength[i] - lambda_0)**2 for i in range(len(wavelength))]

    if plot:

        (m, b), (merr, berr) = bb.plot_fit(linear, x, y, xerr, yerr, init_guess=init_guess, font_size=font_size, title=title,
                    xlabel=xlabel, ylabel=ylabel)
    
    else:
        (m, b), (merr, berr) = bb.fit(linear, x, y, xerror=xerr, yerror=yerr, init_guess=init_guess)
    
    return m, b, merr, berr


