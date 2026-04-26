class BankingSystem:
    def __init__(self):
        self.accounts = {}
        self.outgoing_transactions = {}
        self.payments = {}
        self.payment_number = 0
        
    def create_account(self, timestamp: int, account_id: str) -> bool:
        if account_id in self.accounts:
            return False
        # Create a new account with zero money
        self.accounts[account_id] = 0
        self.outgoing_transactions[account_id] = 0
        return True
    
    def deposit(self, timestamp: int, account_id: str, amount: int) -> int:
        if account_id not in self.accounts:
            return None
        
        # Process any pending cashback before proceeding with the deposit
        for payment_id, payment_info in self.payments.items():
            if payment_info['account_id'] == account_id and payment_info['status'] == 'IN_PROGRESS':
                # If the cashback is due, apply it to the account balance
                if timestamp >= payment_info['cashback_due']:
                    self.accounts[account_id] += payment_info['cashback_amount']
                    payment_info['status'] = 'CASHBACK_RECEIVED'
        
        # Now proceed with the deposit
        self.accounts[account_id] += amount
        return self.accounts[account_id]
    
    def transfer(self, timestamp: int, source_account_id: str, target_account_id: str, amount: int) -> int:
        if source_account_id not in self.accounts or target_account_id not in self.accounts:
            return None
        if self.accounts[source_account_id] < amount:
            return None
        if source_account_id == target_account_id:
            return None
        self.accounts[source_account_id] -= amount
        self.accounts[target_account_id] += amount
        self.outgoing_transactions[source_account_id] += amount 
        return self.accounts[source_account_id]
        
    
    def top_spenders(self, timestamp: int, n: int) -> list:
        # Sort by outgoing transactions (descending) or by account_id (ascending) for ties
        sorted_accounts = sorted(
            self.outgoing_transactions.items(),
            key=lambda x: (-x[1], x[0])  
        )
        # Print the results
        result = [f"{account_id}({total_outgoing})" for account_id, total_outgoing in sorted_accounts[:n]]
        return result
    
    
    def pay(self, timestamp: int, account_id: str, amount: int) -> str:
        if account_id not in self.accounts:
            return None
    
        # Process any pending cashback before checking if the account has sufficient funds
        for payment_id, payment_info in self.payments.items():
                if payment_info['account_id'] == account_id and payment_info['status'] == 'IN_PROGRESS':
                    # Apply cashback if the current timestamp is >= cashback due time
                    if timestamp >= payment_info['cashback_due']:
                        self.accounts[account_id] += payment_info['cashback_amount']
                        payment_info['status'] = 'CASHBACK_RECEIVED'

        # Now, check if the account has sufficient funds for the payment after processing cashback
        if self.accounts[account_id] < amount:
            return None

        # Withdraw money
        self.accounts[account_id] -= amount
        self.outgoing_transactions[account_id] += amount 
        
        # Schedule cash back
        cashback_amount = (2 * amount) // 100  # 2% cashback, rounded down to integers
        
        self.payment_number += 1
        payment_id = f"payment{self.payment_number}"
        
        self.payments[payment_id] = {
            "timestamp": timestamp,
            "account_id": account_id,
            "amount": amount,
            "cashback_amount": cashback_amount,
            "cashback_due": timestamp + 86400000,  # Cashback due in 1 day (in seconds)
            "status": "IN_PROGRESS"
        }
        
        return payment_id
        
    
    def get_payment_status(self, timestamp: int, account_id: str, payment: str) -> str:
        if account_id not in self.accounts:
            return None
        if payment not in self.payments:
            return None
        payment_info = self.payments[payment]
        if payment_info['account_id'] != account_id:
            return None
            
        # Process cashback if the due time has passed
        if timestamp >= payment_info['cashback_due'] and payment_info['status'] == 'IN_PROGRESS':
            self.accounts[account_id] += payment_info['cashback_amount']
            payment_info['status'] = 'CASHBACK_RECEIVED'
            
        return payment_info['status']


    def merge_accounts(self, timestamp: int, account_id_1: str, account_id_2: str) -> bool:
        # Preconditions: The accounts must be different, and both must exist
        if account_id_1 == account_id_2 or account_id_1 not in self.accounts or account_id_2 not in self.accounts:
            return False
        
        # Process any pending cashback refunds for account_id_2
        for payment_id, payment_info in self.payments.items():
            if payment_info['account_id'] == account_id_2 and payment_info['status'] == 'IN_PROGRESS':
                if timestamp >= payment_info['cashback_due']:
                    # Transfer cashback from account_id_2 to account_id_1
                    self.accounts[account_id_1] += payment_info['cashback_amount']
                    payment_info['account_id'] = account_id_1  # Reassign to account_id_1
                    payment_info['status'] = 'CASHBACK_RECEIVED'

        # Merge balances
        self.accounts[account_id_1] += self.accounts[account_id_2]
        
        # Merge outgoing transactions
        if account_id_2 in self.outgoing_transactions:
            self.outgoing_transactions[account_id_1] += self.outgoing_transactions[account_id_2]
        
        # Remove account_id_2 from the system
        del self.accounts[account_id_2]
        del self.outgoing_transactions[account_id_2]

        # Reassign payment histories of account_id_2 to account_id_1
        for payment_id, payment_info in self.payments.items():
            if payment_info['account_id'] == account_id_2:
                payment_info['account_id'] = account_id_1
        
        return True
    

    def get_balance(self, timestamp: int, account_id: str, time_at: int) -> int:
        # Check if the account existed at the given timestamp
        if account_id not in self.accounts:
            return None
        
        # Process pending cashback if due before the requested time
        for payment_id, payment_info in self.payments.items():
            if payment_info['account_id'] == account_id and payment_info['status'] == 'IN_PROGRESS':
                if time_at >= payment_info['cashback_due']:
                    self.accounts[account_id] += payment_info['cashback_amount']
                    payment_info['status'] = 'CASHBACK_RECEIVED'
        
        # If the timestamp is at or after the queried time, return the current balance
        if timestamp >= time_at:
            return self.accounts[account_id]
        
        # Otherwise, return None if the account didn't exist at that time
        return None
