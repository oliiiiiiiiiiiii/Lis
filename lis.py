class Coordinate:
    #constructor
    def __init__(self, *, x: int, y: int, z: int) -> None:
        self.position = {"x": x, "y": y, "z": z}

    #getting a certain coordinate value
    def __getitem__(self, key: str) -> int:
        return self.position[key]

    #setting a certain coordinate value to something
    def __setitem__(self, key: str, value: int) -> None:
        self.position[key] = value

    #deleting a certain coordinate value
    def __delitem__(self, key: str) -> None:
        self.position[key] = 0 
        #this method automatically sets the coordinate value to 0 instead of deleting it
        #del a["x"] will set : the value of the x coordinate to 0

    #mathematical operations for the Coordinate object 
    
    #addition
    def __add__(self, __o: object) -> object:
        return Coordinate(
            x=self.position["x"] + __o.position["x"],
            y=self.position["y"] + __o.position["y"],
            z=self.position["z"] + __o.position["z"],
        )

    #subtraction
    def __sub__(self, __o: object) -> object:
        return Coordinate(
            x=self.position["x"] - __o.position["x"],
            y=self.position["y"] - __o.position["y"],
            z=self.position["z"] - __o.position["z"],
        )

    #multiplication
    def __mul__(self, __o: object) -> object:
        return Coordinate(
            x=self.position["x"] * __o.position["x"],
            y=self.position["y"] * __o.position["y"],
            z=self.position["z"] * __o.position["z"],
        )

    #division or true-division
    def __truediv__(self, __o: object) -> object:
        return Coordinate(
            x=self.position["x"] / __o.position["x"],
            y=self.position["y"] / __o.position["y"],
            z=self.position["z"] / __o.position["z"],
        )

    #floordivision
    def __floordiv__(self, __o: object) -> object:
        return Coordinate(
            x=self.position["x"] // __o.position["x"],
            y=self.position["y"] // __o.position["y"],
            z=self.position["z"] // __o.position["z"],
        )

    #finding the distance of the coordinate from origin
    def __len__(self) -> float:
        return int((self.position["x"] ** 2 + self.position["y"] ** 2 + self.position["z"] ** 2) ** 0.5)

    def __repr__(self) -> str:
        return f"({self.position['x']}, {self.position['y']}, {self.position['z']})"


a = Coordinate(x=5, y=6, z=7)
b = Coordinate(x=6, y=7, z=8)
print(len(a))