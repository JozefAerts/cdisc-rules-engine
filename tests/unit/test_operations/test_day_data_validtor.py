from cdisc_rules_engine.config.config import ConfigService
from cdisc_rules_engine.operations.day_data_validator import DayDataValidator
from cdisc_rules_engine.models.operation_params import OperationParams
import pandas as pd
import pytest

from cdisc_rules_engine.services.cache.cache_service_factory import CacheServiceFactory


@pytest.mark.parametrize(
    "data, expected",
    [
        (
            pd.DataFrame.from_dict(
                {
                    "values": [
                        "1997-07-19T19:20:30",
                        "1997-08-16T19:20:30",
                        "1997-07-16T19:20",
                        "2022-05-20T13:44",
                        "2022-05-20T13:44",
                        None,
                    ]
                }
            ),
            [4, 32, 1, 13, 0, 0],
        ),
    ],
)
def test_minimum(data, expected, mock_data_service, operation_params: OperationParams):
    config = ConfigService()
    cache = CacheServiceFactory(config).get_cache_service()
    datasets_map = {
        "dm.xpt": pd.DataFrame.from_dict(
            {
                "RFSTDTC": [
                    "1997-07-16T19:20:30",
                    "1997-07-16T19:20:30",
                    "1997-07-16T19:20",
                    "2022-05-08T13:44",
                    "TEST",
                    "2022-05-20T13:44",
                ]
            }
        )
    }
    datasets = [
        {"domain": "DM", "filename": "dm.xpt"},
    ]
    mock_data_service.get_dataset.side_effect = lambda name: datasets_map.get(
        name.split("/")[-1]
    )
    operation_params.datasets = datasets
    operation_params.dataframe = data
    operation_params.target = "values"
    result = DayDataValidator(
        operation_params, pd.DataFrame(), cache, mock_data_service
    ).execute()
    print(result)
    assert operation_params.operation_id in result
    for i, val in enumerate(result[operation_params.operation_id]):
        assert val == expected[i]
