if __name__ == '__main__':
    print('Func_called - main')
    count = dict()
    Array = ['apple','banana','camera','apple','banana','apple']
    for i in Array:
        count[i] = count.get(i,0) + 1
    print(count)
    '''
    Count Array's word
    '''
    Num_str = input("Please enter your formula : ")
    count = dict()
    for i in Num_str:
        if i == '(':
            count[i] = count.get(i,0) + 1
        elif i == ')':
            count[i] = count.get(i,0) + 1
    if count[')'] != count['(']:
        print('This is not an expression that uses parentheses correctly.')
    else:
        print('This is an expression that uses parentheses correctly.')
    '''
    Judge whether the parenthesis of the formula is correct.        
    '''
else:
    print('Func_called - imported')
    
'''
----------result----------
Func_called - main
{'apple': 3, 'banana': 2, 'camera': 1}

Please enter your formula : (A*(B+C*(D+E))
This is not an expression that uses parentheses correctly.
--------------------------
entered formula is "(A*(B+C*(D+E))"
This formula lacks one parenthesis.
Corrected as follows: "(A*(B+C*(D+E)))"
'''