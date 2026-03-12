from custom_classes import Calculator

if __name__ == "__main__":
    calc = Calculator()
    
    # Example operation: (10 + 5) * 2 / 3
    calc.add(10, 5)
    calc.multiply(calc._current_val, 2)
    calc.divide(calc._current_val, 3)
    
    print(f"Final Result of (10+5)*2/3 is: {calc._current_val}")