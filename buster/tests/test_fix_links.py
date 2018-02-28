import docopt
import pytest

from buster import buster


def test_main_runs():
    try:
        buster.main()
    except docopt.DocoptExit:
        pass
    except Exception as e:
        pytest.fail("Calling buster raise an exception: %s" % e)
