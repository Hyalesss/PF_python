class DominoTile:
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    def __eq__(self, other):
        return (self.side1 == other.side1 and self.side2 == other.side2) or \
        (self.side1 == other.side2 and self.side2 == other.side1)

    def __lt__(self, other):
        return (self.side1 + self.side2) < (other.side1 + other.side2)

    def __gt__(self, other):
        return (self.side1 + self.side2) > (other.side1 + other.side2)

    def __str__(self):
        return f'[{self.side1}|{self.side2}]'
    
class DominoStack:
    def __init__(self):
        self.stack = []

    def push(self, tile):
        self.stack.append(tile)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        for tile in self.stack:
            print(tile)

domino_stack = DominoStack()

for side1 in range(7):
    for side2 in range(side1, 7):
        domino_stack.push(DominoTile(side1, side2))

print("28 Kartu Domino cuy:")
domino_stack.display()

side1_tile1 = int(input("Masukkan sisi pertama tile 1: "))
side2_tile1 = int(input("Masukkan sisi kedua tile 1: "))
side1_tile2 = int(input("Masukkan sisi pertama tile 2: "))
side2_tile2 = int(input("Masukkan sisi kedua tile 2: "))

tile1 = DominoTile(side1_tile1, side2_tile1)
tile2 = DominoTile(side1_tile2, side2_tile2)

if tile1 == tile2:
    print(f"\n{tile1} sama dengan {tile2}")
elif tile1 < tile2:
    print(f"\n{tile1} kurang dari {tile2}")
else:
    print(f"\n{tile1} lebih besar dari {tile2}")
