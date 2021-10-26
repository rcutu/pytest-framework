from pytest import mark


@mark.TV
@mark.parametrize('tv_brand', [
    ('Samsung'),
    ('Tlefunken'),
    ('Bose')
])
def test_television_turn_on(tv_brand):
    print(f'{tv_brand} turns on as expected')


@mark.diffrent_browsers
def test_browser_can_navigate_to_training_ground(browser):
    browser.get('http://techstepacademy.com/training-ground')
