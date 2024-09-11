from web3 import Web3

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
