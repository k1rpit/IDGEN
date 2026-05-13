from faker import Faker
import sys
END = '\033[0m'

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
PURPLE = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'


def dox():
    nik = fake.user_name()
    name = fake.name()
    ctrana = fake.country()
    cite = fake.city()
    street_address = fake.street_address()
    email = fake.email()
    job = fake.job()
    ipv4 = fake.ipv4()
    phone_number = fake.phone_number()
    license_plate = fake.license_plate()
    print(f'''{BLUE}
    [+]📌📄 ⚙️  log ⚙️   📄📌[+]
    [+]👤UserNmae->{nik}
    [+]👤Name->{name}
    [+]🌍country->{ctrana}
    [+]🏙️city->{cite}
    [+]🏠adress->{street_address}
    [+]📧email->{email}
    [+]💼job->{job}
    [+]🌐ipv4->{ipv4}
    [+]📞phone_number->{phone_number}
    [+]🚗license_plate->{license_plate}
   {END} ''')

def start_now():
    print(f'''{CYAN}
++++++++++++++++++++
▀█▀ █▀▄ ▄▀▀ █▀▀ █▄░█
░█░ █░█ █░█ █▀▀ █▀██
▀▀▀ ▀▀░ ░▀▀ ▀▀▀ ▀░░▀ 
++++++++++++++++++++
  {END}  ''')
    user_la = input('you russia?[y/n]>>')
    if user_la == 'y':
        fake = Faker('ru_RU')
        return fake
    else:
        fake = Faker('en_US')
        return fake
fake = start_now()
def help():
    print(f'''{WHITE}
    [1]-generator🔮
    [2]-k1rpit💀
    [0]-exit⛔
   {END} ''')

def k1():
    print(f'''{RED}
+++++++++++++++++++++++++++++++++++++++++++
██╗░░██╗░░███╗░░██████╗░██████╗░██╗████████╗
██║░██╔╝░████║░░██╔══██╗██╔══██╗██║╚══██╔══╝{BLUE}
█████═╝░██╔██║░░██████╔╝██████╔╝██║░░░██║░░░
██╔═██╗░╚═╝██║░░██╔══██╗██╔═══╝░██║░░░██║░░░
██║░╚██╗███████╗██║░░██║██║░░░░░██║░░░██║░░░{YELLOW}
╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░░╚═╝░░░
++++++++++++++++++++++++++++++++++++++++++++
{GREEN}
version->V1.0 | Author: K1RPIT🔥 
GitHub: https://github.com/k1rpit🔥 
  {END}  ''')
help()
try:
    while True:
        user_input=input('<[?]>>')
        if   user_input == '2':
            k1()
        elif user_input == '0':
            sys.exit()
        elif user_input == '1':
            dox()
except KeyboardInterrupt:
    sys.exit()