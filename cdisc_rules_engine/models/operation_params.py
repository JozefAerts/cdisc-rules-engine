from dataclasses import dataclass
from typing import List

import pandas as pd


@dataclass
class OperationParams:
    operation_id: str
    operation_name: str
    dataframe: pd.DataFrame
    target: str
    domain: str
    dataset_path: str
    directory_path: str
    datasets: List[dict]
    standard: str
    standard_version: str
    meddra_path: str = None
    whodrug_path: str = None
    grouping: List[str] = None