from pytest import mark


@mark.environment
def test_env_is_qa(env):
    assert env == 'qa'


@mark.environment
def test_env_is_dev(env):
    assert env == 'dev'
