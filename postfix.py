expression = input("Enter The Expression : ")

def postfix(exp):
    exp = '(' + exp  + ')'
    exparr = []
    bracket = 0
    answer = ''
    for value in exp:
        if value == " ":
            pass
        elif value.isalpha() or value.isdigit():
            answer += value
        else:
            if value == '(':
                bracket += 1
                exparr.append(value)

            elif value == ')' and bracket <= 0:
                print("invalid")
                answer = ' '
                break
            
            elif value == ')':
                bracket -=1
                for j in range(len(exparr) - 1 , 0 , -1):
                    if exparr[j] != "(":
                        answer += exparr[j]
                        del exparr[j]
                    else:
                        del exparr[j]
                        break

            elif value == '+' :
                for j in range(len(exparr) - 1 , - 1, -1):
                    if exparr[j] != '(':
                        answer = answer + exparr[j]
                        del exparr[j]
                    else:
                        exparr.append("+")
                        break

            elif value == '-' :
                for j in range(len(exparr) - 1 , -1 , -1):

                    if exparr[j] != '(':
                        answer = answer + exparr[j]
                        del exparr[j]
                    else:
                        exparr.append("-")
                        break
            elif value == '*':
                for j in range(len(exparr) - 1 , -1 , -1):
                    if exparr[j] != '(':
                        if exparr[j] == '/':
                            answer += exparr[j]
                            del exparr[j]
                    else:
                        exparr.append("*")
                        break
            elif value == '/':
                for j in range(len(exparr) - 1 , -1 , -1):
                    if exparr[j] != '(':
                        if exparr[j] == '*':
                            answer += exparr[j]
                            del exparr[j]
                    else:
                        exparr.append("/")
                        break
            elif value == "^":
                for j in range(len(exparr) - 1 , -1 , -1):
                    exparr.append("^")
                    break
    
    return answer

print(f"The Postfix is : {postfix(expression)}")