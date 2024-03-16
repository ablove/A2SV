def split_and_join(line):
    ab=line.split()
    ans="-".join(ab)
    return ans
    
    # write your code here

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
