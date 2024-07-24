from web3 import Web3
import json

def add_tournament_to_blockchain(tournament_name, tournament_winner):

    # Connect to Ganache
    w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))

    # Verify connection
    if not w3.is_connected():
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
    f = open("/app/contractAddress.txt", "r")
    contract_address = (f.read()).strip()
    print(contract_address)
    
    # Check if contract code exists at the address
    code = w3.eth.get_code(contract_address)
    if code == b'0x':
        print("No contract deployed at the address")
    else:
        print("Contract code exists at the address")

        # Initialize contract
        contract = w3.eth.contract(address=contract_address, abi=contract_abi)

        # Set up the account
        account = w3.eth.accounts[0]

        # Add a tournament
        tx_hash = contract.functions.addTournament(tournament_name, tournament_winner).transact({'from': account})
        receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

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


def query_blockchain():

    # Set up web3 with Ganache RPC URL
    ganache_url = 'http://localhost:7545'
    web3 = Web3(Web3.HTTPProvider(ganache_url))

    # Contract ABI
    contract_abi = [
        {
            "constant": False,
            "inputs": [
                {
                    "name": "_name",
                    "type": "string"
                },
                {
                    "name": "_winner",
                    "type": "string"
                }
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
                {
                    "name": "",
                    "type": "uint256"
                }
            ],
            "payable": False,
            "stateMutability": "view",
            "type": "function"
        },
        {
            "constant": True,
            "inputs": [
                {
                    "name": "index",
                    "type": "uint256"
                }
            ],
            "name": "getTournament",
            "outputs": [
                {
                    "name": "",
                    "type": "string"
                },
                {
                    "name": "",
                    "type": "string"
                }
            ],
            "payable": False,
            "stateMutability": "view",
            "type": "function"
        }
    ]

    # Contract address
    f = open("/app/contractAddress.txt", "r")
    contract_address = (f.read()).strip()
    print(contract_address)

    # Create contract instance
    contract = web3.eth.contract(address=contract_address, abi=contract_abi)

    def main():
        try:
            # Get the list of accounts
            accounts = web3.eth.accounts
            account = accounts[0]

            # Example: Querying data from the blockchain
            tournament_count = contract.functions.getTournamentCount().call()
            print('Total tournaments:', tournament_count)

            # Example: Query details of each tournament
            for i in range(tournament_count):
                tournament = contract.functions.getTournament(i).call()
                print(f'Tournament {i + 1}:')
                print(f'Name: {tournament[0]}')
                print(f'Winner: {tournament[1]}')
                print('------------------------')

        except Exception as error:
            print('Error:', error)

    if __name__ == "__main__":
        main()
