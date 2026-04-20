"""Basic tests for BrowseGenie"""


def test_import_main():
    """Test that main module can be imported"""
    import main

    assert main is not None


def test_import_browsegenie():
    """Test that browsegenie package can be imported"""
    import browsegenie

    assert browsegenie is not None


def test_basic_assertion():
    """Basic test to ensure pytest is working"""
    assert True
