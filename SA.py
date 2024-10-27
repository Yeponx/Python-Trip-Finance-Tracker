# SA.py
import Moneyleft as ML

def sa(i):
    # Convert current `Owes` balance to an integer
    h = int(ML.Owes)
    a = h - i  # Subtract `i` from the current balance
    ML.Owes = str(a)  # Update `Owes` in the Moneyleft module

    # Save updated balance to file
    with open('Moneyleft.py', 'w') as f:
        f.write(f"Owes = '{ML.Owes}'\n")
