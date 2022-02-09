class Coordinate:
    # constructor
    def __init__(self, *, x: int, y: int, z: int) -> None:
        self.position = {"x": x, "y": y, "z": z}

    # getting a certain coordinate value
    def __getitem__(self, key: str) -> int:
        return self.position[key]

    # setting a certain coordinate value to something
    def __setitem__(self, key: str, value: int) -> None:
        self.position[key] = value

    # deleting a certain coordinate value
    def __delitem__(self, key: str) -> None:
        self.position[key] = 0
        # this method automatically sets the coordinate value to 0 instead of deleting it
        # del a["x"] will set : the value of the x coordinate to 0

    """Mathematical operations for the Coordinate object"""

    # addition
    def __add__(self, __o: object) -> object:
        return Coordinate(
            x=self.position["x"] + __o.position["x"],
            y=self.position["y"] + __o.position["y"],
            z=self.position["z"] + __o.position["z"],
        )

    # subtraction
    def __sub__(self, __o: object) -> object:
        return Coordinate(
            x=self.position["x"] - __o.position["x"],
            y=self.position["y"] - __o.position["y"],
            z=self.position["z"] - __o.position["z"],
        )

    # multiplication
    def __mul__(self, __o: object) -> object:
        return Coordinate(
            x=self.position["x"] * __o.position["x"],
            y=self.position["y"] * __o.position["y"],
            z=self.position["z"] * __o.position["z"],
        )

    # floordivision
    def __floordiv__(self, __o: object) -> object:
        return Coordinate(
            x=self.position["x"] // __o.position["x"],
            y=self.position["y"] // __o.position["y"],
            z=self.position["z"] // __o.position["z"],
        )

    # checks if distance from origin of two points is equal or not
    def __eq__(self, __o: object) -> bool:
        return len(self) == len(__o)

    # checks if distance from origin of two points is not-equal or equal
    def __ne__(self, __o: object) -> bool:
        return len(self) != len(__o)

    # checks if distance from origin of two points is greater than or not
    def __gt__(self, __o: object) -> bool:
        return len(self) > len(__o)

    # checks if distance from origin of two points is greater than equal or not
    def __ge__(self, __o: object) -> bool:
        return len(self) >= len(__o)

    # checks if distance from origin of two points is less than or not
    def __lt__(self, __o: object) -> bool:
        return len(self) < len(__o)

    # checks if distance from origin of two points is less than equal or not
    def __le__(self, __o: object) -> bool:
        return len(self) <= len(__o)

    # finding the distance of the coordinate from origin (approximated result)
    def __len__(self) -> int:
        return int(
            (
                self.position["x"] ** 2
                + self.position["y"] ** 2
                + self.position["z"] ** 2
            )
            ** 0.5
        )

    def __repr__(self) -> str:
        return f"({self.position['x']}, {self.position['y']}, {self.position['z']})"
