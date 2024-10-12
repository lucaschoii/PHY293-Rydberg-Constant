from calibration import calibrate, lambda_0, lambda_0err
import math

m, b, merr, berr = calibrate(plot=False)

sodium_y = [8.85, 8.65]
sodium_y_err = [0.15] * len(sodium_y)

sodium_lambda = [m / (y - b) + lambda_0 for y in sodium_y]
sodium_lambda_err = [math.sqrt((merr / (y - b))**2 + (-m * sodium_y_err[i] / (y - b)**2)**2 + (m * berr / (y - b)**2)**2 + lambda_0err**2) for i, y in enumerate(sodium_y)]


for i, l in enumerate(sodium_lambda):
    print(f"sodium_lambda_{i + 1} = {l} +/- {sodium_lambda_err[i]}")

separation = sodium_lambda[1] - sodium_lambda[0]
separation_err = math.sqrt(sum(s**2 for s in sodium_lambda_err))
print(f"separation, nm = {separation} +/- {separation_err}")


