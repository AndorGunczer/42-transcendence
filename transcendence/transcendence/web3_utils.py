from web3 import Web3

# Connect to Ganache (default URL is usually http://localhost:7545)
web3 = Web3(Web3.HTTPProvider('http://localhost:7545'))

# Ensure connection is successful
if not web3.is_connected():
    raise Exception("Failed to connect to Ethereum node")

# Contract ABI and address (replace with your contract's ABI and address)
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
        "constant": False,
        "inputs": [
            {"name": "index", "type": "uint256"},
            {"name": "participant", "type": "string"}
        ],
        "name": "addParticipant",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {"name": "index", "type": "uint256"},
            {"name": "participant", "type": "string"},
            {"name": "score", "type": "int256"}
        ],
        "name": "incrementScore",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {"name": "index", "type": "uint256"},
            {"name": "_winner", "type": "string"}
        ],
        "name": "setWinner",
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
    },
    {
        "constant": True,
        "inputs": [
            {"name": "index", "type": "uint256"},
            {"name": "participant", "type": "string"}
        ],
        "name": "getParticipantScore",
        "outputs": [
            {"name": "", "type": "int256"}
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
        "name": "getParticipantList",
        "outputs": [
            {"name": "", "type": "string[]"}
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [
            {"name": "_name", "type": "string"}
        ],
        "name": "getTournamentIndexByName",
        "outputs": [
            {"name": "", "type": "uint256"}
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    }
]

# contract_address = '0x7a9f3aA1EEF757421BE6692aefa97132ac210249'
f = open("/Users/mrubina/projects/transcendence/tr2/app/contractAddress.txt", "r")
contract_address = (f.read()).strip()
print(contract_address)

# Initialize contract
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

# Use Ganache's first account (typically pre-funded)
from_address = web3.eth.accounts[0]

def add_tournament(name, winner):
    transaction = contract.functions.addTournament(name, winner).build_transaction({
        'from': from_address,
        'nonce': web3.eth.get_transaction_count(from_address),
        'gas': 2000000,
        'gasPrice': web3.to_wei('20', 'gwei')
    })
    txn_hash = web3.eth.send_transaction(transaction)
    txn_receipt = web3.eth.wait_for_transaction_receipt(txn_hash)
    return txn_receipt

def add_participant(index, participant):
    transaction = contract.functions.addParticipant(index, participant).build_transaction({
        'from': from_address,
        'nonce': web3.eth.get_transaction_count(from_address),
        'gas': 2000000,
        'gasPrice': web3.to_wei('20', 'gwei')
    })
    txn_hash = web3.eth.send_transaction(transaction)
    txn_receipt = web3.eth.wait_for_transaction_receipt(txn_hash)
    return txn_receipt

def increment_score(index, participant, score):
    transaction = contract.functions.incrementScore(index, participant, score).build_transaction({
        'from': from_address,
        'nonce': web3.eth.get_transaction_count(from_address),
        'gas': 2000000,
        'gasPrice': web3.to_wei('20', 'gwei')
    })
    txn_hash = web3.eth.send_transaction(transaction)
    txn_receipt = web3.eth.wait_for_transaction_receipt(txn_hash)
    return txn_receipt

def set_winner(index, winner):
    transaction = contract.functions.setWinner(index, winner).build_transaction({
        'from': from_address,
        'nonce': web3.eth.get_transaction_count(from_address),
        'gas': 2000000,
        'gasPrice': web3.to_wei('20', 'gwei')
    })
    txn_hash = web3.eth.send_transaction(transaction)
    txn_receipt = web3.eth.wait_for_transaction_receipt(txn_hash)
    return txn_receipt

def get_tournament_count():
    return contract.functions.getTournamentCount().call()

def get_tournament(index):
    return contract.functions.getTournament(index).call()

def get_participant_score(index, participant):
    return contract.functions.getParticipantScore(index, participant).call()

def get_participant_list(index):
    return contract.functions.getParticipantList(index).call()

def get_tournament_index_by_name(name):
    return contract.functions.getTournamentIndexByName(name).call()

def test_add_tournament():
    name = "Test Tournament"
    winner = "Winner A"
    receipt = add_tournament(name, winner)
    print(f"addTournament transaction successful with hash: {receipt.transactionHash.hex()}")

def test_add_participant():
    index = 0
    participant = "Participant A"
    receipt = add_participant(index, participant)
    participant = "Participant B"
    receipt2 = add_participant(index, participant)
    print(f"addParticipant transaction successful with hash: {receipt.transactionHash.hex()}")

def test_increment_score():
    index = 0
    participant = "Participant A"
    score = 10
    receipt = increment_score(index, participant, score)
    increment_score(index, "Participant B", 3)
    print(f"incrementScore transaction successful with hash: {receipt.transactionHash.hex()}")

def test_set_winner():
    index = 0
    winner = "Winner B"
    receipt = set_winner(index, winner)
    print(f"setWinner transaction successful with hash: {receipt.transactionHash.hex()}")

def test_get_tournament_count():
    count = get_tournament_count()
    print(f"Total number of tournaments: {count}")

def test_get_tournament():
    index = 0
    tournament_details = get_tournament(index)
    print(f"Tournament details: {tournament_details}")

def test_get_participant_score():
    index = 0
    participant = "Participant B"
    participant_score = get_participant_score(index, participant)
    print(f"Participant score: {participant_score}")

def test_get_participant_list():
    index = 0
    participant_list = get_participant_list(index)
    print(f"Participant list: {participant_list}")
    # for participant in participant_list:
    #     participant_score = get_participant_score(index, participant)


def test_get_tournament_index_by_name():
    name = "Test Tournament"
    tournament_index = get_tournament_index_by_name(name)
    print(f"Tournament index: {tournament_index}")
    




##############
##############
##############
##############

# def test_add_tournament():
#     name = "Test Tournament"
#     winner = "Winner A"
#     receipt = add_tournament(name, winner)
#     print(f"addTournament transaction successful with hash: {receipt.transactionHash.hex()}")

# def test_add_participant():
#     index = 0
#     participant = "Participant A"
#     receipt = add_participant(index, participant)
#     participant = "Participant B"
#     receipt2 = add_participant(index, participant)
#     print(f"addParticipant transaction successful with hash: {receipt.transactionHash.hex()}")

# def test_increment_score():
#     index = 0
#     participant = "Participant A"
#     score = 10
#     receipt = increment_score(index, participant, score)
#     increment_score(index, "Participant B", 3)
#     print(f"incrementScore transaction successful with hash: {receipt.transactionHash.hex()}")

# def test_set_winner():
#     index = 0
#     winner = "Winner B"
#     receipt = set_winner(index, winner)
#     print(f"setWinner transaction successful with hash: {receipt.transactionHash.hex()}")

# def test_get_tournament_count():
#     count = get_tournament_count()
#     print(f"Total number of tournaments: {count}")

# def test_get_tournament():
#     index = 0
#     tournament_details = get_tournament(index)
#     print(f"Tournament details: {tournament_details}")

# def test_get_participant_score():
#     index = 0
#     participant = "Participant B"
#     participant_score = get_participant_score(index, participant)
#     print(f"Participant score: {participant_score}")

# def test_get_participant_list():
#     index = 0
#     participant_list = get_participant_list(index)
#     print(f"Participant list: {participant_list}")

# def test_get_tournament_index_by_name():
#     name = "Test Tournament"
#     tournament_index = get_tournament_index_by_name(name)
#     print(f"Tournament index: {tournament_index}")

# # Example usage
# def main():
#     test_add_tournament()
#     test_add_participant()
#     test_increment_score()
#     test_set_winner()
#     test_get_tournament_count()
#     test_get_tournament()
#     test_get_participant_score()
#     test_get_participant_list()
#     test_get_tournament_index_by_name()

# if __name__ == "__main__":
#     main()