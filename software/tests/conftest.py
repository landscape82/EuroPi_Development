# Copyright 2024 Allen Synthesis
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import sys
from pathlib import Path

import pytest

sys.path.append(str(Path(__file__).parent.parent / "firmware"))
sys.path.append(str(Path(__file__).parent.parent))  # contrib
sys.path.append(str(Path(__file__).parent.parent / "tests" / "mocks"))


import utime
from mock_hardware import MockHardware


@pytest.fixture(autouse=True)
def mock_time_module(monkeypatch):
    """
    MicroPython's `time` module includes utime's ticks_ms/sleep_ms/etc extensions, but CPython's
    doesn't. Scripts written against MicroPython's `time` (rather than `utime` directly) would
    otherwise raise ImportError only when collected under pytest. See issue #310.
    """
    monkeypatch.setitem(sys.modules, "time", utime)


@pytest.fixture
def mockHardware(monkeypatch):
    return MockHardware(monkeypatch)
