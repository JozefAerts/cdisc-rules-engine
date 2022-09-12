from abc import ABC, abstractmethod
from typing import Callable, TextIO, List, Optional

import pandas as pd

from .cache_service_interface import CacheServiceInterface


class DataServiceInterface(ABC):
    """
    Interface that defines a set of methods
    that must be implemented by all services
    that download datasets from a certain storage.
    """

    @classmethod
    @abstractmethod
    def get_instance(
        cls, cache_service: CacheServiceInterface, config, **kwargs
    ) -> "DataServiceInterface":
        """
        Creates an instance of data service
        """

    @abstractmethod
    def get_dataset(self, dataset_name: str, **params) -> pd.DataFrame:
        """
        Gets dataset from blob storage.
        """

    @abstractmethod
    def get_dataset_metadata(self, dataset_name: str, **kwargs):
        """
        Gets dataset metadata from blob storage.
        """

    @abstractmethod
    def get_dataset_by_type(
        self, dataset_name: str, dataset_type: str, **params
    ) -> pd.DataFrame:
        """
        Generic function to return dataset based on the type.
        dataset_type param can be: contents, metadata, variables_metadata.
        """

    @abstractmethod
    def join_split_datasets(self, func_to_call: Callable, dataset_names, **kwargs):
        """
        Accepts a list of split dataset filenames,
        downloads all of them and merges into a single DataFrame.
        """

    @abstractmethod
    def has_all_files(self, prefix: str, file_names: List[str]) -> bool:
        """
        Checks if all files exist
        """

    @abstractmethod
    def read_data(self, file_path: str, read_mode: str = "r") -> TextIO:
        """
        Reads data from the given path and returns TextIO instance.
        """

    @abstractmethod
    def get_dataset_class(
        self, dataset: pd.DataFrame, file_path: str, datasets: List[dict]
    ) -> Optional[str]:
        """
        Returns dataset class based on its contents
        """