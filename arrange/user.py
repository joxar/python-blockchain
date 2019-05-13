import blockChain as bc

def createNewBlock(frm, to, amount):
    newTxn = bc.Block.new_transaction(frm, to, amount)
    previous_index = len(bc.block_chain)
    new_block = bc.Block(previous_index, str(bc.datetime.datetime.now()), newTxn, bc.block_chain[previous_index - 1].now_hash)
    bc.putQ(new_block)

