const Tournaments = artifacts.require("Tournaments");

module.exports = function(deployer) {
  deployer.deploy(Tournaments);
};
