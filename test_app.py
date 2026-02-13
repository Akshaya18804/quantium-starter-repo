import pytest
from app import app


def test_header_present(dash_duo):
    dash_duo.start_server(app)
    assert dash_duo.find_element("h1")


def test_visualisation_present(dash_duo):
    dash_duo.start_server(app)
    assert dash_duo.find_element("div")


def test_region_picker_present(dash_duo):
    dash_duo.start_server(app)
    assert dash_duo.find_element("input[type='radio']")
