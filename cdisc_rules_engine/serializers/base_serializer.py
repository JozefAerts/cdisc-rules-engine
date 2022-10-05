from abc import ABC, abstractmethod


class BaseSerializer(ABC):
    """
    Interface for all concrete serializers.
    """

    @abstractmethod
    @property
    def data(self) -> dict:
        """
        Returns wrapped object as a dict.
        """

    @abstractmethod
    def is_valid(self) -> bool:
        """
        Returns if the wrapped object is valid or not.
        """
