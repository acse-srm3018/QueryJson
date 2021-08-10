"""Module for query by Example JSON document store .

This is an implementation of Raha Moosavi

Query By Example allows a client to specify a structure
in which is used as the example, and all entities which match are returned.
Implement a basic storage mechanism which allows a user to store documents
in JSON format.
The structure of the document may be otherwise arbitrary.

The program accepts a command through stdin followed by a space,
followed by a document, followed by a newline.

There are three allowed commands:
* Add : store the given document
* Get : find all documents which have the same properties and property value
        as the given document, and emit them to stdout
* Delete: remove all documents which have the same properties
        and property values as the given document.

The commands are all lowercase.
"""

import json
import sys


class Database:
    """
    A Class to get query from user as json format.

    Three commands can be applied based on user need:
    1- add 2- get and match 3- delete

    Methods
    -------
    add(query):
        Adds the user query to database list.

    get(query):
        Getting the user query and find a match in database
        list if there is any.

    delete(query):
        Deletes the user query from database list.

    parse(query):
        Parses the user query in input and applied sutaible
        methods based on command and query.

    """

    def __init__(self):
        """Construct an initial empty list."""
        self.list_db = []

    def add(self, query):
        """
        Add entity from user to database list.

        Args:
        -----
        query:
            get stdin from user
        """
        self.list_db.append(query)

    def get(self, query):
        """
        Get query and find matches.

        Args:
        -----
        query:
            get stdin from user
        """
        for data in self.list_db:
            active = True
            for key, value in query.items():
                if isinstance(value, dict):
                    for i_key, i_value in value.items():
                        try:
                            if data[key].get(i_key) != i_value:
                                active = False
                                continue
                        except KeyError:
                            continue
                elif isinstance(value, list):
                    for item in value:
                        if item not in data["list"]:
                            active = False
                        continue
                elif data.get(key) != value:
                    active = False
                    continue
            # If find a match, printing that data
            if active:
                try:
                    print(json.dumps(data, separators=(',', ':')))
                except IOError:
                    # stdout is closed, no point in continuing
                    # Attempt to close them explicitly to prevent cleanup
                    try:
                        sys.stdout.close()
                    except IOError:
                        pass

    def delete(self, query):
        """
        Delete the query from database list.

        Args:
        -----
        query:
            get stdin from user
        """
        # looping through each data and finding the matching values
        for data in self.list_db:
            active = True
            for key, value in query.items():
                if isinstance(value, dict):
                    for i_key, i_value in value.items():
                        try:
                            if data[key].get(i_key) != i_value:
                                active = False
                                continue
                        except KeyError:
                            continue
                if isinstance(value, list):
                    for item in value:
                        if item not in data["list"]:
                            active = False
                            continue

                elif data.get(key) != value:
                    active = False
                    continue
            # If a match is present, removing that data
            if active and data in self.list_db:
                self.list_db.remove(data)

    def parse(self):
        """
        Parse json format input into command and value.

        get the input from user, parse it and then call
        methods based on user command.
        """
        for line in sys.stdin:
            if not line:
                return
            command, value = line.split(" ", maxsplit=1)
            objects = json.loads(value)
            if command == 'add':
                self.add(objects)
            elif command == 'get':
                self.get(objects)
            elif command == 'delete':
                self.delete(objects)
            else:
                return


data = Database()
data.parse()
