## deps

* selenium
* webdriver_manager
* PyYAML
* pytest

for debian:
```
#apt install python3-selenium python3-yaml python3-pytest
$ pip install webdriver_manager
```

## output example

```
$ ./run_tests.sh
=========================================== test session starts ============================================
platform linux -- Python 3.11.1, pytest-7.2.1, pluggy-1.0.0+repack -- /usr/bin/python3
cachedir: .pytest_cache
rootdir: /home/sl/PycharmProjects/HillelWebDriverLearning
collected 5 items

tests/1_test_qauto_garage.py::test_garage_is_empty PASSED
tests/1_test_qauto_garage.py::test_add_car_button_is_present PASSED
tests/1_test_qauto_garage.py::test_add_button_is_disabled PASSED
tests/1_test_qauto_garage.py::test_add_button_is_enabled PASSED
tests/1_test_qauto_garage.py::test_add_car_check_in_garage_then_remove PASSED

============================================ 5 passed in 28.01s ============================================
```


## refs

* https://github.com/SherDG/Hillel_top
* https://selenium-python.readthedocs.io/api.html
* https://www.selenium.dev/documentation/webdriver/
* https://www.selenium.dev/documentation/webdriver/waits/
* https://docs.pytest.org/en/7.2.x/
* https://docs.pytest.org/en/7.2.x/reference/fixtures.html#fixture
