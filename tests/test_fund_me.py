from scripts.utils.utils import get_account
from scripts.deploy import DeployContractRunner
from scripts.utils.constants import LOCAL_BLOCKCHAIN_ENVS
from brownie import network, accounts
import pytest


def test_can_fund_and_withdraw():
    account = get_account()
    fund_me = DeployContractRunner().run()
    entrance_fee = fund_me.getEntranceFee() + 100
    tx = fund_me.fund({"from": account, "value": entrance_fee})
    tx.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == entrance_fee
    tx2 = fund_me.withdraw({"from": account})
    tx2.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == 0


def test_only_owner_can_withdraw():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVS:
        pytest.skip('Only for local testing blockchains')
    fund_me = DeployContractRunner().run()
    founder_account = get_account()
    bad_actor = accounts.add()
    print(f'bad_actor >> {bad_actor}')
    assert founder_account != bad_actor
    with pytest.raises(ValueError):
        # Here, I'm saying that I expect the code to raise an Exception
        fund_me.withdraw({"from": bad_actor})
