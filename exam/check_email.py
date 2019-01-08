def isEmpty(name):
    if len(name) == 0:
        return True
    else:
        return False

def isCorrectForm(email, context='email'):
    if context == 'email':
        if '@' not in email:
            return False
        else:
            return True
    elif context == 'domain':
        if '.' not in email:
            return False
        else:
            return True

def isValidFirstChar(char, context='local'):
    if context == 'local':
        if ('A' <= char and char <= 'Z') or ('a' <= char and char <= 'z') or ('0' <= char and char <= '9'):
            return True
        else:
            return False
    elif context == 'domain':
        if char != '.':
            return True
        else:
            return False

def isValidChar(char, context='local'):
    if context == 'local':     
        if char == '.' or char == '_' or ('A' <= char and char <= 'Z') or ('a' <= char and char <= 'z') or ('0' <= char and char <= '9'):
            return True
        else:
            return False
    elif context == 'domain':
        if char == '.' or ('A' <= char and char <= 'Z') or ('a' <= char and char <= 'z') or ('0' <= char and char <= '9'):
            return True
        else:
            return False

def isDuplicatePoint(domain):
    for i in range(len(domain) - 1):
        if domain[i] == '.' and (domain[i] == domain[i+1]):
            return True
    return False
         
#===============================================================================#
def check_email(email):
    if not isCorrectForm(email):
        return 'INVALID'

    try:
        localPart, domainName = email.split('@')
    except:
        return "INVALID"

    if isEmpty(localPart):
        return 'INVALID'

    if isEmpty(domainName):
        return 'INVALID'
    # Check local Part
    # Check first char
    if not isValidFirstChar(localPart[0], context='local'):
        return 'INVALID'

    for char in localPart:
        if not isValidChar(char, context='local'):
            return 'INVALID'

    # Check domain Part
    # Check Form
    # 4
    if not isCorrectForm(domainName, context='domain'):
        return 'INVALID'

    # 5
    for char in domainName:
        if not isValidChar(char, context='domain'):
            return "INVALID"
        
    if not isValidFirstChar(domainName[0], context='domain'):
        return "INVALID"

    if not isValidFirstChar(domainName[-1], context='domain'):
        return "INVALID"

    if isDuplicatePoint(domainName):
       return "INVALID"

    return 'VALID'


email = str(input())
print(check_email(email))

# check_list = [
#     'big0@gmail.com',
#     'big@gmail.com.',
#     'bigbig@gmail..com',
#     '#big@gmail.com',
#     'bigo@gmailcom',
#     'big@gmail..com',
#     'big@.gmail.com',
#     '@',
#     'big&&123@',
#     '@big@com',
#     'Afdsf@mai.com.',
#     '(@mai.com..com',
#     'A_123@ema.i.com',
#     'AS SD@gmail.com'
# ]

# for item in check_list:
#     print("{}-{}".format(item, check_email(item)))
