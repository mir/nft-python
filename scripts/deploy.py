from brownie import (
    accounts, config, network, Contract,
    MaratsNFT
    )
from scripts.utils import get_account

def main():
    deploy()

def deploy():
    account = get_account()
    nft = MaratsNFT.deploy(
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify", False))

