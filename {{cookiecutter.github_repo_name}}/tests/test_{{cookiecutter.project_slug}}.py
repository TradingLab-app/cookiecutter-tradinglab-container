#!/usr/bin/env python

"""Tests for `{{ cookiecutter.project_slug }}` package."""

{% if cookiecutter.use_pytest == 'y' -%}
import pytest
{% else %}
import unittest
{%- endif %}

from {{ cookiecutter.project_slug }} import {{ cookiecutter.project_slug }}

{%- if cookiecutter.use_pytest == 'y' %}

@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    NotImplemented("")


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    ...


{%- else %}

class Test_{{ cookiecutter.project_slug|title }}(unittest.TestCase):
    """Tests for `{{ cookiecutter.project_slug }}` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

{%- endif %}
