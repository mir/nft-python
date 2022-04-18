from brownie import (
    accounts, config, network, Contract,
    MaratsNFT
    )
from web3 import Web3

FORKED_LOCAL_ENVIRONMENTS = ["mainnet-forked", "mainnet-fork-dev"]
LOCAL_BLOCKHAIN_ENVIRONMENTS = ["development", "ganache-local"]


def get_account(index=None, id=None):
    if index:
        return accounts[index]
    if id:
        return accounts.load(id)

    if (network.show_active() in LOCAL_BLOCKHAIN_ENVIRONMENTS
            or network.show_active() in FORKED_LOCAL_ENVIRONMENTS):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])