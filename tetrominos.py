
all_patterns = []

# T
pattern = [
        [0, 1, 0],
        [1, 1, 1],
        [0, 0, 0]]

all_patterns.append((pattern, (127, 127, 0)))

# L
pattern = [
        [0, 1, 0],
        [0, 1, 0],
        [0, 1, 1]]

all_patterns.append((pattern, (0, 127, 127)))

# J
pattern = [
            [0, 1, 0],
            [0, 1, 0],
            [1, 1, 0]
        ]

all_patterns.append((pattern, (0, 127, 255)))

# S
pattern = [
        [0, 1, 1],
        [1, 1, 0],
        [0, 0, 0]]
all_patterns.append((pattern, (0, 255, 0)))

# Z
pattern = [
        [1, 1, 0],
        [0, 1, 1],
        [0, 0, 0]]
all_patterns.append((pattern, (255, 255, 255)))

# O
pattern = [
        [1, 1],
        [1, 1]]
all_patterns.append((pattern, (127, 0, 127)))


# I
pattern = [
        [0, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 0, 0]]
all_patterns.append((pattern, (255, 255, 255)))
