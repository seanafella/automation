class BankAccount:

  def __init__(self, account_holder, balance):
    self.account_holder = account_holder
    self.balance = balance

  def deposit(self, amount):
    """Add the specified amount to the balance."""
    if amount > 0:
        self.balance += amount
    else:
        print("Deposit amount must be positive.")

  def withdraw(self, amount):
      """Subtract the specified amount from the balance if sufficient funds are available."""
      if amount > self.balance:
          print("Insufficient funds.")
      elif amount > 0:
          self.balance -= amount
      else:
          print("Withdrawal amount must be positive.")

  def get_balance(self):
      """Return the current balance."""
      return self.balance