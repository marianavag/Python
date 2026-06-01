from enum import Enum
from typing import List, Dict, Any
from datetime import datetime
from pydantic import BaseModel, Field, model_validator, ValidationError
from typing_extensions import Self


class Rank(str, Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime = Field()
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def mission_validator(self) -> Self:
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")
        has_leader = any(
            member.rank in [Rank.commander, Rank.captain]
            for member in self.crew
            )
        if not has_leader:
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )
        any_inactive = any(
            not member.is_active
            for member in self.crew
        )
        if any_inactive:
            raise ValueError("All crew members must be active")
        if self.duration_days > 365:
            total_crew = len(self.crew)
            experienced_count = 0
            for member in self.crew:
                if member.years_experience >= 5:
                    experienced_count += 1
            if experienced_count < total_crew/2:
                raise ValueError(
                    "Long missions (> 365 days) "
                    "need 50% experienced crew (5+ years)"
                )
        return self


space_missions: List[Dict[str, Any]] = [
    {
        'mission_id': 'M2024_MARS',
        'mission_name': 'Mars Colony Establishment',
        'destination': 'Mars',
        'launch_date': '2024-01-01T12:00:00',
        'duration_days': 900,
        'crew': [
            {
                'member_id': 'CM001',
                'name': 'Sarah Connor',
                'rank': 'commander',
                'age': 50,
                'specialization': 'Mission Command',
                'years_experience': 20
            },
            {
                'member_id': 'CM002',
                'name': 'John Smith',
                'rank': 'lieutenant',
                'age': 40,
                'specialization': 'Navigation',
                'years_experience': 15
            },
            {
                'member_id': 'CM003',
                'name': 'Alice Johnson',
                'rank': 'officer',
                'age': 30,
                'specialization': 'Engineering',
                'years_experience': 5
            }
        ],
        'budget_millions': 2500.0
    },
    {
        'mission_id': 'M2024_MARS',
        'mission_name': 'Mars Colony Establishment',
        'destination': 'Mars',
        'launch_date': '2024-01-01T12:00:00',
        'duration_days': 900,
        'crew': [
            {
                'member_id': 'CM001',
                'name': 'Sarah Connor',
                'rank': 'cadet',
                'age': 50,
                'specialization': 'Mission command',
                'years_experience': 20
            },
            {
                'member_id': 'CM002',
                'name': 'John Smith',
                'rank': 'lieutenant',
                'age': 40,
                'specialization': 'Navigation',
                'years_experience': 15
            },
            {
                'member_id': 'CM003',
                'name': 'Alice Johnson',
                'rank': 'officer',
                'age': 30,
                'specialization': 'Engineering',
                'years_experience': 5
            }
        ],
        'budget_millions': 2500.0
    }
]


def main() -> None:
    print("Space Mission Crew Validation")
    for space_mission in space_missions:
        try:
            mission = SpaceMission(**space_mission)
            print("=" * 38)
            print("Valid mission created:")
            print(
                f"Mission: {mission.mission_name}\n"
                f"ID: {mission.mission_id}\n"
                f"Destination: {mission.destination}\n"
                f"Duration: {mission.duration_days} days\n"
                f"Budget: ${mission.budget_millions}M\n"
                f"Crew size: {len(mission.crew)}\n"
                "Crew members:"
            )
            for member in mission.crew:
                name = member.name
                rank = member.rank.value
                spec = member.specialization
                print(f"- {name} ({rank}) - {spec}")
            print()
        except ValidationError as e:
            print("=" * 38)
            print("Expected validation error:")
            for error in e.errors():
                print(error["msg"])


if __name__ == "__main__":
    main()
