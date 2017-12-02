from collections import OrderedDict

import pytest

from .windirs import windirs


def test_windir():
    found = OrderedDict()
    for name in windirs:
        path = getattr(windirs, name)
        found[name] = path
        getitem_found = windirs[name]
        assert getitem_found == path
    assert windirs['desktop'] == found['Desktop']
    assert found['Desktop'] and found['Desktop'].lower().endswith('desktop')
    with pytest.raises(AttributeError):
        _ = windirs.x
