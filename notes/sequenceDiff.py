# sales
# alien
def sequenceDiff(s1, s2):
    if s1 == "" or s2 == "":
        return max(len(s1), len(s2))
    elif s1[0] == s2[0]:
        return sequenceDiff(s1[1:], s2[1:])
    else:
        sub = sequenceDiff(s1[1:], s2[1:])
        add = sequenceDiff(s1[1:], s2)
        rem = sequenceDiff(s1, s2[1:])
        return 1 + min(sub, add, rem)

print(sequenceDiff("sales", "alien"))