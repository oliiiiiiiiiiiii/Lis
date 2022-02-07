class Lis:
    def __init__(self, *args: object) -> None:
        self.args = list(args)

    def __getitem__(self, key: int) -> object:
        return self.args[key]

    def __setitem__(self, key: int, value: object) -> None:
        self.args[key] = value

    def __delitem__(self, key: int) -> None:
        del self.args[key]

    def __reversed__(self) -> object:
        return Lis(*(self.args[::-1]))

    def __eq__(self, __o: object) -> bool:
        return self.args == __o.args

    def __lt__(self, __o: object) -> bool:
        return self.args < __o.args

    def __le__(self, __o: object) -> bool:
        return self.args <= __o.args

    def __gt__(self, __o: object) -> bool:
        return self.args > __o.args

    def __ge__(self, __o: object) -> bool:
        return self.args >= __o.args

    def __ne__(self, __o: object) -> bool:
        return self.args != __o.args

    def __add__(self, __o: object) -> object:
        return Lis(*(self.args + __o.args))

    def __iadd__(self, __o: object) -> object:
        self.args += __o.args

    def __mul__(self, __o: int) -> object:
        return Lis(*(self.args * __o))

    def __imul__(self, __o: int) -> object:
        self.args *= __o

    def __len__(self) -> int:
        return len(self.args)

    def __contains__(self, element: object) -> object:
        return self.args.__contains__(element)

    def __iter__(self) -> object:
        return self

    def __str__(self) -> str:
        return str(self.args).replace("[", "< ").replace("]", " >")

    def __repr__(self) -> str:
        return str(self.args).replace("[", "< ").replace("]", " >")

    def copy(self) -> object:
        return Lis(*(self.args))

    def reverse(self) -> None:
        self.args = self.args.__reversed__()

    def index(self, element: object) -> int:
        return self.args.index(element)

    def append(self, element: object) -> None:
        self.args = self.args.append(element)

    def pop(self, key: int) -> None:
        self.args = self.args.pop(key)

    def sort(self, *, key: object, reverse: bool) -> None:
        self.args = (self.args).sort(key=key, reverse=reverse)

    def count(self, element: object) -> int:
        return self.args.count(element)

    def insert(self, insert: int, element: object) -> None:
        self.args = self.args.insert(insert, element)

    def remove(self, element: object) -> None:
        self.args = self.args.remove(element)

    def extend(self, element: object) -> None:
        self.args = self.args.extend(element)
