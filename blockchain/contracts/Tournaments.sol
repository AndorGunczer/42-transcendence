// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.5.0;
pragma experimental ABIEncoderV2;

contract Tournaments {
    struct Tournament {
        string name;
        string winner;
        mapping(string => int) participants;
        string[] participantList;
    }
    
    Tournament[] public tournaments;
    
    // Function to add a new tournament
    function addTournament(string memory _name, string memory _winner) public {
        Tournament memory newTournament;
        newTournament.name = _name;
        newTournament.winner = _winner;
        tournaments.push(newTournament);
    }
    
    // Function to add a participant to a tournament
    function addParticipant(uint index, string memory participant) public {
        require(index < tournaments.length, "Index out of bounds");
        tournaments[index].participants[participant] = 0;
        tournaments[index].participantList.push(participant);
    }
    
    // Function to increment the score of a participant in a tournament
    function incrementScore(uint index, string memory participant, int score) public {
        require(index < tournaments.length, "Index out of bounds");
        require(tournaments[index].participants[participant] >= 0, "Participant does not exist");
        tournaments[index].participants[participant] += score;
    }
    
    // Function to set the winner of a tournament
    function setWinner(uint index, string memory _winner) public {
        require(index < tournaments.length, "Index out of bounds");
        tournaments[index].winner = _winner;
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

    // Function to get the score of a participant in a tournament
    function getParticipantScore(uint index, string memory participant) public view returns (int) {
        require(index < tournaments.length, "Index out of bounds");
        require(tournaments[index].participants[participant] >= 0, "Participant does not exist");
        return tournaments[index].participants[participant];
    }
    
    // Function to get the list of participants in a tournament
    function getParticipantList(uint index) public view returns (string[] memory) {
        require(index < tournaments.length, "Index out of bounds");
        return tournaments[index].participantList;
    }
    
    // Function to get the index of a tournament by name
    function getTournamentIndexByName(string memory _name) public view returns (uint) {
        for (uint i = 0; i < tournaments.length; i++) {
            if (keccak256(abi.encodePacked(tournaments[i].name)) == keccak256(abi.encodePacked(_name))) {
                return i;
            }
        }
        revert("Tournament not found");
    }
}
