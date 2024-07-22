const {Web3} = require('web3');
const web3 = new Web3(new Web3.providers.HttpProvider('http://127.0.0.1:7545/'));

const contractAbi = [
    {
        "constant": true,
        "inputs": [
          {
            "name": "",
            "type": "uint256"
          }
        ],
        "name": "tournaments",
        "outputs": [
          {
            "name": "name",
            "type": "string"
          },
          {
            "name": "winner",
            "type": "string"
          }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
      },
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
    ]

const contractAddress = '0xCABb0706C2E5D5b92119D1865212951dc527CbdD';
const contract = new web3.eth.Contract(contractAbi, contractAddress);

async function main() {
    try {
        const accounts = await web3.eth.getAccounts();
        const account = accounts[0];

        // Specify gas price manually (in wei)
        const gasPrice = '20000000000'; // Example gas price: 20 Gwei

        // Add tournament
        const tx = await contract.methods.addTournament('Tournament1', 'Winner1').send({ from: account, gasPrice });
        console.log('Transaction hash:', tx.transactionHash);
        console.log('Transaction successful!');

        // Get the tournament count
        const count = await contract.methods.getTournamentCount().call();
        console.log('Tournament Count:', count);

        // // Fetch each tournament
        // for (let i = 0; i < count; i++) {
        //     const tournament = await contract.methods.getTournament(i).call();
        //     console.log(`Tournament ${i}: Name: ${tournament[0]}, Winner: ${tournament[1]}`);
        // }
    } catch (error) {
        console.error('Error:', error);
    }
}

main();
