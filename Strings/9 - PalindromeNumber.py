def isPalindrome(self, x: int) -> bool:
    l = list(str(x))
    l.insert(0, "placeholder")
    for i in range(1, len(l)):
        if l[i] != l[-i]:
            return False
    return True