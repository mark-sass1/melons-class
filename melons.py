"""Classes for melon orders."""

import random
import datetime

class AbstractMelonOrder:
    """An abstract base class that other Melon Orders inherit from."""

    def get_total(self):
        """Calculate price, including tax."""

        base_price = self.get_base_price()
        
        # update christmas melon to cost 1.5 times
        if self.species == "christmas melon":
            base_price = (base_price * 1.5)
        
        # if internation order less than < $10, add $3 fee.
    
        total = (1 + self.tax) * self.qty * base_price

        if self.order_type == "internation" and self.qty < 10:
            total += 3
        
        return total

    def get_base_price(self):
        
        #if time between 8-11, add $4 surcharge to new_base
        
        time = datetime.datetime.now()
        hour = time.hour
        day = time.day

        if hour in range(8, 12) and day in range(1, 6):
            base = random.choice(range(5, 10)) + 4 
        #else just $5 base
        else:
            base = 5 
        
    
        return base
    
    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True
  


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = "domestic"
        self.tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder): 
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.country_code = country_code
        self.shipped = False
        self.order_type = "international"
        self.tax = 0.17

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
    

class GovernmentMelonOrder(AbstractMelonOrder):
    
    def __init__(self, species, qty,):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.tax = 0.0
        self.order_type = "goverment"
        self.passed_inspection = False

    def mark_inspection(self, passed):
       self.passed_inspection = passed


# order1 = InternationalMelonOrder('watermelon', 5, "BR")
# order1.get_total()
