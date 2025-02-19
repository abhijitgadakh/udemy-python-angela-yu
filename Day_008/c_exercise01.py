import math

def paint_calc(coverage, test_h, test_w):
    area = test_h * test_w
    require_cans = math.ceil(area / coverage)
    print(f'You need {require_cans} cans to paint the wall')




test_h = int(input("Enter Height of wall (m): "))
test_w = int(input("Enter Width of wall (m): "))

coverage = 5

paint_calc(coverage, test_h, test_w)
