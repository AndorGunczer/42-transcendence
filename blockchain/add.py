from web3 import Web3
import json

# Connect to Ganache
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))

# Verify connection
if not w3.isConnected():
    print("Failed to connect to the Ethereum node")
else:
    print("Connected to the Ethereum node")

# Contract ABI
contract_abi = [
    {
        "constant": False,
        "inputs": [
            {"name": "_name", "type": "string"},
            {"name": "_winner", "type": "string"}
        ],
        "name": "addTournament",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "getTournamentCount",
        "outputs": [
            {"name": "", "type": "uint256"}
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [
            {"name": "index", "type": "uint256"}
        ],
        "name": "getTournament",
        "outputs": [
            {"name": "", "type": "string"},
            {"name": "", "type": "string"}
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    }
]

# Contract address
contract_address = '0x8fe065a44AA43106946577353EfbFdb57da72835'

# Check if contract code exists at the address
code = w3.eth.getCode(contract_address)
if code == b'0x':
    print("No contract deployed at the address")
else:
    print("Contract code exists at the address")

    # Initialize contract
    contract = w3.eth.contract(address=contract_address, abi=contract_abi)

    # Set up the account
    account = w3.eth.accounts[0]

    # Add a tournament
    tx_hash = contract.functions.addTournament("Tournament1", "Winner1").transact({'from': account})
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)

    # Check transaction receipt
    if receipt.status == 1:
        print("Transaction successful!")
    else:
        print("Transaction failed!")

    # Check the tournament count
    try:
        tournament_count = contract.functions.getTournamentCount().call()
        print(f"Tournament Count: {tournament_count}")

        # Fetch and print tournament details
        for index in range(tournament_count):
            tournament = contract.functions.getTournament(index).call()
            print(f"Tournament {index}: Name: {tournament[0]}, Winner: {tournament[1]}")
    except Exception as e:
        print(f"Error fetching tournament details: {e}")
