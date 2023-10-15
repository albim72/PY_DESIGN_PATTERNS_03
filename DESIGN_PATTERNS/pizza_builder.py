from enum import Enum
import time


PizzaProgress = Enum('PizzaProgress','queue preparation baking ready')
PizzaDough = Enum('PizzaDough','thin thick')
PizzaSouce = Enum('PizzaSouce','tomato garlic')
PizzaTopping = Enum('PizzaTopping','mozarella double_mozarella bacon ham mushrooms red_onion oregano')
STEP_DELAY = 3


class Pizza:
    def __init__(self,name):
        self.name = name
        self.dough = None
        self.sauce = None
        self.topping = []

    def __str__(self):
        return self.name

    def prepare_dough(self,dough):
        self.dough = dough
        print(f'prepairing the {self.dough.name} dough of your {self}')
        time.sleep(STEP_DELAY)
        print(f'done with the {self.dough.name} dough')


class MargaritaBuilder:
    def __init__(self):
        self.pizza = Pizza('Margarita')
        self.progress = PizzaProgress.queue
        self.baking_time = 5

    def prepare_dough(self):
        self.progress = PizzaProgress.preparation
        self.pizza.prepare_dough(PizzaDough.thin)

    def add_sauce(self):
        print(f'adding tomato sauce to Your Margarita!')
        self.pizza.sauce = PizzaSouce.tomato
        time.sleep(STEP_DELAY)
        print('Done with the tomato sauce!')

    def add_topping(self):
        topping_desc = 'podwójna mozarella, oregano'
        topping_items = (PizzaTopping.double_mozarella, PizzaTopping.oregno)
        print(f'adding the topping ({topping_desc}) to Your Margarita!')
        self.pizza.topping.append([t for t in topping_items])
        time.sleep(STEP_DELAY)
        print(f'done with the topping ({topping_desc})')

    def bake(self):
        self.progress = PizzaProgress.baking
        print(f'baking Your Margarita for {self.baking_time} s')
        time.sleep(self.baking_time)
        print('Your Margrita is ready!!!')


class CreamyBaconBuilder:
    def __init__(self):
        self.pizza = Pizza('Creamy Bacon')
        self.progress = PizzaProgress.queue
        self.baking_time = 7

    def prepare_dough(self):
        self.progress = PizzaProgress.preparation
        self.pizza.prepare_dough(PizzaDough.thick)

    def add_sauce(self):
        print(f'adding garlic sauce to Your Creamy Bacon!')
        self.pizza.sauce = PizzaSouce.garlic
        time.sleep(STEP_DELAY)
        print('Done with the garlic sauce!')

    def add_topping(self):
        topping_desc = 'mozarella, boczek, szynka, grzyby, czerwona cebula, oregano'
        topping_items = (PizzaTopping.mozarella,
                         PizzaTopping.bacon,
                         PizzaTopping.ham,
                         PizzaTopping.mushrooms,
                         PizzaTopping.red_onion,
                         PizzaTopping.oregno)
        print(f'adding the topping ({topping_desc}) to Your Creamy Bacon!')
        self.pizza.topping.append([t for t in topping_items])
        time.sleep(STEP_DELAY)
        print(f'done with the topping ({topping_desc})')

    def bake(self):
        self.progress = PizzaProgress.baking
        print(f'baking Your Creamy Bacon for {self.baking_time} s')
        time.sleep(self.baking_time)
        print('Your Creamy Bacon is ready!!!')


class Waiter:
    def __init__(self):
        self.builder = None

    def construct_pizza(self,builder):
        self.builder = builder
        steps = (builder.prepare_dough,
                 builder.add_sauce,
                 builder.add_topping,
                 builder.bake)
        [step() for step in steps]

    @property
    def pizza(self):
        return self.builder.pizza
    
def validate_style(builders):
    try:
        input_msg = 'What pizza would You like? [m]argarita or [c]reamy bacon?'
        pizza_style = input(input_msg)
        builder = builders[pizza_style]()
    except KeyError:
        error_msg = 'Sorry, only [m]argarita or [c]reamy bacon!'
        return (False,error_msg)
    return (True,builder)
