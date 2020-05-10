from typing import *
import uuid
import pandas as pd
import matplotlib.pyplot as plt
from event_tools.user import User
from datetime import datetime
from geopy.geocoders import Nominatim



class Event(object):
    def __init__(
        self,
        host: User,
        name: str,
        start_date: str,
        end_date: str,
        description: str,
        location: str,
    ) -> None:
        self.assign_host(host, name)
        self.name = name
        self.end_date = pd.to_datetime(end_date)
        self.start_date = pd.to_datetime(start_date)
        self.description = description
        # also events should have a unique ID to avoid double-named events
        self.uuid = uuid.uuid4()
        self.location = location

        self.invited: List[User] = []
        self.attending: List[User] = []
        self.maybe: List[User] = []
        self.declined: List[User] = []

    def assign_host(self, host: User, name: str) -> None:
        """
        Function which assigns the host to the event and updates
        the state of the `User` class accordingly
        """
        self.host = host
        # wrap in if condition to avoid duplicate assingment
        if name not in [event.name for event in self.host.events_hosted]:
            # assign this event to the corresponding user
            self.host.events_hosted.append(self)
            # we assume that the host attends by default
            self.host.events_attending.append(self)
        return None

    def invite_users(self, sender: User, guest_list: List[User]) -> None:
        # check that the sender of the invite is the host
        if sender.uuid != self.host.uuid:
            raise ValueError("Only event hosts can send invites to the event")

        # update the state of users
        for user in guest_list:
            # we don't want to send duplicate invites
            if user.uuid not in [user.uuid for user in self.invited]:
                # add user to list of invitees
                self.invited.append(user)
                # update the state of the user
                user.events_invited.append(self)

        return None

    def get_info(self) -> Dict:
        print("*********************")
        print(f"Event Name: {self.name}")
        print(f"Host: {self.host.name}")
        print(f"Start Date: {self.start_date}")
        print(f"End Date: {self.end_date}")
        print(f"Location: {self.location}")
        print(f"Description: {self.description}")
        print(f"Event UUID: {self.uuid}")
        print(f"Invited: {[user.name for user in self.invited]}")
        print(f"Confirmed: {[user.name for user in self.attending]}")
        print(f"Maybe: {[user.name for user in self.maybe]}")
        print(f"Declined: {[user.name for user in self.declined]}")
        print("*********************")

    def get_response_stats(self):
        response_df = pd.DataFrame(
            data={
                "response": ["Invited", "Attending", "Maybe", "Declined"],
                "count": [
                    len(self.invited),
                    len(self.attending),
                    len(self.maybe),
                    len(self.declined),
                ],
            }
        )

        response_df.plot(kind="bar",
                         x="response",
                         y="count",
                         figsize=(12, 9),
                         color=["b", "g", "y", "r"])
        plt.title(f"Responses to event {self.name} taking place on {self.start_date}", fontsize=20)
        plt.xlabel(f"Response", fontsize=14)
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        plt.show()

    def countdown(self):
        """
        Function which prints the number of days to given event
        :return:
        """
        diff = self.start_date - datetime.now()
        print(
            f"Countdown to {self.name}: {diff.days} days..."
        )

    def get_directions(self) -> None:
        geolocator = Nominatim(user_agent="my-application")
        location = geolocator.geocode(self.location)

        print("Full Address of the event venue:")
        print(location)
        return None

    def remove(self):
        """
        Remove a user from the event
        """
        pass
