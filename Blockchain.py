#!/usr/bin/env python3

# Name: Benjamin M. Boden
# Class: (INFO 1200)
# Section: (X01)
# Professor: (Crandall)
# Date: 25/04/12022
# Project #: Final
''' I declare that the source code contained in this assignment was written solely by me.
    I understand that copying any source code, in whole or in part, 
    constitutes cheating, and that I will receive a zero on this project
    if I am found in violation of this policy.'''


# import stuff
import json
import hashlib

PATHNAME = "blockchain.json"

# creat Block object
# this stores the transaction and gets the prof
class  Block_Obj:
    block:list
    sender:str
    recever:str
    transaction:float

    def __init__(self, sender, recever, transaction):
        pass

# creat Blockchain object
# this adds the block to the blockchain and saves to a CSV
class Blockchain:
    def __init__():
        # creat the genisus block
        pass

    def mine_block(self, sender, recever, transaction):
        proof = ''
        block = {   "index": i,
                    "previus": blocks,
                    "proof": proof,
                    "sender": sender,
                    "recipient": recever,
                    "amount": transaction
                }


    def get_chain(self):
        with open(PATHNAME, 'r', newline='') as json_file:
            temp = json_file.readlines()
            chain = json.loads(temp)
            return chain


    def save_chain(self, new_block):
        with open (PATHNAME, 'w', newline="" ) as json_file:
            pass
            

    def list_chain(self, chain):
        pass

    def show_block(self, index_num, chain):
        pass


# Name: main () function
# Job: main program function
# Peramiters: none
def main ():
    # initiate the chain
    # get user input
    # save to chain
    pass


# creat function that
# verifies user info as a float

# Run main () program function
if __name__ == "__main__" : main ()