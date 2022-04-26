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
import csv
import hashlib
import sys

PATHNAME = "Blockchain\blockchain.csv"

# creat Blockchain object
# this adds the block to the blockchain and saves to a CSV
class Blockchain:
    chain:list
    def __init__(self):
        self.chain = []
        # creat the genisus block
        self.mine_block("genisus","genisus", 0.0)


    # Function: mine_block()
    # Job: this mines the new block and saves it to the CSV chain
    # Peramiters: 
    def mine_block(self, sender:str, recever:str, transaction:float, previus_proof_num):
        proof = self.proof_of_work(previus_proof_num)
        block = {"sender":sender,
                "recever":recever,
                "transaction":transaction,
                "proof":proof,
                "hash":0}
        hash = self.hash()
        block["hash"] = hash
                
        with open(PATHNAME, 'a', newline='') as csv_file:
            block_writer = csv.writer(csv_file)
            block_writer.writerow(block)
            csv_file.close()      

        self.chain.append(block)     
        return block

    
    # This is the function for proof of work
    # and used to successfully mine the block
    # this is from 'https://www.geeksforgeeks.org/create-simple-blockchain-using-python/'
    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
         
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            
            if hash_operation[:5] == '00000':
                check_proof = True
            else:
                new_proof += 1
                 
        return new_proof


    # this is from 'https://www.geeksforgeeks.org/create-simple-blockchain-using-python/'
    # calculates the hash of a string of text
    def hash(self, block):
        
        encoded_block = json.dumps(block, sort_keys=True).encode()
        
        return hashlib.sha256(encoded_block).hexdigest()

    
    # Validates the chain
    # NEED TO CHANGE TO WORK WITH PROGRAM
    def chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
         
        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
               
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(
                str(proof**2 - previous_proof**2).encode()).hexdigest()
             
            if hash_operation[:5] != '00000':
                return False
            previous_block = block
            block_index += 1
         
        return True


              
    # Job: lists the blocks in the chain line by line
    def list_chain(self,):
        for i in self.chain:
            print(f"{i['sender']}\t{i['recever']}\t{i['transaction']}\t{i['proof']}\t{i['hash']}")
    

    # Job: finds and prints a single block on the chain
    def show_block(self, index_num):
        i = self.chain[index_num]
        print(f"{i['sender']}\t{i['recever']}\t{i['transaction']}\t{i['proof']}\t{i['hash']}")


# Name: main () function
# Job: main program function
# Peramiters: none
def main ():
    # initiate the chain
    # get user input
    # save to chain
    
    print ("Benjamin Boden's Blockchian program")
    print ()

    Chain = Blockchain()

    menu = '''Comands:
            
            new --------- creats new block
            list -------- lists all blocks in the chain
            vew --------- shows one block
            menu -------- shows the menu
            exit -------- ends the program''' # list of comands saved as string

    
    print (menu)
    while True: # main program loop
        command = input('Comand: ->  ')
        # switch case statments for menu command
        if command == "menu":
            print(menu)
        elif command == "exit":
            print ("Good by!")
            sys.exit()
        elif command == "new":
            ### need some print statmens to get user input            
            Chain.mine_block()
        elif command == "list":
            Chain.list_chain()
        elif command == "vew":
            num = get_valled_int("What block num do you want: ")
            Chain.show_block(num)
        else :
            print ("Not a valled responce")
            print ("hint: use command 'menu' to vew the list of commands again")



# creat function that
# verifies user info as a float
def get_valed_float ():
    pass


def get_valled_int():
    pass

# Run main () program function
if __name__ == "__main__" : main ()