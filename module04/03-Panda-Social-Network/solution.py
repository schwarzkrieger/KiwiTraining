"""Solution of module 4.3 - Panda Social Network"""
import re
class Panda:
    """Panda class"""
    def __init__(self, name, email, gender):
        self._name = name
        pattern = """
        ^                   # beginning of string
        \w+                 # any alphanumeric one or more times
        ([\.-]?\w+)*        # optional dot or slash, then any alphanum zero or more times
        @
        \w+([\.-]?\w+)*     # any alphanum, dot or slash then alphanum zero or more times
        (\.\w{2,})+         # dot folowwed by 2 or more alphanumerics, one or more times
        $                   # end of the string
        """
        if not re.search(pattern, email, re.VERBOSE):
            raise ValueError("The e-mail address is invalid.")
        self._email = email
        if gender != "male" and gender != "female":
            raise TypeError("Only biological genders allowed!")
        self._gender = gender

    def is_male(self):
        return self._gender == "male"

    def is_female(self):
        return self._gender == "female"

    def __eq__(self, other):
        return (self._name == other.name()
                and self._email == other.email()
                and self._gender == other.gender()
                )

    def __hash__(self):
        return hash(self._name + self._email + self._gender)

    def __str__(self):
        return self._name + " " + self._email + " " + self._gender

    def name(self):
        return self._name

    def email(self):
        return self._email

    def gender(self):
        return self._gender

class PandaSocialNetwork:
    """Panda Social Network class"""
    def __init__(self):
        self._socialnetwork = []
        self._friendship = []

    def add_panda(self, panda):
        if panda in self._socialnetwork:
            raise PandaAlreadyThere("Panda already there")
        self._socialnetwork.append(panda)

    def has_panda(self, panda):
        return panda in self._socialnetwork

    def make_friends(self, panda1, panda2):
        if [panda1, panda2] in self._friendship:
            raise PandasAlreadyFriends("Pandas Already Friends")
        if not self.has_panda(panda1):
            self.add_panda(panda1)
        if not self.has_panda(panda2):
            self.add_panda(panda2)
        self._friendship.append([panda1, panda2])
        self._friendship.append([panda2, panda1])

    def are_friends(self, panda1, panda2):
        return [panda1, panda2] in self._friendship

    def friends_of(self, panda):
        friends = []
        for p1, p2 in self._friendship:
            if p1 == panda:
                friends.append(p2)
        return friends
