import pandas as pd
import pytest

from myeia.api import API

eia = API()


@pytest.mark.parametrize("series_id", ["NG.RNGC1.D", "PET.WCESTUS1.W", "PET.MD0MP_R10-R20_1.M", "INTL.29-12-HKG-BKWH.A"])
def test_get_series(series_id):
    df = eia.get_series(series_id)
    assert isinstance(df, pd.DataFrame)


@pytest.mark.parametrize(
    "route,series,frequency,facet",
    [("natural-gas/pri/fut", "RNGC1", "daily", "series"), ("petroleum/stoc/wstk", "WCESTUS1", "weekly", "series"), ("petroleum/move/pipe", "MD0MP_R10-R20_1", "monthly", "series")],
)
def test_get_series_via_route(route, series, frequency, facet):
    df = eia.get_series_via_route(route, series, frequency, facet)
    assert isinstance(df, pd.DataFrame)
