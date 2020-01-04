"""Solution of module 4.3 - Panda Social Network"""
import re
class Panda:
    """Panda class"""
    def __init__(self, name, email, gender):
        self._name = name
        pattern = """
        ^                   # beginning of the string
        \w+                 # any alphanumeric one or more times
        ([.-]?\w+)*         # optional dot or slash, then any alphanum zero or more times
        @
        \w+([.-]?\w+)*      # any alphanum, dot or slash then alphanum zero or more times
        (\.\w{2,})+         # dot folowwed by 2 or more alphanumerics, one or more times
        $                   # end of the string
        """
        if not re.search(pattern, email, re.VERBOSE):
            raise ValueError("The e-mail address is invalid.")
        self._email = email
        if gender not in ("male", "female"):
            raise TypeError("Only biological genders allowed!")
        self._gender = gender

    def is_male(self):
        """check male gender"""
        return self._gender == "male"

    def is_female(self):
        """check female gender"""
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
        """return panda name"""
        return self._name

    def email(self):
        """return panda e-mail"""
        return self._email

    def gender(self):
        """return panda gender"""
        return self._gender

class PandaSocialNetwork:
    """Panda Social Network class"""
    def __init__(self):
        self._socialnetwork = []
        self._friendship = []

    def add_panda(self, panda):
        """add panda to the network"""
        if panda in self._socialnetwork:
            raise PandaAlreadyThere("Panda already there")
        self._socialnetwork.append(panda)

    def has_panda(self, panda):
        """check if panda is member of the network"""
        return panda in self._socialnetwork

    def make_friends(self, panda1, panda2):
        """make two pandas friends"""
        if [panda1, panda2] in self._friendship:
            raise PandasAlreadyFriends("Pandas Already Friends")
        if not self.has_panda(panda1):
            self.add_panda(panda1)
        if not self.has_panda(panda2):
            self.add_panda(panda2)
        self._friendship.append([panda1, panda2])
        self._friendship.append([panda2, panda1])

    def are_friends(self, panda1, panda2):
        """check if two pandas are friends"""
        return [panda1, panda2] in self._friendship

    def friends_of(self, panda):
        """return list of panda's friends"""
        friends = []
        for panda1, panda2 in self._friendship:
            if panda1 == panda:
                friends.append(panda2)
        return friends

    def connection_level(self, panda1, panda2):
        """check connection level between pandas"""
        if panda1 not in self._socialnetwork or panda2 not in self._socialnetwork:
            return False
        tested_panda = []
        return self._connection_level(panda1, panda2, tested_panda)

    def _connection_level(self, current_panda, target_panda, tested_panda):
        if current_panda in tested_panda:
            return -1
        tested_panda.append(current_panda)
        if current_panda == target_panda:
            return 0
        for friend in self.friends_of(current_panda):
            connlvl = self._connection_level(friend, target_panda, tested_panda)
            if connlvl != -1:
                return connlvl+1
        return -1

    def are_connected(self, panda1, panda2):
        """check if two pandas are connected"""
        return self.connection_level(panda1, panda2) > 0

    def how_many_gender_in_network(self, level, panda, gender):
        """check how many genders to given level"""
        gender_count = 0
        tested_panda = [panda]
        nextlevel = self.friends_of(panda)
        while level > 0:
            nextlvl = []
            for friend in nextlevel:
                if friend in tested_panda:
                    continue
                tested_panda.append(friend)
                if friend.gender() == gender:
                    gender_count += 1
                for next_friends in self.friends_of(friend):
                    if next_friends not in tested_panda:
                        nextlvl.append(next_friends)
            nextlevel = nextlvl
            level -= 1
        return gender_count

class PandaAlreadyThere(Exception):
    """bogus exception handler"""

class PandasAlreadyFriends(Exception):
    """bogus exception handler"""
