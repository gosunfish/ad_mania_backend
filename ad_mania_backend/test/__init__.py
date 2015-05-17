"""
Test package for ad_mania module
"""
pass

import os

def runall():
    import pytest
    pytest.main(os.path.split(__file__)[0])
