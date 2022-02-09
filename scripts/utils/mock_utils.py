from brownie import MockV3Aggregator
from web3 import Web3

from scripts.utils.constants import STARTING_PRICE, DECIMALS


def get_mocked_v3_aggregator(account: str, force_deploy: bool = False):
    if len(MockV3Aggregator) <= 0 or force_deploy:
        # to prevent redeploying
        print('Deploy mocked V3Aggregator')
        # return MockV3Aggregator.deploy(DECIMALS, Web3.toWei(STARTING_PRICE, "ether"), {
        #     "from": account
        # })
        return MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {
            "from": account
        })
    else:
        print('Reuse latest deployed contract')
        # use the latest deployed contract
        return MockV3Aggregator[-1]

# def get_mocked_v3_aggregator(account: str):
#     return MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {
#         "from": account
#     })
