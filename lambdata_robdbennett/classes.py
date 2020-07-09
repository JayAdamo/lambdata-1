
class Gamer:
    """A test class for gamers. 
    Parameters-
    :var name: str
    :var age: int
    :var position: 0
    """

    # Class Variables
    hair = None
    beard = None
    snobbery = None

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.position = 0

    def __repr__(self):
        return f'{self.__class__} {self.__dict__}'

    def move_up(self) -> None:
        self.position += 1
        print(f'{self.name} moved from {self.position -1} to {self.position}')

    def move_down(self) -> None:
        self.position -= 1
        print(f'{self.name} moved from {self.position +1} to {self.position}')

    def move_to(self, pos: int) -> None:
        old = self.position
        self.position = pos
        print(f'{self.name} moved from {old} to {self.position}')

class Larper(Gamer):
    """A test class(Larper) that inherits from Gamer.
    Adds a speak command.
    """
    # Class variables.
    hair = True
    beard = True

    def __init__(self, name, age):
        super().__init__(name, age)

    def speak(self) -> str:
        return 'LIGHTNING BOLT! LIGHTNING BOLT! LIGHTNING BOLT!'

class Tabletop(Gamer):
    """A test class(Tabletop) that inherits from Gamer.
    Adds a speak command.
    """

    # Class variables.
    hair = True
    snobbery = True
    
    def __init__(self, name, age):
        super().__init__(name, age)

    def speak(self) -> str:
        return 'On page 138 you will clearly see that you are wrong and terrible.'

class VideoGame(Gamer):
    """A test class(Videogame) that inherits from Gamer.
    Adds a speak command.
    """

    # Class variables.
    beard = True

    def __init__(self, name, age):
        super().__init__(name, age)

    def speak(self) -> str:
        return f'{self.name} asks for a Monster energy.'

class Parlor(Larper):
    """A test class(Parlor) that inherits from Larper.
    Adds a hobby and phrase attribute.
    """

    # Class variables.
    games_played = 'indoor'

    def __init__(self, name: str, age: int, hobby: str = None):
        super().__init__(name, age)
        self.hobby = hobby
    
    def speak(self) -> str:
        phrase = f'My name is {self.name}, I am {self.age} years old, but my character is 1000.'
        if self.hobby:
            phrase += f' I like to do {self.hobby}.'
        else:
            phrase += f', and we are both boring.'
        return phrase
    
    def do_hobby(self) -> str:
        if self.hobby:
            return f'I am doing {self.hobby}, it is fun!'
        else:
            return f'I do not have a hobby.'
    
class Immersion(Larper):
    """A test class(Immersion) that inherits from Larper.
    Adds a phrase and hobby command.
    """
    # Class variables.
    games_played = 'outdoor'
    
    def __init__(self, name: str, age: int, hobby: str= None):
        super().__init__(name, age)
        self.hobby = hobby

    def speak(self) -> str:
        phrase = f'My name is {self.name}, I am {self.age} years old, and my character is soooo cool.'
        if self.hobby:
            phrase += f' They are a noble of...'
        else:
            phrase -= f' They know magic!'
        return phrase
    
    def do_hobby(self) -> str:
        if self.hobby:
            return f'I am doing {self.hobby}, it is fun!'
        else:
            return f'I do not have time for fun.'

if __name__ == "__main__":
    pass
