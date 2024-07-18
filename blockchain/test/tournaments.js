const Tournaments = artifacts.require("Tournaments");

contract("Tournaments", (accounts) => {
  let tournamentsInstance;

  before(async () => {
    tournamentsInstance = await Tournaments.deployed();
  });

  it("should add a new tournament", async () => {
    await tournamentsInstance.addTournament("Tournament 1", "Winner 1", { from: accounts[0] });
    const count = await tournamentsInstance.getTournamentCount();
    assert.equal(count, 1, "Tournament count should be 1 after adding a tournament");
  });

  it("should retrieve tournament details", async () => {
    await tournamentsInstance.addTournament("Tournament 2", "Winner 2", { from: accounts[0] });
    const tournament = await tournamentsInstance.getTournament(1);
    assert.equal(tournament[0], "Tournament 2", "Tournament name should be 'Tournament 2'");
    assert.equal(tournament[1], "Winner 2", "Tournament winner should be 'Winner 2'");
  });
});
