import hashlib
import json
import datetime
import queue

class Block:

    def __init__(self, index, timestamp, transaction, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.transaction = transaction
        self.previous_hash = previous_hash
        self.difficulty = 4 # マイニング難易度を調整
        self.property_dict = {
            str(i): j for i, j in self.__dict__.items()
        }
        self.now_hash = self.calc_hash()
        self.proof = None # プルーフを追加
        self.proof_hash = None # プルーフ追加して計算したハッシュ

    def calc_hash(self):
        block_string = json.dumps(self.property_dict, sort_keys=True).encode('utf-8')
        return hashlib.sha256(block_string).hexdigest()

    # プルーフの検証用関数
    def check_proof(self, nonce):
        proof_string = self.now_hash + str(nonce)
        calced = hashlib.sha256(proof_string.encode('utf-8')).hexdigest()
        if calced[:self.difficulty:].count('0') == self.difficulty:
            self.proof_hash = calced
            return True
        else:
            return False

    # マイニング関数
    def mining(self):
        proof = 0
        while True:
            if self.check_proof(proof):
                break
            else:
                proof += 1
        return proof

    def new_transaction(sender, recipient, amount):
        return {
            "差出人": sender,
            "宛先": recipient,
            "金額": amount
        }

q = queue.Queue()
def putQ(unchecked_block):
    global q
    q.put(unchecked_block)

def showQ():
    print("--- Mining pool ---")
    while True:
        if q.empty():
            break
        else:
            item = q.get()
            print(item.transaction)
    print("--------------------")

# initialize
block_chain = []
genesis_block = Block(0, 0, 0, "-")
def initialize():
    genesis_block.proof = genesis_block.mining()
    block_chain.append(genesis_block)

# show
def show():
    for block in block_chain:
        for key, value in block.__dict__.items():
            print(key, ':', value)
        print("")

