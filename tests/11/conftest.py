# coding=utf-8
import pytest
#


@pytest.fixture(scope="session", autouse=True)
def test_datas():
    """

    :return:
    """
    return [
        {
            'N': 4,
            'ways': [
                {1, 1, 1, 1},
                {2, 1, 1},
                {1, 2, 1},
                {1, 1, 2},
                {2, 2}
            ],
        }
    ]
