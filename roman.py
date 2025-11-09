class Roman: 

    def roman_numeral(self, number):

        val = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
            (1, 'I'),
        ]

        res = ''
        num = number
        

        for (n, roman) in val:
            (x, num) = divmod(num, n)
            res += roman * x

        return res
    
converter = Roman()

user = int(input("Enter a whole number: "))
print(f"{user}: is {converter.roman_numeral(user)}")