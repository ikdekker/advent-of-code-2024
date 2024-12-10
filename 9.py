def get_next_char(m, s):
    while m[2] <= m[1]:
        m[0] += 1
        m[1] = 0
        m[2] = int(s[(2*m[0]+1)*-1])
        m[3] = len(s) // 2 - m[0]
    m[1] += 1
    return m[3]

x = open("inputs/9.txt").read()

checksum = 0
n = ""
s = len(x)
marker = [-1, 0, -1, s//2] # [POINTER, COUNTER, BUFFER_SIZE, NUMBER_TO_FILL]
c = 0
for i in range(0, len(x)//2, 2):
    c_id = i//2
    c_count = int(x[i:i+1])
    f_count = int(x[i+1:i+2])
    n += c_count * str(c_id)
    for c_i in range(c_count):
        checksum += c * c_id
        c += 1
    for j in range(int(f_count)):
        end_char = get_next_char(marker, x)
        n += str(end_char)
        checksum += int(end_char) * c
        c += 1

# probably reached the end of what we can fill
# actually not sure what the best condition is yet to do this or not..
# for i in range(i+2,len(x), 2):
#     c_id = i//2
#     print(i, i//2)
#
#     c_count = int(x[i:i+1])
#     to_fill = c_count
#     if marker[3] == c_id:
#         to_fill = marker[2] - marker[1]
#     n += to_fill * str(c_id)
#     for c_i in range(i, i+to_fill):
#         checksum += c * c_id
#         c += 1
#     if marker[3] == c_id:
#         break

print(checksum) #1928
print(n) #1928
