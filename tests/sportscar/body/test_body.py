from pytest import mark


@mark.body
class BodyTests:
    @mark.ui
    def test_can_navigate_to_body(self, chrome_browser):
        chrome_browser.get('https://www.artofmanliness.com/articles/how-a-cars-engine-works/')
        assert True

    @mark.body
    def test_bumper(self):
        assert True

    @mark.body
    def test_windshield(self):
        assert True
