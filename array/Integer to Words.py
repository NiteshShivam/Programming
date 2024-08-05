'''

https://www.geeksforgeeks.org/problems/number-to-words0335/1
'''

class Solution:
    def convertToWords(self, n):
        if n==0:
            return 'zero'
        one_to_19=[
            'one','two','three','four','five','six','seven','eight',
            'nine','ten','eleven','twelve','thirteen','fourteen','fifteen',
            'sixteen','seventeen','eighteen','nineteen'
            
            ]
        tens =  [
            'twenty','thirty','forty','fifty','sixty','seventy','eighty',
            'ninety'
            ]
        places = ["",
            'thousand','lakh','crore'
            ]
        def convert_hundred(num):
            if num==0:
                return []
            if num<20:
                return [one_to_19[num-1]]
            if num<100:
                return [tens[num//10-2]] + convert_hundred(num%10)
            
            
            t = [one_to_19[num//100-1]] + ['hundred']
            t1 = convert_hundred(num % 100)
            if len(t1):
                return t + ['and'] + t1
            else:
                return t
        def split_number(n):
            crore = n//10000000
            lakh = (n//100000)%100
            thousand = (n//1000)%100
            hundred = (n//100)%10
            units = n%1000
            return units,hundred,thousand,lakh,crore
            
        units,hundred,thousand,lakh,crore = split_number(n)
        word_list = []
        if crore:
            word_list += convert_hundred(crore) +['crore']
            if not lakh and not thousand and not hundred and units:
                word_list+= ['and']
                
        if lakh:
            word_list += convert_hundred(lakh) +['lakh']
        if thousand:
            word_list += convert_hundred(thousand) +['thousand']
            if not hundred and units:
                word_list+= ['and']
                
        
        if units:
            word_list+=convert_hundred(units)
        return ' '.join(word_list).strip()            
