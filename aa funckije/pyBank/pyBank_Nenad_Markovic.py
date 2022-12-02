import datetime
import os

company_name = ''
company_street_and_number = ''
company_postal_code = ''
company_city = ''
company_tax_id = ' '
company_manager = ''
currency = ' hr'
transaction_id = 0
transactions = { }
account_number = ''
account_balance = 0.00

def create_deposit():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    global company_name
    global company_street_and_number 
    global company_postal_code
    global company_city
    global company_tax_id
    global company_manager
    global currency
    global transactions
    global transaction_id
    global account_balance
    
    print('*' * 65)
    print('PyBANK ALGEBRA\n'.center(65), '\n')
    print('NOVA UPLATA NA RAČUN\n'.center(65), '\n')
    print(f'Trenutno stanje racuna:\t{account_balance:.2f}{currency}\n')
    print('Molimo Vas upisite iznos koji zelite uplatiti na racun. (EUR ili HRK):\t')

    deposit_amount = input('\t')

    if deposit_amount != '':
        deposit_amount = float(deposit_amount)
        deposit_transaction = []
        transaction_id += 1
        account_balance += deposit_amount
        deposit_transaction.append(datetime.datetime.date)
        deposit_transaction.append(datetime.datetime.time)
        deposit_transaction.append(deposit_amount)
        deposit_transaction.append(account_balance)
        deposit_transaction.append(account_number)
        deposit_transaction.append('Nova uplata na račun')
        deposit_transaction.append(company_manager)
        transactions[transaction_id + 1] = deposit_transaction
    else:
        deposit_amount = 0.00

    print('-' * 65)
    input('Za Povratak u Glavni izbornik pritisnite bilo koju tipku\t')


def create_withdraw():
    os.system('cls' if os.name == 'nt' else 'clear')
    global company_name
    global company_street_and_number 
    global company_postal_code
    global company_city
    global company_tax_id
    global company_manager
    global currency
    global transactions
    global transaction_id
    global account_balance
    
    print('*' * 65)
    print('PyBANK ALGEBRA\n'.center(65), '\n')
    print('NOVA ISPLATA NA RAČUN\n'.center(65), '\n')
    print(f'Trenutno stanje racuna:\t{account_balance:.2f}{currency}\n')
    print('Molimo Vas upisite iznos koji zelite isplatiti s računa. (EUR ili HRK):\t')
    
    withdraw_amount = input('\t')

    if withdraw_amount != '':
        withdraw_amount = float(withdraw_amount)
        withdraw_transaction = []
        transaction_id += 1
        account_balance -= withdraw_amount
        withdraw_transaction.append(datetime.datetime.date)
        withdraw_transaction.append(datetime.datetime.time)
        withdraw_transaction.append(withdraw_amount)
        withdraw_transaction.append(account_balance)
        withdraw_transaction.append(account_number)
        withdraw_transaction.append('Nova uplata na račun')
        withdraw_transaction.append(company_manager)
        transactions[transaction_id + 1] = withdraw_transaction
    else:
        withdraw_amount = 0.00

    print('-' * 65)
    input('Za Povratak u Glavni izbornik pritisnite bilo koju tipku\t')


def generate_account_number():
    global account_number

    year = datetime.datetime.now().year
    month = datetime.datetime.now().month

    if month < 10:
        month = str('0' + str(month))
    else:
        month = str(month)
    if account_number == '':
        account_number = 'BA-' + str(year) + '-' + month + '-00001'
    else:
        number_str = account_number.split('-')[-1]
        number = int(number_str)
        if number < 9:
            number += 1
            account_number = 'BA-' + str(year) + '-' + month + '-0000' + str(number)
        elif number < 99:
            number += 1
            account_number = 'BA-' + str(year) + '-' + month + '-000' + str(number)
        elif number < 999:
            number += 1
            account_number = 'BA-' + str(year) + '-' + month + '-00' + str(number)
        elif number < 9999:
            number += 1
            account_number = 'BA-' + str(year) + '-' + month + '-0' + str(number)
        else:
            number += 1
            account_number = 'BA-' + str(year) + '-' + month + '-' + str(number)
    return account_number


def open_account():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('*' * 65)
    print('PyBANK ALGEBRA\n'.center(65), '\n')
    print('KREIRANJE RACUNA\n'.center(65))
    print('Podaci o vlasniku racuna\n'.center(65))

    global company_name
    global company_street_and_number 
    global company_postal_code
    global company_city
    global company_tax_id
    global company_manager
    global currency
    global transactions
    global account_balance
    global choice

    company_name = input('Naziv Tvrtke:\t\t\t\t')
    company_street_and_number = input('Ulica i broj sjedista Tvrtke:\t\t')
    company_postal_code = input('Postanski broj sjedista Tvrtke:\t\t')
    company_city = input('Grad u kojem je sjediste Tvrtke:\t')

    while True:
        company_tax_id = input('OIB Tvrtke:\t\t\t\t')
        if len(company_tax_id) != 11 and company_tax_id.isdigit():
            print('OIB mora imati tocno 11 znamenki i moraju biti samo brojke.\nMolimo Vas ponovite unos\n')
        else:
            break
    company_manager = input('Ime i prezime odgovorne osobe Tvrtke:\t')
    print()
    currency = input('Upisite naziv valute racuna (EUR ili HRK):\t')
    if currency.upper() == 'HRK':
        currency = ' hr'
    else:
        currency = ' €'
    
    input('\nSPREMI? (Pritisnite bilo koju tipku) ')
    os.system('cls' if os.name == 'nt' else 'clear')
    print('*' * 65)
    print('PyBANK ALGEBRA\n'.center(65), '\n')
    print('KREIRANJE RACUNA\n'.center(65))
    print(f'Podaci o vlasniku racuna tvrtke {company_name}, su uspjesno spremljeni.')
    input('Za nastavak pritisnite bilo koju tipku\t')
    os.system('cls' if os.name == 'nt' else 'clear')
    print('*' * 65)
    print('PyBANK ALGEBRA\n'.center(65), '\n')
    print('KREIRANJE RACUNA\n'.center(65))
    print('Stanje racuna\n'.center(65), '\n')
    print(f'Broj racuna {generate_account_number()}')
    print(f'Trenutno stanje racuna:\t{account_balance:.2f}{currency}\n')

    print('Molimo Vas upisite iznos koji zelite poloziti na racun.\nNAPOMENA Molimo Vas koristite decimalnu tocku, a ne zarez.\n')
    amount = input('\t')
    if amount != '':
        amount = float(amount)
        transaction = []
        account_balance += amount
        transaction.append(datetime.datetime.date)
        transaction.append(datetime.datetime.time)
        transaction.append(amount)
        transaction.append(account_balance)
        transaction.append(account_number)
        transaction.append('Polog kod otvaranja racuna')
        transaction.append(company_manager)
        transactions[transaction_id + 1] = transaction
    else:
        amount = 0.00
    choice = -1


def update_account():
    #os.system('cls' if os.name == 'nt' else 'clear')
    global company_name
    global company_street_and_number 
    global company_postal_code
    global company_city
    global company_tax_id
    global company_manager
    global currency
    global transactions
    global account_balance

    print('*' * 65)
    print('PyBANK ALGEBRA\n'.center(65), '\n')
    print('AŽURIRANJE RACUNA\n'.center(65))
    print('Ažuriranje računa po koracima: \n'.center(65))

    company_name = input('Naziv Tvrtke:\t\t\t\t')
    company_street_and_number = input('Ulica i broj sjedista Tvrtke:\t\t')
    company_postal_code = input('Postanski broj sjedista Tvrtke:\t\t')
    company_city = input('Grad u kojem je sjediste Tvrtke:\t')

    while True:
        company_tax_id = input('OIB Tvrtke:\t\t\t\t')
        if len(company_tax_id) != 11 and company_tax_id.isdigit():
            print('OIB mora imati tocno 11 znamenki i moraju biti samo brojke.\nMolimo Vas ponovite unos\n')
        else:
            break

    company_manager = input('Ime i prezime odgovorne osobe Tvrtke:\t')
    print()

    currency = input('Upisite naziv valute racuna (EUR ili HRK):\t')

    if currency.upper() == 'HRK':
        currency = ' hr'
    else:
        currency = ' €'
    
    input('\nSPREMI? (Pritisnite bilo koju tipku) ')
    os.system('cls' if os.name == 'nt' else 'clear')
    print('*' * 65)
    print('PyBANK ALGEBRA\n'.center(65), '\n')
    print('AŽURIRANJE RACUNA\n'.center(65))
    print(f'Podaci o vlasniku racuna tvrtke {company_name}, su uspjesno ažurirani.')
    print('-' * 65)
    input('Za Povratak u Glavni izbornik pritisnite bilo koju tipku\t')


def main_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    choice = -1
    print('*' * 65)
    print('PyBANK ALGEBRA\n'.center(65), '\n')
    print('GLAVNI IZBORNIK\n'.center(65))

    if company_name == '':
        print('1. Kreiranje racuna')
    else:
        print('1. Azuriranje racuna')
    print('2. Prikaz stanja racuna')
    print('3. Prikaz prometa po racunu')
    print('4. Polog novca na racun')
    print('5. Podizanje novca s racuna')
    print('0. Izlaz')
    print('_' * 65)
    if company_name == '':
        while choice != 1 and choice != 0:
            print('Jos niste otvorili racun. Molimo prvo kreirajte racun. Hvala!')
            print('-' * 65)
            choice = int(input('Vas izbor:\t'))
            print()
    else:
        print('Molimo Vas upisite samo broj ispred opcije koju zelite odabrati')
        print('-' * 65)
        choice = int(input('Vas izbor:\t'))
        print()
    return choice

def display_account_balance():
    os.system('cls' if os.name == 'nt' else 'clear')

    print('*' * 65)
    print('PyBANK ALGEBRA\n'.center(65), '\n')
    print('PRIKAZ STANJA RACUNA\n'.center(65), '\n')
    print(f'Broj racuna:\t{account_number}')
    print(f'Broj racuna:\t{company_name}')
    print(f'Datum i vrijeme:\t{datetime.datetime.today()} {datetime.datetime.now()}\n')
    print(f'Trenutno stanje racuna:\t{account_balance:.2f}{currency}\n\n')
    print('-' * 65)
    input('Za Povratak u Glavni izbornik pritisnite bilo koju tipku\t')

def display_account_transactions():
    print('*' * 65)
    print('PyBANK ALGEBRA\n'.center(65), '\n')
    print('PRIKAZ PROMETA PO RAČUNU\n'.center(65), '\n')
    print(f'Broj racuna:\t{account_number}')
    print(f"{transactions}") ##

    for i in transactions:
        print(f"ID transakcije: {i}")
        print(f"Iznos transakcije: {transactions[i][2]}")
        print(f"Iznos na računu: {transactions[i][3]}")
        print(f"Broj računa: {transactions[i][4]}")
        print(f"Opis transakcije: {transactions[i][5]}")
        print(f"Odgovorna osoba: {transactions[i][6]}")
        print('-' * 40)

    print('-' * 65)
    input('Za Povratak u Glavni izbornik pritisnite bilo koju tipku\t')


choice = main_menu()

while choice != 0:
    if choice == 1 and company_name == '':
        open_account()
    if choice == 1 and company_name != '':
        update_account()
    if choice == 2:
        display_account_balance()
    elif choice == 3:
        display_account_transactions()
    elif choice == 4:
        create_deposit()
    elif choice == 5:
        create_withdraw()
    else:
        pass
    
    choice = main_menu()