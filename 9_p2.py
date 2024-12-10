import time

def get_next_char(memo, mk, space_available):
    for count, index in memo.values():
        if count <= space_available and index not in mk:
            mk.add(index)
            return count, index
    return 0, -1

def fill_memo(s):
    memo = {}
    for i in range(len(s) // 2 + 1):
        idx_of_fill = -(2 * i + 1)
        count_of_fill = int(s[idx_of_fill])
        memo[i] = (count_of_fill, len(s) // 2 - i)
    return memo

def compute_checksum(s):
    checksum = 0
    c = 0
    mk = set()
    memo = fill_memo(s)

    for c_id in range(len(s) // 2):
        file_id_amount = int(s[2 * c_id])
        fill_count = int(s[2 * c_id + 1])

        if c_id not in mk:
            checksum += c_id * file_id_amount * (2 * c + file_id_amount - 1) // 2
            c += file_id_amount
            mk.add(c_id)
        else:
            c += file_id_amount

        while fill_count > 0:
            count, char = get_next_char(memo, mk, fill_count)
            if char == -1:
                c += fill_count
                break

            checksum += char * count * (2 * c + count - 1) // 2
            c += count
            fill_count -= count

    return checksum

# Main execution
start_time = time.time()
s = open("inputs/9.txt").read()
checksum = compute_checksum(s)
end_time = time.time()

print(f"Checksum: {checksum}")
print(f"Execution time: {end_time - start_time:.4f} seconds")
