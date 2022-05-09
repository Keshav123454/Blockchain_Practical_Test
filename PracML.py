import json
from web3 import Web3
from bitcoin import *
import mqsql.connector
#------------Interact with account----------------   

infura_url = "https://mainnet.infura.io/v3/fc2040152e6946c7ad907111b733db51"

web3 = Web3(Web3.HTTPProvider(infura_url))
abi = '[{"constant":true,"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"mint","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"}]'
my_address = "0x2392f6ABF07B5fCE14603d0E28fc952205b8703D"

contract = web3.eth.contract(address=address,abi=abi)
#-------------Generate Addresses------------------
totalSupply = contract.functions.totalSupply().call()

Amount = "The amount we want to send"
remain_balance = balance - Amount
balance = web3.eth.getbalance('my_address')

#--------------Connect MySQL server-----------------
mydb = mysql.connector(host="localhost", user="root",password="password")
mycursor = mydb.cursor()
i=0
while i<100:
    private_key = random_key()
    print(private_key)

    public_key = privtopub(private_key)
    address = pubtoaddr(public_key)
    
    sql = "insert into Address(id,adrs) value(%s,%s)"
    val=(i,address)
    mycursor.execute(sql,val)
    mysql.commit()
 
    transaction = dai.functions.transfer(address, 0x10).buildTransaction({'chainId': 4, 'gas':70000, 'nonce': w3.eth.getTransactionCount('0x5b580eB23Fca4f0936127335a92f722905286738')})
    w3.eth.account.signTransaction(Amount, private_key)
    txn_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)

    sql1 = "insert into Transections(id,transection_hash,FromAddress,ToAddress,Amount,received) value(%s,%s,%s,%s,%s,%s)"
    if balance - Amount == remain_balance :        
        val1=(i,txn_hash,my_address,address,Amount,1)
        mycursor.execute(sql1,val1)
    else:
        val1=(i,txn_hash,my_address,address,Amount,1)
        mycursor.execute(sql1,val1)

    mysql.commit()
    i+=1
mycursor.execute()


