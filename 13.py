import numpy as np

def button_to_vector(line, op):
    if len(line) <= 1:
        return None
    vec = line[1].strip().split(", ")
    return (int(vec[0].split(op)[1]), int(vec[1].split(op)[1]))

def spans(x, y, z):
    matrix = np.column_stack((x, y))
    target = np.array(z)
    coeffs = np.linalg.solve(matrix, target)
    if np.allclose(coeffs, np.round(coeffs), rtol=1e-15):
        return np.round(coeffs).astype(int)

t = np.zeros(2, dtype=int)
part2 = True
with open("inputs/13_1.txt") as file:
    A = B = C = ()
    for line in file:
        button_a = button_to_vector(line.split("Button A:"), '+')
        button_b = button_to_vector(line.split("Button B:"), '+')
        target = button_to_vector(line.split("Prize:"), '=')

        if button_a:
            A = button_a
        if button_b:
            B = button_b
        if target:
            C = target if not part2 else np.add(target, np.array([10000000000000, 10000000000000]))

        if target:
            s = spans(A, B, C)
            if not s is None:
                t = np.add(t, s)

            A = B = C = ()

print(np.sum(np.multiply(np.array([3, 1]), t)))
