# MicroBank: Professional Bank Account Processor with Mini-Statement
# Reads transactions from input.py in the same folder

import os

def process_transactions(file_path):
    """
    Reads a transaction file, calculates running balance, 
    and returns a list of transactions with updated balances.
    """
    transactions = []
    balance = 0.0
    
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue  # Skip empty lines or comments
                
                try:
                    date_str, transaction_type, amount_str = line.split(',')
                    transaction_type = transaction_type.strip().lower()
                    amount = float(amount_str.strip())
                except ValueError:
                    print(f"Warning: Skipping invalid line: {line}")
                    continue
                
                if transaction_type == 'deposit':
                    balance += amount
                elif transaction_type == 'withdrawal':
                    balance -= amount
                else:
                    print(f"Warning: Unknown transaction type '{transaction_type}' on {date_str}")
                    continue
                
                transactions.append({
                    'date': date_str.strip(),
                    'type': transaction_type.title(),
                    'amount': amount,
                    'balance': balance
                })
        
        return transactions
    
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []


def print_statement(transactions):
    """
    Prints a professional mini-statement of transactions.
    """
    print("-------- MicroBank Mini-Statement --------")
    print(f"{'Date':<12} {'Type':<12} {'Amount':>10} {'Balance':>12}")
    print("-" * 48)
    for tx in transactions:
        print(f"{tx['date']:<12} {tx['type']:<12} ${tx['amount']:>9.2f} ${tx['balance']:>11.2f}")
    print("-" * 48)
    if transactions:
        print(f"Final Balance: ${transactions[-1]['balance']:.2f}")
    else:
        print("No transactions to display.")
    print("-----------------------------------------\n")


def main():
    # Automatically find input.data in the same folder as this script
    script_folder = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(script_folder, "input.data")  # Using your existing file name
    
    transactions = process_transactions(input_file)
    print_statement(transactions)


if __name__ == "__main__":
    main()