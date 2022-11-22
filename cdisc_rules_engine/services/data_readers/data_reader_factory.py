from typing import Type

from cdisc_rules_engine.interfaces import (
    DataReaderInterface,
    FactoryInterface,
)
from cdisc_rules_engine.services.data_readers.xpt_reader import XPTReader
from cdisc_rules_engine.services.data_readers.dataset_json_reader import DatasetJSONReader


class DataReaderFactory(FactoryInterface):
    _reader_map = {
        "xpt": XPTReader,
        "json": DatasetJSONReader,
    }

    use_json = True

    def __init__(self):
        self._default_service_name: str = "xpt"

    @classmethod
    def register_service(cls, name: str, service: Type[DataReaderInterface]):
        """
        Registers a new service in internal _service_map
        """
        print("registering data reader service with name = ", name)
        if not name:
            raise ValueError("Service name must not be empty!")
        if not issubclass(service, DataReaderInterface):
            raise TypeError("Implementation of DataReaderInterface required!")
        cls._reader_map[name] = service

    def get_service(self, name: str = None, **kwargs) -> DataReaderInterface:
        """
        Get instance of service that matches searched implementation
        """
        # print("get_service, name = ", name)
        # print("Using JSON, use_json = ", self.use_json)
        if name is None and self.use_json:
            # name = "json"
            print("service name changed into = ", name)
        service_name = name or self._default_service_name
        # print("service_name = ", service_name)
        if service_name in self._reader_map:
            return self._reader_map[service_name]()
        raise ValueError(
            f"Service name must be in {list(self._reader_map.keys())}, "
            f"given service name is {service_name}"
        )
