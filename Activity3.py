class India:
    def capital(self):
        print("The capital of India is New Delhi")
    def language(self):
        print("The main spoken language in India is Hindi")
    def type(self):
        print("India is a developing country")

class USA:
    def capital(self):
        print("The capital of US is Washington DC")
    def language(self):
        print("The most common language spoken in the US is English")
    def type(self):
        print("US is a developed country")

objIndia = India()
objUS = USA()

for i in (objIndia, objUS):
    i.capital()
    i.language()
    i.type()
    



