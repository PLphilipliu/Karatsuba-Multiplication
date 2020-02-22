import math

x = int(input("First number:"))
y = int(input("Second number:"))

#x = 3141592653589793238462643383279502884197169399375105820974944592
#y = 2718281828459045235360287471352662497757247093699959574966967627

def grade_school (fac1, fac2):
    mul = fac1 * fac2
    return mul

def karatsuba_multiplication (fac1, fac2):
    if len(str(fac1)) == 1 or len(str(fac2)) == 1:
        return fac1 * fac2
    else:
        power_digit = 10 ** int(math.log10(fac1) / 2.0 + 0.5)
        fac1_a = fac1 // power_digit
        fac1_b = fac1 % power_digit
        fac2_c = fac2 // power_digit
        fac2_d = fac2 % power_digit

        z1 = karatsuba_multiplication(fac1_a, fac2_c)
        z2 = karatsuba_multiplication(fac1_b, fac2_d)
        z3 = karatsuba_multiplication(fac1_a + fac1_b, fac2_c + fac2_d) - z2 - z1

        return (power_digit * power_digit * z1 + power_digit * z3 + z2)

result1 = karatsuba_multiplication(x, y)
result2 = grade_school(x, y)

print("Karatsuba Algorithm:", result1)
print("Grade School:", result2)