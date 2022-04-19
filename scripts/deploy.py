from brownie import (
    accounts, config, network, Contract,
    MaratsNFT
    )
from scripts.utils import get_account, get_contract

def main():    
    account = get_account()
    nft_contract = get_contract("MaratsNFT")    
    tx = nft_contract.awardItem(
        account.address,
        config['nft']['pug_uri'],
        {"from": account})
    tx.wait(1)
    print(f"NFT balance of account[0]:{nft_contract.balanceOf(account.address)}")
    

