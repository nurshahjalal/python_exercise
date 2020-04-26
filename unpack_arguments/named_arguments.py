# https://www.udemy.com/the-complete-python-course/learn/v4/t/lecture/9477756?start=600
accounts = {
    'checking': 1958.00,
    'savings': 3695.00
}


def add_balance(amount: float, name: str) -> float:
    """ Function to update balance of an account and return the new balance
    """
    accounts[name] += amount
    return accounts[name]


transactions = [
    (-180.67, 'checking'),
    (-220.00, 'checking'),
    (220.00, 'checking'),
    (-15.70, 'savings'),
    (1579.50, 'checking'),
    (-600.50, 'checking'),
    (600.50, 'savings')
]

# regular and popular way
for t in transactions:
    add_balance(t[0], t[1])


# same thing can be done with named argument

for t in transactions:
    new_balance = add_balance(amount=t[0], name=t[1])

    # can be put arguments in any order
    new_balance_1 = add_balance(name=t[1], amount=t[0] )





