from re import finditer
def solution(s):
     return ' '.join([m.group(0) for m in finditer('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', s)])
