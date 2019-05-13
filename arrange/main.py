import blockChain as bc
import user
import miner
from time import sleep

# initialize
bc.initialize()

# user action
user.createNewBlock("店A", "たろう", 100)
user.createNewBlock("店A", "じろう", 100)
user.createNewBlock("店A", "さぶろう", 100)
user.createNewBlock("たろう", "いちたろう", 50)
user.createNewBlock("たろう", "にたろう", 50)

# miner action
miner.mining()
sleep(10)
miner.mining()
sleep(10)
miner.mining()
sleep(10)
miner.mining()

# show
bc.showQ()
bc.show()

