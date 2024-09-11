const {Web3} = require('web3');

// Set up web3 with Ganache RPC URL
const ganacheUrl = 'http://localhost:7545';
const web3 = new Web3(new Web3.providers.HttpProvider(ganacheUrl));

// Contract ABI
const contractAbi = [
  {
    "constant": false,
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
    "payable": false,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": true,
    "inputs": [],
    "name": "getTournamentCount",
    "outputs": [
      {
        "name": "",
        "type": "uint256"
      }
    ],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
  },
  {
    "constant": true,
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
    "payable": false,
    "stateMutability": "view",
    "type": "function"
  }
];

// Contract address
const contractAddress = '0x8fe065a44AA43106946577353EfbFdb57da72835';  // Ensure this is the correct contract address

// Create contract instance
const contract = new web3.eth.Contract(contractAbi, contractAddress);

async function main() {
  try {
    // Get the list of accounts
    const accounts = await web3.eth.getAccounts();
    const account = accounts[0];

    // Example: Querying data from the blockchain
    const tournamentCount = await contract.methods.getTournamentCount().call();
    console.log('Total tournaments:', tournamentCount);

    // Example: Query details of each tournament
    for (let i = 0; i < tournamentCount; i++) {
      const tournament = await contract.methods.getTournament(i).call();
      console.log(`Tournament ${i + 1}:`);
      console.log(`Name: ${tournament[0]}`);
      console.log(`Winner: ${tournament[1]}`);
      console.log('------------------------');
    }

    // Example: Adding a new tournament
    const tx = await contract.methods.addTournament('Tournament1', 'Winner1').send({ from: account });
    console.log('Transaction successful:', tx);

  } catch (error) {
    console.error('Error:', error);
  }
}

main();
