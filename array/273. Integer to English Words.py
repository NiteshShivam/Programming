'''
https://leetcode.com/problems/integer-to-english-words/description/
'''
class Solution:
    def numberToWords(self, num: int) -> str:
        if num==0:
            return "Zero"
        one_two_19  =[
            'One','Two','Three','Four','Five','Six','Seven','Eight','Nine',
            'Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen',
            'Seventeen','Eighteen','Nineteen'
        ]
        twenty_to_90 = [
            'Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety'
        ]
        def find(num):
            if num==0:
                return []
            if num<20:
                return [one_two_19[num-1]]
            if num<100:
                return [twenty_to_90[num//10-2]] +find(num%10)
            return [one_two_19[num//100-1]]+["Hundred"]+find(num%100)
        def splitNumber(num):
            Trillion = (num//1000000000000)%1000
            Billion = (num//1000000000)%1000
            Million = (num//1000000)%1000
            Thousand = (num//1000)%1000
            unit = num%1000
            return Trillion,Billion,Million,Thousand,unit
        Trillion,Billion,Million,Thousand,unit = splitNumber(num)
        result = []
        if Trillion:
            result +=find(Trillion) + ["Trillion"]
        if Billion:
            result += find(Billion) + ["Billion"]
        if Million:
            result += find(Million) + ["Million"]
        if Thousand:
            result += find(Thousand) + ["Thousand"]
        
        
        if unit:
            result += find(unit)
        return " ".join(result).strip()
