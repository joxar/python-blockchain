import blockChain as bc

def mining():
    target_block = bc.q.get()
    target_block.proof = target_block.mining()
    bc.block_chain.append(target_block)

