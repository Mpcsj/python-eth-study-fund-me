from brownie import accounts, config, network
from scripts.utils.constants import LOCAL_BLOCKCHAIN_ENVS, FORKED_LOCAL_BLOCKCHAIN_ENVS


def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVS or network.show_active() in FORKED_LOCAL_BLOCKCHAIN_ENVS:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])
