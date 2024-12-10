def extended_euclidean_algorithm(a, b):
    """
    Implements the extended Euclidean algorithm.
    Finds the greatest common divisor (GCD) of two integers a and b,
    along with Bézout coefficients x and y such that:
        a * x + b * y = gcd(a, b)
    
    Parameters:
    a (int): First integer.
    b (int): Second integer.
    
    Returns:
    tuple: (gcd, x, y) where:
           - gcd is the greatest common divisor of a and b,
           - x and y are Bézout coefficients.
    """
    if b == 0:
        # Base case: gcd(a, 0) = a, Bézout coefficients x = 1, y = 0.
        return a, 1, 0
    
    # Recursively calculate gcd and coefficients for smaller inputs
    gcd, x1, y1 = extended_euclidean_algorithm(b, a % b)
    
    # Update Bézout coefficients
    x = y1
    y = x1 - (a // b) * y1
    
    return gcd, x, y


# Example usage:
if __name__ == "__main__":
    a = int(input("enter a: "))
    b = int(input("enter b: "))
    gcd, x, y = extended_euclidean_algorithm(a, b)
    
    print(f"The GCD of {a} and {b} is: {gcd}")
    print(f"Bézout coefficients are: x = {x}, y = {y}")
    print(f"Verification: {a} * {x} + {b} * {y} = {gcd}")