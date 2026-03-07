from abc import ABC,abstractmethod

class Phone(ABC):
    
    @abstractmethod
    def call(self):
        pass

    @abstractmethod
    def charging(self):
        pass

    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def massaging(self):
        pass
    

class Samsung(Phone):

    def call(self):
        print("It provide unittrupted incoming and outgoing call with live voice Translation")
    
    def charging(self):
        print("It has fast charging facilty")

    def display(self):
        print("It provide OLED display with all S-series")

    def massaging(self):
        print("It now provide massaging with Bixby AI massaging for all its premium phone")

class OnePlus(Phone):
    def call(self):
        print("It provide unittrupted incoming and outgoing call but does not provide live voice Translation")
    
    def charging(self):
        print("It also has fast charging facilty")

    def display(self):
        print("It also provide OLED display with all S-series")

    def massaging(self):
        print("It uses Gemini AI in massaging")

class Iphone(Phone):
    def call(self):
        print("It provide unittrupted incoming and outgoing call but does not provide live voice Translation")
    
    def charging(self):
        print("It does provide fast charging facilty but not as fast as other 2 provide")

    def display(self):
        print("It also provide OLED display with all S-series")

    def massaging(self):
        print("It uses Siri AI in massaging")

    def security(self):
        print("it provide one of the best security to customer among the other Popular Brands")


ph_1=Samsung()

ph_1.call()
ph_1.charging()
ph_1.display()
ph_1.massaging()

ph_2=OnePlus()

ph_2.call()
ph_2.charging()
ph_2.display()
ph_2.massaging()

ph_3=Iphone()

ph_3.call()
ph_3.charging()
ph_3.display()
ph_3.massaging()
ph_3.security()