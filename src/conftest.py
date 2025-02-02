# pyright: strict

"""Configuration and fixtures for pytest.

This file configures pytest and provides some global fixtures.
See https://docs.pytest.org/en/latest/index.html for more details.

At the moment, Sage is not yet using any tests based on pytest.
"""

from __future__ import annotations
from typing import Any
import pytest

@pytest.fixture(autouse=True)
def add_imports(doctest_namespace: dict[str, Any]):
    """
    Add global imports for doctests.

    See `pytest documentation <https://docs.pytest.org/en/stable/doctest.html#doctest-namespace-fixture>`.
    """
    import sage.all  # type: ignore # implicitly used below by calling locals()
    doctest_namespace.update(**locals())
