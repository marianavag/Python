from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from typing import Optional, Any, List, Dict
from enum import Enum
from typing_extensions import Self


class ContactType(str, Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telep = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime = Field()
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def validate_contact(self) -> Self:
        if not self.contact_id.startswith("AC"):
            raise ValueError(
                "Contact ID must start with 'AC' (Alien Contact)"
            )
        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError(
                "Physical contact reports must be verified"
            )
        if self.contact_type == ContactType.telep and self.witness_count < 3:
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
            )
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError(
                "Strong signals (> 7.0) should include received messages"
            )
        return self


alien_contacts: List[Dict[str, Any]] = [
    {
        'contact_id': 'AC_2024_001',
        'timestamp': '2024-01-01T12:00:00',
        'location': 'Area 51, Nevada',
        'contact_type': 'radio',
        'signal_strength': 8.5,
        'duration_minutes': 45,
        'witness_count': 5,
        'message_received': 'Greetings from Zeta Reticuli',
    },
    {
        'contact_id': 'AC_2024_001',
        'timestamp': '2024-01-01T12:00:00',
        'location': 'Area 51, Nevada',
        'contact_type': 'telepathic',
        'signal_strength': 8.5,
        'duration_minutes': 45,
        'witness_count': 2,
        'message_received': 'Greetings from Zeta Reticuli'
    }
]


def main() -> None:
    print("Alien Contact Log Validation")
    print("=" * 38)
    for alien_contact in alien_contacts:
        try:
            report = AlienContact(**alien_contact)
            print("Valid contact report:")
            print(
                    f"ID: {report.contact_id}\n"
                    f"Type: {report.contact_type}\n"
                    f"Location: {report.location}\n"
                    f"Signal: {report.signal_strength}/10\n"
                    f"Duration: {report.duration_minutes} minutes\n"
                    f"Witnesses: {report.witness_count}"
            )
            if report.message_received:
                print(f"Message: '{report.message_received}'")
            print()
        except ValidationError as e:
            print("=" * 38)
            print("Expected validation error:")
            for error in e.errors():
                print(error['msg'])


if __name__ == "__main__":
    main()
