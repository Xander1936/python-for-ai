# helpers.py

def calculate_total(quantity, price):
    """Calculate total for a single item"""
    return quantity * price

def format_currency(amount):
    """Format number as currency"""
    return f"${amount:,.2f}" # We just want 2 Decimal places for the amount and a dollar sign