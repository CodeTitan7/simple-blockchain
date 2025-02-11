import hashlib
import time
import json

class Block:
    def __init__(self, index, previous_hash, transactions, proof):
        self.index = index  # Block position in the chain
        self.timestamp = time.time()
        self.transactions = transactions
        self.previous_hash = previous_hash  # Ensures chain integrity
        self.proof = proof  # Value obtained from proof-of-work
        self.hash = self.compute_hash()  # Unique identifier of the block

    def compute_hash(self):
        block_data = {
            "index": self.index,
            "timestamp": self.timestamp,
            "transactions": self.transactions,
            "previous_hash": self.previous_hash,
            "proof": self.proof
        }
        block_string = json.dumps(block_data, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    def __init__(self, difficulty=2):
        self.chain = []
        self.transactions = []
        self.difficulty = difficulty  # Mining difficulty
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, "0", [], 0)
        genesis_block.hash = genesis_block.compute_hash()
        self.chain.append(genesis_block)

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def proof_of_work(self, previous_hash):
        proof = 0
        while True:
            block_data = f"{previous_hash}{proof}"
            block_hash = hashlib.sha256(block_data.encode()).hexdigest()
            if block_hash.startswith("0" * self.difficulty):  # Valid proof condition
                return proof
            proof += 1

    def add_block(self):
        previous_hash = self.chain[-1].hash  # Fetch last block's hash
        proof = self.proof_of_work(previous_hash)
        new_block = Block(len(self.chain), previous_hash, self.transactions, proof)
        new_block.hash = new_block.compute_hash()
        self.transactions = []  # Reset after block creation
        self.chain.append(new_block)

    def is_valid_chain(self):
        for i in range(1, len(self.chain)):
            prev_block = self.chain[i - 1]
            curr_block = self.chain[i]
            if curr_block.hash != curr_block.compute_hash():  # Detect tampering
                return False
            if curr_block.previous_hash != prev_block.hash:  # Ensure linkage
                return False
        return True

    def tamper_with_block(self, index, new_data):
        if 0 < index < len(self.chain):  # Avoid modifying genesis block
            self.chain[index].transactions = new_data
            self.chain[index].hash = self.chain[index].compute_hash()  # Recalculate hash

    def display_chain(self):
        for block in self.chain:
            print(json.dumps(block.__dict__, indent=4))

# Initialize blockchain
blockchain = Blockchain()

# Add transactions and mine blocks
blockchain.add_transaction({"from": "Arjun", "to": "Marley", "amount": 60})
blockchain.add_block()
blockchain.add_transaction({"from": "Chaplin", "to": "Dev", "amount": 25})
blockchain.add_block()

# Display valid blockchain
print("Blockchain before tampering:")
blockchain.display_chain()
print("Is the blockchain valid :", blockchain.is_valid_chain())

# Modify a block's transaction data
tamper_index = 1
blockchain.tamper_with_block(tamper_index, [{"from": "Geronimo", "to": "Dwayne", "amount": 1500}])

# Display tampered blockchain
print("\nBlockchain after tampering:")
blockchain.display_chain()
print("Is the blockchain valid :", blockchain.is_valid_chain())
