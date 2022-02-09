from scripts.utils.utils import get_account, config
from brownie import FundMe, network
from scripts.utils.mock_utils import get_mocked_v3_aggregator
from scripts.utils.constants import LOCAL_BLOCKCHAIN_ENVS


class DeployContractRunner:
    def __init__(self):
        self.account = get_account()

    def get_aggregator_v3_interface_address(self) -> str:
        curr_network = network.show_active()
        print(f'curr_network>>{curr_network}')
        if curr_network not in LOCAL_BLOCKCHAIN_ENVS:
            return config["networks"][curr_network]["eth_usd_price_feed"]
        else:
            print(f"The active network is {curr_network}")
            print("Deploying mocks")
            return get_mocked_v3_aggregator(self.account).address

    def run(self):
        account = get_account()
        fund_me = FundMe.deploy(self.get_aggregator_v3_interface_address(),
                                {"from": account},
                                publish_source=config["networks"][network.show_active()].get("verify", False)
                                )
        print(f'contract deployed to {fund_me.address}')
        return fund_me


def main():
    DeployContractRunner().run()
