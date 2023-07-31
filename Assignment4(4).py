"""Q:7 How Do You Handle Exceptions With Try/Except/Finally In Python? Explainwith coding
    snippets.
    A:7 therer are four types of exception in exception handling:-
    try: when the code inside try block will run successfully
    except: if try block does'nt run the except block will be executed
    else: if try block will run successfully then else will be defaultly executed
    finally: this block will run in every situation(wather the condition gets
	run or not)"""
   # --> code :-
try:
    print("Value = ",u)
except Exception as e:
    print("Error:",e)

print("========================================")

# Write python program that user to enter only odd numbers, else will raise an exception. 
def get_odd_number():
    while True:
        try:
            num = int(input("Enter an odd number: "))
            if num % 2 != 1:
                raise ValueError("You must enter an odd number.")
            return num
        except ValueError as e:
            print(f"Invalid input: {e}")


if __name__ == "__main__":
    try:
        odd_number = get_odd_number()
        print(f"You entered an odd number: {odd_number}")
    except KeyboardInterrupt:
        print("\nOperation interrupted by the user.")
    except Exception as e:
        print(f"An error occurred: {e}")

