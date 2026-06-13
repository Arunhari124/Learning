import ui
from account_creation import account_creating
from signin import sign_in

ui.bank_name()
is_running=True
while is_running:
    x=input("\nNew User?[R]             Existing user?[S]")
    if x.upper()=="X":
        account_creating()
        x=input("sign_in[S]")
        
        is_running=False
    elif x.upper()=="S":
        sign_in()
        is_running=False
    else:
        account_creating()
        is_running=False