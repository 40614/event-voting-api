import pandas as pd
import uuid


class User(object):
    def __init__(self, name: str, gender: str, uuid_: str = None) -> None:
        """
        Wrapper class for a user which assigns unique user IDs
        :param name:
        :param gender:
        """
        self.name = name  # display name
        self.events_hosted = []
        self.events_invited = []
        self.events_attending = []
        self.events_maybe = []
        self.events_declined = []
        # maybe add self.event_declined

        # assign uuid if it doesn't exist yet
        if uuid_ is None:
            self.uuid = uuid.uuid4()
        else:
            self.uuid = uuid_

        # we'll allow for "other" genders as well to be non-discriminative
        valid_genders = ["male", "female", "other"]
        assert (
            gender in valid_genders
        ), f"Invalid gender passed! please select one of {valid_genders}"
        self.gender = gender

    def get_info(self):
        print("********************************")
        print(f"User Name {self.name}")
        print(f"User ID: {self.uuid}")
        print(f"Gender: {self.gender}")
        print(f"Events hosted: {[event.name for event in self.events_hosted]}")
        print(f"Events invited: {[event.name for event in self.events_invited]}")
        print(f"Events attending: {[event.name for event in self.events_attending]}")
        print(f"Events maybe attending: {[event.name for event in self.events_maybe]}")
        print("********************************")

    def get_event_from_uuid(self, uuid: str):
        for event in self.events_invited:
            if event.uuid == uuid:
                return event
            else:
                continue

        # return -1 if event can't be matched
        return -1

    def attend(self, event_uuid: str) -> None:
        event = self.get_event_from_uuid(event_uuid)
        # make sure that we only repond once to avoid duplicates
        if event not in self.events_attending:
            print(f"{self.name} is attending {event.name}")
            event.attending.append(self)
            self.events_attending.append(event)
        return None

    def maybe(self, event_uuid: str) -> None:
        event = self.get_event_from_uuid(event_uuid)
        # make sure that we only repond once to avoid duplicates
        if event not in self.events_maybe:
            print(f"{self.name} is maybe attending {event.name}")
            event.maybe.append(self)
            self.events_maybe.append(event)
        return None

    def decline(self, event_uuid: str) -> None:
        event = self.get_event_from_uuid(event_uuid)
        # make sure that we only repond once to avoid duplicates
        if event not in self.events_declined:
            print(f"{self.name} is has declined {event.name}")
            event.declined.append(self)
            self.events_declined.append(event)

        return None
