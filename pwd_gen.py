import string
import random
 

def generate_password(len:int = 12, diff:int = 4)->str:
    """function for generation random password with difficult, range customization
    
    Keyword arguments:
    len -- length of password
    diff -- difficult of password ( from 1 to 4 )
    Return: randomly generated password string
    """
    
    lower = random.choices(list(string.ascii_lowercase), k = round(len)) if diff>0 else []
    upper = random.choices(list(string.ascii_uppercase), k = round(len)) if diff>1 else []
    digit = random.choices(list(string.digits), k = round(len)) if diff>2 else []
    punct = random.choices(list(string.punctuation), k = round(len)) if diff>3 else []
    result = lower+upper+digit+punct
    random.shuffle(result)
    return str.join('', result[:len])

def main():
    pwd = generate_password(10, 4)
    print(pwd, len(pwd), sep='\n')


if __name__ == '__main__':
    main()