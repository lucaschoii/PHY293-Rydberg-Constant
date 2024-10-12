from calibration import calibrate
import math
from calibration import lambda_0

m, b, merr, berr = calibrate(True)


unknown_y = [7.0, 8.35, 8.65, 9.5, 10.65, 12.85, 14.15, 15.5, 16]
unknown_y_err = [0.15] * len(unknown_y)

unknown_lambda = [m / (y - b) + lambda_0 for y in unknown_y]

denom = [y - b for y in unknown_y]
denom_err = [math.sqrt(yerr**2 + berr**2) for yerr in unknown_y_err]

first_term_err = [m / denom[i] * math.sqrt((denom_err[i] / denom[i])**2 + (merr / m)**2) for i in range(len(denom))]
unknown_lambda_err = [math.sqrt(first_term_err[i]**2 + merr**2) for i in range(len(first_term_err))]

for i, l in enumerate(unknown_lambda):
    print(f"lambda_{i + 1} = {l} +/- {unknown_lambda_err[i]}")