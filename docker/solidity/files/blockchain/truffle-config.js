module.exports = {
  networks: {
    development: {
      host: "127.0.0.1",     // Localhost (default: ganache-cli)
      port: 7545,            // Standard Ganache UI port
      network_id: "*",       // Any network (default: ganache-cli)
    },
  },
  compilers: {
    solc: {
      version: "0.5.0",     // Specify compiler version
      settings: {
        optimizer: {
          enabled: true,
          runs: 200,
        },
      },
    },
  },
};