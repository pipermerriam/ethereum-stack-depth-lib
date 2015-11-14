import pytest

import itertools

from ethereum.tester import TransactionFailed


@pytest.mark.parametrize(
    "before_d,check_d",
    (
        # down to 1023
        (0, 0),
        (0, 1),
        (0, 1023),
        (1, 1022),
        (2, 1021),
        (3, 1020),
        # down to 1024
        (0, 1024),
        (1, 1023),
        (2, 1022),
        (3, 1021),
        (4, 1020),
    ),
)
def test_depths(deployed_contracts, before_d, check_d):
    tester = deployed_contracts.TestDepth
    tester.set_sdl(deployed_contracts.StackDepthLib._meta.address)
    expected = before_d + check_d < 1024
    assert tester.test_depth(before_d, check_d) is expected


def test_gas_usage(deployed_contracts, deploy_client):
    tester = deployed_contracts.TestDepth
    tester.set_sdl(deployed_contracts.StackDepthLib._meta.address)

    gas_usage = {}

    values_to_measure = itertools.chain(
        range(0, 10),
        range(10, 100, 10),
        range(100, 1000, 100),
        [1023],
    )

    from pprint import pprint

    for depth in values_to_measure:
        txn_hash = tester.test_depth.sendTransaction(0, depth)
        txn_receipt = deploy_client.wait_for_transaction(txn_hash)
        gas_used = int(txn_receipt['gasUsed'], 16)
        gas_usage[depth] = (gas_used - 21399) / max(depth, 1)

    pprint(sorted(gas_usage.items()))


@pytest.mark.parametrize(
    "pre_depth",
    (0, 1, 10, 20, 23, 24),
)
def test_modifier(deployed_contracts, pre_depth):
    tester = deployed_contracts.TestDepth
    tester.set_sdl(deployed_contracts.StackDepthLib._meta.address)
    expected = pre_depth + 1000 < 1024
    if expected:
        assert tester.test_requires_depth(pre_depth) is True
    else:
        with pytest.raises(TransactionFailed):
            tester.test_requires_depth(pre_depth)
