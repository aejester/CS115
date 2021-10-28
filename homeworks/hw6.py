"""
Created on 10/15/2021
@author:   Ryan Monaghan, Prithvinarayan Revuri
Pledge:    I pledge my honor I have abided by the Stevens Honor System.

CS115 - Hw 6
"""

from functools import reduce

# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.

# THIS CODE IS ELLIGIBLE FOR THE 5% EXTRA CREDIT.

def base10_to_base2(n: int):
    """Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned."""
    if n == 0:
        return ""

    return base10_to_base2(n//2) + str(n % 2)

def base2_to_base10(s):
    """Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0."""
    if len(s) == 0:
        return 0
    
    return (int(s[0]) * (2**(len(s)-1))) + base2_to_base10(s[1:])

def group_characters(s: str, prev_s=""):
    """Splits groups of characters into groups of 31 or less."""
    if len(s) == 0:
        return [prev_s] if prev_s != "" else []
    elif prev_s == "" or s[0] == prev_s[0]:
        if len(prev_s) == MAX_RUN_LENGTH:
            return [prev_s] + group_characters(s[1:], s[0])
        else:
            return [] + group_characters(s[1:], s[0]+prev_s)
    else:
        return [prev_s] + group_characters(s[1:], s[0])

def compress_helper(bitlist: list[str], final_bit=""):
    """A function that does the heavy lifting for the compress function."""
    if len(bitlist) == 0:
        return []
    elif len(bitlist) >= 2 and bitlist[0][0] == bitlist[1][0]:
        return [("0" * (COMPRESSED_BLOCK_SIZE-len(bitlist[0])) + base10_to_base2(len(bitlist[0]))), "0"*COMPRESSED_BLOCK_SIZE, ("0" * (COMPRESSED_BLOCK_SIZE-len(bitlist[1])) + base10_to_base2(len(bitlist[1])))] + compress_helper(bitlist[2:], bitlist[1][0] if len(bitlist[2:]) == 1 else "")
    else:
        pre_final = [("0" * (COMPRESSED_BLOCK_SIZE-len(bitlist[0])) + base10_to_base2(len(bitlist[0])))] + compress_helper(bitlist[1:])
        final = ["0" * COMPRESSED_BLOCK_SIZE] + pre_final if bitlist[0][0] == final_bit else pre_final
        return final

def compress(s: str):
    """Compresses binary string s using a run length encoding algorithm."""
    bitlist = group_characters(s)
    compressed = compress_helper(bitlist)
    return "".join(["0" * COMPRESSED_BLOCK_SIZE] + compressed if bitlist[0][0] == "1" else compressed)

def uncompress(s: str, accum=0):
    """Uncompresses a run length encoded binary string."""
    if len(s) == 0:
        return ""
    return str(accum % 2) * base2_to_base10(s[:COMPRESSED_BLOCK_SIZE]) + uncompress(s[COMPRESSED_BLOCK_SIZE:], accum+1)

def compression(s):
    """Returns the compression ratio of a binary string and a run length encoded binary string."""
    return len(compress(s)) / len(s)

#LIST OF TEST CASES:

#Penguin: "00011000"+"00111100"*3 + "01111110"+"11111111"+"00111100"+"00100100"
#Compression Ratio: 1.265625

#Smile: "0"*8 + "01100110"*2 + "0"*8 + "00001000" + "01000010" + "01111110" + "0"*8
#Compression Ratio: 1.21875

#Five: "1"*9 + "0"*7 + "10000000"*2 + "1"*7 + "0" + "00000001"*2 + "1"*7 + "0"
#Compression Ratio: 0.8125

#Q: explain what is the largest number of bits that your compress algorithm could possibly use to encode a 64-bit string/image.
#A: the largest number of bits we could use is 6 bits, if a image is 64 bits of only white or only black, then we would return a binary number of 100000 which is 6 bits.

#Q: argue to NASA that Professor Lai is Lai-ing—such an algorithm cannot  exist! Try to make your reasoning as convincing and water-tight as possible. (In essence, you are proving that such an algorithm cannot exist.)
#A: The reason why an algorithm like this cannot work is because even if your compressed block size was a singular bit (which it cant be because you cannot represent multiple numbers in one bit) if there was a 64bit long string of repeating 01 or repeating 10
# it would give you a compression of the same length. This means her LaiCompress algorithm cannot compress every image into a small bit of data.