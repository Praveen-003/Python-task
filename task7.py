#trigonomentry function
import math
n = int(input("Enter the degree:"))
val = math.radians(n)
print("Enter the function need to find trigonometry(sin,cos,tan,asin,acos,atan,sinh,cosh,tanh):")
print("=>")
func=input()
if func == "sin":
    print("Sine of", n, "is", math.sin(val))
else:
    if func == "cos":
        print("Cosine of", n, "is", math.cos(val))
    else:
        if func == "tan":
            print("Tangent of", n, "is", math.tan(val))
        else:
            if func == "asin":
                print("Inverse of sine ", n, "is", math.asin(val))
            else:
                if func == "acos":
                    print("Cosine Inverse of", n, "is", math.acos(val))
                else:
                    if func == "atan":
                        print("Inverse of Tangent ", n, "is", math.atan(val))
                    else:
                        if func == "sinh":
                            print("Hyperbolic Sine of", n, "is", math.sinh(val))
                        else:
                            if func == "cosh":
                                print("Hyperbolic Cosine of", n, "is", math.cosh(val))
                            else:
                                if func == "tanh":
                                    print("Hyperbolic Tangent of", n, "is", math.tanh(val))
                                else:
                                    print("Error:Invalid function")
        print('\n')
