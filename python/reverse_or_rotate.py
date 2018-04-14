'''
The input is a string str of digits. Cut the string into chunks (a chunk here is a substring of the initial string) of size sz (ignore the last chunk if its size is less than sz).

If a chunk represents an integer such as the sum of the cubes of its digits is divisible by 2, reverse that chunk; otherwise rotate it to the left by one position. Put together these modified chunks and return the result as a string.

If

    sz is <= 0 or if str is empty return ""
    sz is greater (>) than the length of str it is impossible to take a chunk of size sz hence return "".

Examples:
revrot("123456987654", 6) --> "234561876549"
revrot("123456987653", 6) --> "234561356789"
revrot("66443875", 4) --> "44668753"
revrot("66443875", 8) --> "64438756"
revrot("664438769", 8) --> "67834466"
revrot("123456779", 8) --> "23456771"
revrot("", 8) --> ""
revrot("123456779", 0) --> "" 
revrot("563000655734469485", 4) --> "0365065073456944"
'''

def revrot_chunk(chunk, sz):
    try:
        int(chunk)
        num_odds = 0
        for i in range(sz):
            if int(chunk[i])%2 != 0:
                num_odds = num_odds+1
        if num_odds%2 == 0:
            # reverse chunk
            return chunk[::-1]
        else:
            # rotate chunk
            return chunk[1::]+chunk[0]

    except ValueError:
        # rotate chunk
        return chunk[1::]+chunk[0]

def revrot(strng, sz):
    l = len(strng)
    if(strng == "" or sz <= 0 or sz > l):
        return ""
    else:
        output_string = ""
        # number of chunks of size sz
        nc = l // sz
        for i in range(nc):
            chunk = strng[i*sz:(i+1)*sz]
            output_string += revrot_chunk(chunk, sz)
        return output_string