try:
    # Code that may raise an exception
    x = int(input("Enter a number: "))
    result = 10 / x
    print("Result:", result)

except ValueError:
    print("Invalid input. Please enter a valid number.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

except Exception as e:
    print("An error occurred:", str(e))

else:
    print("No exceptions occurred.")

finally:
    print("Execution completed.")

