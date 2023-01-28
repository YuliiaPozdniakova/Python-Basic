class String(str):
    def __add__(self, other):
        str(other)
        return f'{self}{other}'

    def __sub__(self, other):
        s = self
        o = str(other)
        if s.find(o) != -1:   #  o.lower() in s.lower()
            start = s.find(o)
            end = start + len(o)
            result = s[:start]+s[end:]
            return f'{result}'
        else:
            return f'{s}'


new_str = String('1777') + 3
print(type(new_str))
print(new_str)
