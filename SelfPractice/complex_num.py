# Method 1: Literal syntax
z=3+4j
print(z.real)
print(z.imag)
print(abs(z))

    #OR
# Method 2: complex(real, imag) constructor
x=complex(2,-6)
print(x.real)
print(x.imag)
print(abs(x))   #This performs the calculation the squar root of {real^2 + imag^2}

#Use the .conjugate() method to flip the sign of the imaginary part.
print(z.conjugate())
print(x.conjugate())
