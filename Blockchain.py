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

PATHNAME = "blockchain.csv"

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
        block = [sender,recever,transaction,proof]
        hash = self.hash()
        block.append(hash)
                
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


              
    # lists the blocks in the chain line by line
    def list_chain(self, chain):
        pass
    

    # finds and prints a single block on the chain
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