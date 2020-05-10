from event_tools.user import User
import pandas as pd
from typing import *


class Page(object):
    """
    This class brings together the users and events that are managed
    on itself. Key properties include:
    - being able to list all users registered on the page
    - being able to list all events that take place
    - all other, more detailed information about people and events
    are handled by the respective `Event` and `User` class
    """

    def __init__(self):
        # create initial list of users and write to csv
        self.users = self.create_initial_users()
        self.events = []  # list of events to be added here
        # keep list of

    def create_initial_users(self):
        users = [
            User(name="Chris Kamara", gender="male"),
            User(name="Lionel Messi", gender="male"),
            User(name="Jan Frodeno", gender="male"),
            User(name="Heiko Westermann", gender="male"),
            User(name="Serena Williams", gender="female"),
            User(name="Marta", gender="female"),
            User(name="Alex Morgan", gender="female"),
        ]

        # create Dataframe and write users to csv
        users_df = pd.DataFrame(
            data={
                "name": [u.name for u in users],
                "uuid": [u.uuid for u in users],
                "gender": [u.gender for u in users],
                "invited": [u.events_invited for u in users],
                "attending": [u.events_attending for u in users],
            }
        )

        users_df.to_csv("users.csv", sep=",", encoding="utf-8")

        return users

    def get_users(self) -> List[User]:
        """
        Loads in CSV of current users and returns list of User objects
        :return:
        """
        return self.users

    def get_user_information(self):
        for user in self.users:
            user.get_info()

    def get_event_information(self):
        for event in self.events:
            event.get_info()

    def add_user(self, new_user: User):
        # update property
        self.users += [new_user]
        # update csv database
        return None

    def get_events(self):
        pass

    def write_users(self):
        pass

    def get_event_stats(self):
        pass


if __name__ == "__main__":
    # write some function calls to locally test the page class
    pass
