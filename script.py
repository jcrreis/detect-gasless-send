from slither.slither import Slither  
from slither.core.expressions.call_expression import CallExpression
from slither.core.expressions.assignment_operation import AssignmentOperation
from slither.core.expressions.expression import Expression

import typing
import sys

if(len(sys.argv) != 2):
    print("Usage: python script.py |solidity file|")
    sys.exit()

def detect_send(exp: str) -> bool:
    if(len(exp.split('.send')) == 2 and exp.split('.send')[1] == ''):
        return True 
    return False

def detect_transfer(exp: str) -> bool:
    if(len(exp.split('.transfer')) == 2 and exp.split('.transfer')[1] == ''):
        return True
    return False

def detect_send_on_arguments(lstExp: typing.List[Expression]) -> bool:
    for exp in lstExp:
        if isinstance(exp, CallExpression):
            exp_str = str(exp.called)
            if(detect_send(exp_str)):
                return True
    return False



def detect_send_or_transfer_usage(exp: Expression) -> typing.Tuple[str, bool]:
    if(isinstance(exp, AssignmentOperation)):
        """
            Detected an assignment operation can be a send? Only if right side is type CallExpression
        """
        if(isinstance(exp.expression_right, CallExpression)):
            exp_str: str = str(exp.expression_right.called)
            if(detect_send(exp_str)):
                return ('send', True)
            else:
                if(detect_send_on_arguments([exp for exp in exp.expression_right.arguments])):
                    return ('send',  True)
    else:
        if(isinstance(exp, CallExpression)):
            """
                Detected an Call expression, can be either a send or transfer?
            """
            exp_str = str(exp.called)
            if(detect_send(exp_str)):
                return ('send', True)
            else:
                if(detect_transfer(exp_str)):
                    return ('transfer', True)
                else:
                    if(detect_send_on_arguments([exp for exp in exp.arguments])):
                        return ('send',  True)
        else:
            return ('', False)
    
    return ('', False)

  

slither = Slither(sys.argv[1])  

lst = []
for contract in slither.contracts: 
    print('==================================================') 
    print('Contract: '+ contract.name + '\n') 
  
    for function in contract.functions:  
        print('Function: {}'.format(function.name) + '\n')  
        
        for v in function.nodes:
            if(v.expression == None):
                continue
            #print("Expression: " + str(v.expression) + '\n' + str(type(v.expression)))
            print(f"Checking if following statement uses send or transfer: {v.expression}")
            res: typing.Tuple[str,bool] = detect_send_or_transfer_usage(v.expression)
            print(res)
            print('\n')
        

