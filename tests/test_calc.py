import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from calc import bmi, level  # noqa: E402


def test_bmi_normal():
    assert bmi(70, 175) == 22.9


def test_level():
    assert level(17) == "過輕"
    assert level(22.9) == "正常"
    assert level(25) == "過重"
    assert level(30) == "肥胖"


def test_bad_height():
    with pytest.raises(ValueError):
        bmi(70, 0)
