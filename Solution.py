def canConstruct(ransomNote, magazine):
    for i in ransomNote:
        if magazine.count(i)<ransomNote.count(i):
            return False
    return True
a='aa'
b='ab'
print(canConstruct(a,b))