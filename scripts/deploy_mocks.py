from scripts.utils.mock_utils import get_mocked_v3_aggregator
from scripts.utils.utils import get_account


def main():
    get_mocked_v3_aggregator(get_account(), force_deploy=True)
