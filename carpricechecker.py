import requests
from bs4 import BeautifulSoup
import sys
import webbrowser
import mysql.connector
from persiantools import digits

sys.stdin.reconfigure(encoding='utf-8') # To Support Utf-8 And Show Data Successfully
sys.stdout.reconfigure(encoding='utf-8')

def connection():
    '''
    this function will work as a connection to 
    target's website
    '''
    global response,website_address # we need to make some values global to use in other functions
    website_address = 'https://khodro45.com/pricing/'
    response = requests.get(website_address) # Connection To Target's website
    match response.status_code:
        case 200:
            print('You Connected Successfuly')
        case ___:
            print('Your Connection Has A Problam')
connection()

def data_loader():
    '''
    this function will be a dataloader and the data is the html page
    of the target's website
    '''
    global response,website_address,soup
    html_page = response.text
    soup = BeautifulSoup(html_page,'html.parser')
data_loader()

def iran_khodro_cars():
    # peugeot-206-t2
    global response,website_address,soup
    new_response = requests.get('https://khodro45.com/pricing/peugeot-206-t2/') # We Need New Connection To Access To Values)
    html_page = new_response.text
    soup = BeautifulSoup(html_page,'html.parser')
    peugeot_206_t2 = soup.find('div',attrs={'class':'text-16 font-weight-bold'})
    print(f'The Price Of peugeuot206t2 Is:{peugeot_206_t2.text}Tooman')

    # peugeot-206-t3
    new_response = None
    new_response = requests.get('https://khodro45.com/pricing/peugeot-206-t3/')
    html_page = new_response.text
    soup = BeautifulSoup(html_page,'html.parser')
    peugeot_206_t3 = soup.find('div',attrs={'class','text-16 font-weight-bold'})
    print(f'The Price Of peugeuot206t3 Is:{peugeot_206_t3.text}Tooman')

    # peugeot-207-panaromamt
    new_response = None
    new_response = requests.get('https://khodro45.com/pricing/peugeot-207-panaromamt/')
    html_page = new_response.text
    soup = BeautifulSoup(html_page,'html.parser')
    peugeot_207_panaromamt = soup.find_all('div',attrs={'class':'text-16 font-weight-bold'})

    prices_of_peugeot_207_panaromamt = []
    for i in peugeot_207_panaromamt:
        prices_of_peugeot_207_panaromamt.append(i.text)
    price_list_of_peugeot_len = len(prices_of_peugeot_207_panaromamt)
    print(f'The Price Of Peugeot207Panaromamt Is:{prices_of_peugeot_207_panaromamt[price_list_of_peugeot_len-1]}Tooman')
    question_of_user = input('Which Of The Car Do You Wanna See A Picture Of It(Peugeot207Panaromamt,Peugeuot206T3,Peugeuot206T2):')
    question_of_user = question_of_user.lower()
    match question_of_user:
        case 'peugeot207panaromamt':
            webbrowser.open('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS-E7hys151gfEsr_PQDLAdgx8HbL1KcBkPhA&s')
        case 'peugeuot206t3':
            webbrowser.open('https://cdn.khodrobank.com/Gallery/12656_IMG_4678.jpg')
        case 'peugeuot206t2':
            webbrowser.open("https://www.iranjib.ir/uploads/53682.jpg")
        case ___:
            print('Not Valid Input The Program Exiting...')
            sys.exit(0)
    second_question_of_user = input('Do You Want To Save Data To Database(y,n):')
    second_question_of_user = second_question_of_user.lower()
    match second_question_of_user:
        case 'y':
            price_list_of_peugeot_len = price_list_of_peugeot_len-1
            print('Attemping To Connect To Database.....')
            cnx = mysql.connector.connect(host='127.0.0.1',user='mahdi',password='13831349mM@#',database='car_price')
            print('Connected To Database!')
            my_cursur = cnx.cursor()
            my_cursur.execute(f'INSERT INTO iran_khodro_cars (name,price) VALUES(\'peugeot207panaromamt\',\'{digits.fa_to_en(prices_of_peugeot_207_panaromamt[price_list_of_peugeot_len-1])}\'),(\'peugeuot206t3\',\'{digits.fa_to_en(peugeot_206_t3.text)}\'),(\'peugeuot206t2\',\'{digits.fa_to_en(peugeot_206_t2.text)}\')')
            cnx.commit()
            cnx.close()
            print('The Data Added To Database TNX.')
        case 'n':
            print('Nice To Meet You! Bye!')
            sys.exit(0)
        case ___:
            print('Not A Valid Input!')
            sys.exit(0)

def saipa():
    # atlas-g-mt
    global response,website_address,soup
    new_response = requests.get('https://khodro45.com/pricing/atlas-g-mt/')
    soup = BeautifulSoup(new_response.text,'html.parser')
    Atlas_g = soup.find('div',attrs={'class':'text-16 font-weight-bold'})
    print(f'The Price Of Atlas-G Car Is:{Atlas_g.text}Tooman')

    # pride-151-se
    new_response = None
    new_response = requests.get('https://khodro45.com/pricing/pride-151-se/')
    soup = BeautifulSoup(new_response.text,'html.parser')
    pride_151_se = soup.find('div',attrs={'class':'text-16 font-weight-bold'})
    print(f'The Price Of Pride151Se Is:{pride_151_se.text}Tooman')

    # tiba-hatchback-ex
    new_response = None
    new_response = requests.get('https://khodro45.com/pricing/tiba-hatchback-ex/')
    soup = BeautifulSoup(new_response.text,'html.parser')
    pride_hachback = soup.find('div',attrs={'class':'text-16 font-weight-bold'})
    print(f'The Price Of PrideHachback Is:{pride_hachback.text}Tooman')

    # Connecting To Database
    new_response = None
    question_of_user = input('Do You Wanna To Add Data To Database(y,n):')
    match question_of_user:
        case 'y':
            cnx = mysql.connector.connect(host='127.0.0.1',user='mahdi',password='13831349mM@#',database='car_price')
            my_cursur = cnx.cursor()
            my_cursur.execute(f'INSERT INTO saipa_cars (name,price) VALUES(\'AtlasG\',\'{digits.fa_to_en(Atlas_g.text)}\'),(\'Pride151SE\',\'{digits.fa_to_en(pride_151_se.text)}\'),(\'PrideHachback\',\'{digits.fa_to_en(pride_hachback.text)}\')')
            cnx.commit()
            print("Data Added To Database Successfully")
            print("Thanks For Using This Program!")
            sys.exit(0)
        case 'n':
            print('Nice To Meet You! Bye!')
            sys.exit(0)
        case ___:
            print('Not A Valid Input!')
            sys.exit(0)
        
def foreign_cars():
    # MercedesBenzE200
    global response,website_address,soup
    new_response = requests.get('https://khodro45.com/pricing/benz-e-200/')
    soup = BeautifulSoup(new_response.text,'html.parser')
    benz_e_200 = soup.find('div',attrs={'class':'text-16 font-weight-bold'})
    print(f'The Price Of MercedesBenzE200 Is:{benz_e_200.text}Tooman')

    #  BMW x4 28i
    new_response = None
    new_response = requests.get('https://khodro45.com/pricing/bmw-x4-28i/')
    soup = BeautifulSoup(new_response.text,'html.parser')
    bmw_x4_28i = soup.find('div',attrs={'class':'text-16 font-weight-bold'})
    print(f'The Price Of BmwX4 28i Is:{bmw_x4_28i.text}Tooman')

    # Toyota CHR hybrid
    new_response = None
    new_response = requests.get('https://khodro45.com/pricing/toyota-chr-hat/')
    soup = BeautifulSoup(new_response.text,'html.parser')
    Toyota_chr_hybrid = soup.find('div',attrs={'class':'text-16 font-weight-bold'})
    print(f'The Price Of Toyota CHR Hybrid Is:{Toyota_chr_hybrid.text}Tooman')

    # Adding To The Database
    print('Connecting To The Database....')
    cnx = mysql.connector.connect(host='127.0.0.1',user='mahdi',password='13831349mM@#',database='car_price')
    print('Connected To The Database!')
    question_of_user = input('Do You Want To Add Your Data In Database(y,n):')
    match question_of_user:
        case 'y':
            my_cursur = cnx.cursor()
            my_cursur.execute(f'INSERT INTO foreign_cars (name,price) values(\'MercedesBenzE200\',\'{digits.fa_to_en(benz_e_200.text)}\'),(\'BMW x4 28i\',\'{digits.fa_to_en(bmw_x4_28i.text)}\'),(\'Toyota CHR hybrid\',\'{digits.fa_to_en(Toyota_chr_hybrid.text)}\')')
            cnx.commit()
            print('The Data Has Been Successfully Added To Database')
            cnx.close()
        case 'n':
            print('OK Nice To Meet You Have A Great Day')
            sys.exit(0)
        case ___:
            print('Invalid Input Sorry!')
            sys.exit(0)

def data_display():
    '''
    this function will be display the data of 
    car prices
    '''
    global response,website_address,soup
    sub_domain_list = [] # We Need Subdomain To Make For Customers A choise
    for link in soup.find_all('a'):
        sub_domain_list.append(link.get('href'))
    
    customer_question = input('Do You Wanna See Data Before You Add Something(y,n):')
    customer_question = customer_question.lower()
    match customer_question:
        case 'y':
            cnx = mysql.connector.connect(host='127.0.0.1',user='mahdi',password='13831349mM@#',database='car_price')
            my_cursur = cnx.cursor()
            customer_question2 = input('Which Of These Do You Wanna See(Irankhodro/Saipa/Foreign-cars)?')
            customer_question2 = customer_question2.lower()
            match customer_question2:
                case 'irankhodro':
                    my_cursur.execute('SELECT * FROM iran_khodro_cars')
                    my_result = my_cursur.fetchall()
                    for row in my_result:
                        print(row)
                case 'saipa':
                    my_cursur.execute('SELECT * FROM saipa_cars')
                    my_result = my_cursur.fetchall()
                    for row in my_result:
                        print(row)
                case 'foreign-cars':
                    my_cursur.execute('SELECT * FROM foreign_cars')
                    my_result = my_cursur.fetchall()
                    for row in my_result:
                        print(row)
                case ___:
                    print('Not Valid Input!')
                    sys.exit(0)
        case 'n':
            print('OK')
        case ___:
            print('Not A Valid Option Closing App...')
            sys.exit(0)

    # Add Some Data To Database
    customer_input = input('Please Choose Between Saipa/Irankhodro/Foreign-cars:')
    customer_input = customer_input.lower()
    match customer_input: # the customer has 3 choices and if it was invalid input app will be close
        case 'saipa':
            saipa()
        case 'irankhodro':
            iran_khodro_cars()
        case 'foreign-cars':
            foreign_cars()
        case ___:
            print('Suddenly Your Input Was Invalid And Program Exit......')
            sys.exit(0)
data_display()
    


    