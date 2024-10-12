from calibration import calibrate

s1 = 8.85 * 10 ** -9
s2 = 8.65 * 10 ** -9

diff = s1 - s2  


m, b, merr, berr = calibrate(plot=False)
print(m, b, merr, berr)

