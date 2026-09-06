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
import pytest

import europi_hardware
from europi_config import MODEL_PICO, MODEL_PICO_2, MODEL_PICO_2W, MODEL_PICO_W


@pytest.mark.parametrize("model", [MODEL_PICO_2, MODEL_PICO_2W])
def test_usb_connection_uses_sie_status_on_pico_2(monkeypatch, model):
    """Pico 2 / Pico 2 W must use the SIE_STATUS register, not the GP24 pin (see issue #478)."""
    monkeypatch.setattr(europi_hardware.europi_config, "PICO_MODEL", model)
    usb = europi_hardware.UsbConnection()
    assert usb.pin is None


@pytest.mark.parametrize("model", [MODEL_PICO, MODEL_PICO_W])
def test_usb_connection_uses_gp24_on_original_pico(monkeypatch, model):
    """The original Pico / Pico W still detect USB via the GP24 pin."""
    monkeypatch.setattr(europi_hardware.europi_config, "PICO_MODEL", model)
    usb = europi_hardware.UsbConnection()
    assert usb.pin is not None
