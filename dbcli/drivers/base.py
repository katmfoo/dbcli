from abc import ABC, abstractmethod
from typing import List, Optional, Tuple

class ExecutionResponse():
    """Class that is returned by the `execute()` method of a driver class.

    :param success: Whether or not the execution was successful.
    :param result: Optional, should only be set if the execution created a
                   result set that should be returned.
    :param headers: Optional, should only be set if there is a result set and
                    there are headers to go along with that result set.
    :param count: Optional, should be set to the number of results if a result
                  set is being returned. Otherwise, if applicable, this should
                  be set to the number of items created or updated.
    :param error_message: Optional, should only be set if the execution was not
                          successful and there is an error message available.
    """

    def __init__(self, success: bool = True,
                 result: Optional[List[Tuple[str, ...]]] = None,
                 headers: Optional[Tuple[str, ...]] = None,
                 count: Optional[int] = None,
                 error_message: Optional[str] = None):
        self.success = success
        self.result = result
        self.headers = headers
        self.count = count
        self.error_message = error_message

class Driver(ABC):
    """Base driver class that can be extended to add a new database engine (or
    anything else really)
    """

    item_singular: Optional[str] = None
    """The name of the item that is being retrieved/modified (if applicable),
    e.g. 'row' or 'document'"""

    item_plural: Optional[str] = None
    """Plural version of `item_singular`"""

    @classmethod
    def get_pluralized_item_name(cls, count: int) -> Optional[str]:
        """Returns either `item_singular` or `item_plural` based on the count
        that is passed in, or `None` if not available"""

        if cls.item_plural is None:
            if cls.item_singular is None:
                # Neither `item_singular` or `item_plural` is available
                return None
            else:
                # `item_singular` is the only option
                return cls.item_singular
        elif cls.item_singular is None:
            # `item_plural` is the only option
            return cls.item_plural

        # Both `item_singular` and `item_plural` are available, choose which
        # one to return based on `count`
        if count == 1:
            return cls.item_singular
        else:
            return cls.item_plural

    @abstractmethod
    def connect(self, **kwargs) -> None:
        """Should take any information necessary to create and store a
        connection.
        """
        pass

    @abstractmethod
    def execute(self, command: str) -> ExecutionResponse:
        """Should take a command, attempt to execute that command, and return
        an `ExecutionResponse`.

        :param command: The command, query, etc. to execute.
        :returns: An `ExecutionResponse`.
        """
        pass

