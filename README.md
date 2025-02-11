# Simple Blockchain Simulation  

## Overview  
A basic Python implementation of a blockchain that includes block creation, hashing, proof-of-work, and chain validation.  

## Features  
- Add transactions and mine blocks  
- SHA-256 hashing for security  
- Detect tampering with chain validation  

## Requirements  
- Python 3.x  

## Installation  
1. Clone the repository:  
   ```bash
   git clone https://github.com/yourusername/simple-blockchain.git  
   cd simple-blockchain  
   ```  
2. Run the script:  
   ```bash
   python blockchain.py  
   ```  

## Example Workflow  
1. The genesis block is created automatically.  
2. Transactions are added and new blocks are mined.  
3. The blockchain is displayed and validated.  

## Blockchain Validation  
- The `is_valid_chain` method ensures integrity.  
- If tampering occurs, validation flags inconsistencies.  
