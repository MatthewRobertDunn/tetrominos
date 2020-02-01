
import tiles
all_patterns = []

# T
pattern = [
        [0, 1, 0],
        [1, 1, 1],
        [0, 0, 0]]

all_patterns.append((pattern, tiles.RED_TILE))

# L
pattern = [
        [0, 1, 0],
        [0, 1, 0],
        [0, 1, 1]]

all_patterns.append((pattern, tiles.BLUE_TILE))

# J
pattern = [
            [0, 1, 0],
            [0, 1, 0],
            [1, 1, 0]
        ]

all_patterns.append((pattern, tiles.YELLOW_TILE))

# S
pattern = [
        [0, 1, 1],
        [1, 1, 0],
        [0, 0, 0]]
all_patterns.append((pattern, tiles.GREEN_TILE))

# Z
pattern = [
        [1, 1, 0],
        [0, 1, 1],
        [0, 0, 0]]
all_patterns.append((pattern, tiles.GRAY_TILE))

# O
pattern = [
        [1, 1],
        [1, 1]]
all_patterns.append((pattern, tiles.ORANGE_TILE))


# I
pattern = [
        [0, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 0, 0]]
all_patterns.append((pattern,tiles.PINK_TILE))
