
const {Web3} = require('web3');
const fs = require('fs');
const solc = require('solc');

// Set up web3 with Ganache RPC URL
const ganacheUrl = 'http://127.0.0.1:7545';
const web3 = new Web3(ganacheUrl);

// Read the contract source code
const source = fs.readFileSync('./contracts/Tournaments.sol', 'utf8');

// Compile the contract
const input = {
  language: 'Solidity',
  sources: {
    'Tournaments.sol': {
      content: source,
    },
  },
  settings: {
    outputSelection: {
      '*': {
        '*': ['abi', 'evm.bytecode'],
      },
    },
  },
};

const output = JSON.parse(solc.compile(JSON.stringify(input)));
const abi = output.contracts['Tournaments.sol']['Tournaments'].abi;
const bytecode = output.contracts['Tournaments.sol']['Tournaments'].evm.bytecode.object;

// Deploy the contract
async function deploy() {
  const accounts = await web3.eth.getAccounts();
  const account = accounts[0];

  const contract = new web3.eth.Contract(abi);
  const deployedContract = await contract.deploy({ data: bytecode }).send({ from: account, gas: 1500000, gasPrice: '30000000000000' });

  console.log('Contract deployed at address:', deployedContract.options.address);
}

deploy();
