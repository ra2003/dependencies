from typing import Any
from typing import Dict
from typing import List

class Replace:
    def __init__(self, dependency: Any, attrs: List[str]) -> None: ...

class Attributes:
    def __init__(self, spec: Any, attrs: List[str]) -> None: ...
    def __call__(self, **kwargs: Dict[str, Any]) -> Any: ...
    @property
    def __name__(self) -> str: ...
    @property
    def __dependencies__(self) -> Any: ...
