import pytest


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
