from dataclasses import dataclass, field
from typing import Optional

@dataclass
class Todo:
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False
