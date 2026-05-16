from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional, Any, List, Dict


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_length=200)


space_stations: List[Dict[str, Any]] = [
    {
        'station_id': 'ISS001',
        'name': 'International Space Station',
        'crew_size': 6,
        'power_level': 85.5,
        'oxygen_level': 92.3,
        'last_maintenance': '2024-01-01T12:00:00',
        'notes': None
    },
    {
        'station_id': 'ISS001',
        'name': 'International Space Station',
        'crew_size': 30,
        'power_level': 85.5,
        'oxygen_level': 92.3,
        'last_maintenance': '2024-01-01T12:00:00',
        'is_operational': False,
        'notes': None
    },
]


def main() -> None:
    print("Space Station Data Validation")
    for space_station in space_stations:
        try:
            station = SpaceStation(**space_station)
            print("========================================")
            print("Valid station created:")
            print(
                f"ID: {station.station_id}\n"
                f"Name: {station.name}\n"
                f"Crew: {station.crew_size} people\n"
                f"Power: {station.power_level}%\n"
                f"Oxygen: {station.oxygen_level}%\n"
                "Status: "
                f"{'Operational' if station.is_operational else 'Offline'}"
            )
            if station.notes:
                print(f"Notes: {station.notes}")
            print()
        except ValidationError as e:
            print("========================================")
            print("Expected validation error:")
            for error in e.errors():
                print(f"{error['msg']}")


if __name__ == "__main__":
    main()
