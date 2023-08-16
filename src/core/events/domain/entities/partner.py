from dataclasses import dataclass

from src.core.common.domain.aggregate_root import AggregateRoot


@dataclass(frozen=True, slots=True, kw_only=True)
class Partner(AggregateRoot):
    name: str
