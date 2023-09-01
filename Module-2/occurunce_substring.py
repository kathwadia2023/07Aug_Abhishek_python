# Write a Python program to count occurrences of a substring in a string.

string = '''Paprika tabasco pepper Italian linguine puttanesca cremini 
            mushrooms Thai sun pepper cozy butternut crunchy ginger carrot 
            spiced juice summer fruit salad chai tea strawberries enchiladas 
            leek chocolate red pepper dill basmati crispy iceberg lettuce habanero 
            golden ghost pepper avocado basil pesto cherry bomb hummus tasty cozy 
            cinnamon oatmeal. Lychee delightful blueberry scones blueberry pops vine
            tomatoes shiitake mushrooms cocoa peaches picnic double dark chocolate 
            Chinese five-spice powder zesty tofu pad thai smoked tofu. Chickpea 
            crust pizza roasted peanuts crumbled lentils grains raspberry fizz one bowl
            street style Thai basil tacos Sicilian pistachio pesto dark chocolate 
            hearty figs tomato and basil miso dressing grenadillo macadamia nut 
            cookies smoky maple tempeh glaze black beans almond milk chai latte rich 
            coconut cream sandwiches mangos.'''
substring = 'co'


result = string.count(substring)
print("Number of substring occurrences:", result)