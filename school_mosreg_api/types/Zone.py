from typing import Optional
from .model import Type, TypeMobile


class Zone(Type):
    f6969id: Optional[int]
    zoneType: Optional[str]
    name: Optional[str]
    radius: Optional[int]
    address: Optional[str]
    latitude: Optional[float]
    longitude: Optional[float]


class CreateZoneResponse(TypeMobile):
    zone: Optional[Zone]
