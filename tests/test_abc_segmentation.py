import sys
from pathlib import Path

import pytest

sys.path.append(str(Path(__file__).resolve().parents[1]))
from abc_segmentation import ABC_segmentation


@pytest.mark.parametrize("value", [0.0, 0.5, 0.8])
def test_abc_segmentation_a(value):
    assert ABC_segmentation(value) == "A"


@pytest.mark.parametrize("value", [0.81, 0.9, 0.95])
def test_abc_segmentation_b(value):
    assert ABC_segmentation(value) == "B"


@pytest.mark.parametrize("value", [0.96, 0.99, 1.0])
def test_abc_segmentation_c(value):
    assert ABC_segmentation(value) == "C"
