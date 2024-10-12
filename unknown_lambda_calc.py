from calibration import calibrate, lambda_0, lambda_0err
import math

m, b, merr, berr = calibrate(True)


unknown_y = [7.0, 8.35, 8.65, 9.5, 10.65, 12.85, 14.15, 15.5, 16]
unknown_y_err = [0.15] * len(unknown_y)

unknown_lambda = [m / (y - b) + lambda_0 for y in unknown_y]
unknown_lambda_err = [math.sqrt((merr / (y - b))**2 + (-m * unknown_y_err[i] / (y - b)**2)**2 + (m * berr / (y - b)**2)**2 + lambda_0err**2) for i, y in enumerate(unknown_y)]


for i, l in enumerate(unknown_lambda):
    print(f"lambda_{i + 1} = {l} +/- {unknown_lambda_err[i]}")