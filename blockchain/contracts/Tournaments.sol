// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.5.0;

contract Tournaments {
    struct Tournament {
        string name;
        string winner;
    }
    
    // Array to store tournaments
    Tournament[] public tournaments;
    
    // Function to add a new tournament
    function addTournament(string memory _name, string memory _winner) public {
        tournaments.push(Tournament(_name, _winner));
    }
    
    // Function to get the total number of tournaments
    function getTournamentCount() public view returns (uint) {
        return tournaments.length;
    }
    
    // Function to get tournament details by index
    function getTournament(uint index) public view returns (string memory, string memory) {
        require(index < tournaments.length, "Index out of bounds");
        return (tournaments[index].name, tournaments[index].winner);
    }
}
