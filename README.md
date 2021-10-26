# pytest-framework
pytest qa automation framework leverangin markes and fixures

MARKERS
defined in pytest.ini
skipping tests: @pytest.mark.skip(reson="specific failure")
expected failure: @mark.xfail


FIXTURES
methods defined in conftest.py
@fixture(scope="function") / scope can be also session (running only one instance), class, etc.

REPORTING
html report: pip install pytest--html
run tests with pytest --html="results.html"
or Jenkins report:
in Build Environment you make the script:
cd tests
pytest --junitxml="BUILD_${BUILD_NUMBER}_results.xml"

PARAMETRIZE
example of usage: parametrize a fixture to use multiple webdrivers