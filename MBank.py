from datetime import date

bank_data = {
    "123456789": {
        "balance": 5000,
        "currency": "USD",
        "date_opened": "2023-01-01",
        "owner": "John Dof"
    },
    "987654321": {
        "balance": 10000,
        "currency": "EUR",
        "date_opened": "2023-02-15",
        "owner": "Jane Smith"
    },
    "567890123": {
        "balance": 2000,
        "currency": "GBP",
        "date_opened": "2023-03-10",
        "owner": "Michael Johnson"
    }
}

transactions = []
transactions_values = []
transactions_by_date = []
transactions_dict = {}
top_transactions_dict = {}
top_transactions_list = []
keychain = []
b = 0

def add_transaction(account_number, amount, optional_arg=None):
    if optional_arg:
        bank_data[account_number]['balance'] += int(amount)
        transactions.append({account_number: [amount, optional_arg]})
        with open('Data.txt', 'a') as file:
            file.write(f'{account_number}: [{amount} {optional_arg}] \n')
        return bank_data
    else:
        bank_data[account_number]['balance'] += int(amount)
        transactions.append({account_number: [amount, str(date.today())]})
        with open('Data.txt', 'a') as file:
            file.write(f'{account_number}: [{amount}, {str(date.today())},] \n')
        return bank_data

def get_account_balance(account_number):
    return bank_data[account_number]['balance']

def analyze_transactions():
    for items in transactions:
        value = list(items.values())
        transactions_values.append(value[0][0])
    print('=============================================')
    print('Общая сумма транзакций: ', sum([abs(v) for v in transactions_values]))
    print('Средняя сумма тразнакций: ', sum(transactions_values)//len(transactions_values))
    print('Максимальная сумма транзакций: ', max(transactions_values))
    print('Минимальная сумма транзакций: ', min([abs(v) for v in transactions_values]))
    print('=============================================')

add_transaction("123456789", 1500, '2023-06-29')
add_transaction("123456789", 1000, '2023-06-29')
add_transaction("123456789", 2000, '2023-06-30')
add_transaction("987654321", -500, '2023-06-30')
add_transaction("987654321", 1200, '2023-06-29')
add_transaction("987654321", 800, '2023-07-1')

def get_transactions_by_date(account_number, start_date, end_date):
    for transaction_data in transactions:
        values = list(transaction_data.values())
        key = list(transaction_data.keys())
        if start_date <= values[0][1] <= end_date and key[0] ==  account_number:
            transactions_by_date.extend(values)
            print(f'Транзакция: дата "{values[0][1]}", сумма "{values[0][0]} {bank_data[account_number]["currency"]}"')


def get_top_accounts(n):
    top_transactions_dict.clear()
    top_transactions_list.clear()

    for transaction in transactions:
        account_number = list(transaction.keys())[0]
        amount = transaction[account_number][0]

        if account_number in top_transactions_dict:
            top_transactions_dict[account_number] += abs(amount)
        else:
            top_transactions_dict[account_number] = abs(amount)

    sorted_transactions = sorted(top_transactions_dict.items(), key=lambda x: x[1], reverse=True)
    top_accounts = sorted_transactions[:n]

    for account, total_amount in top_accounts:
        top_transactions_list.append({
            'account_number': account,
            'total_amount': total_amount,
            'owner': bank_data[account]['owner']
        })
    return top_transactions_list

