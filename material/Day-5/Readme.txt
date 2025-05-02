Day 5
.......................................
Will cover
1. oops classes and objects

Python supports several types of inheritance:
1. Single inheritance: A class inherits from only one parent class.
2. Multiple inheritance: A class inherits from multiple parent classes.
3. Multilevel inheritance: A class inherits from another class, which in turn inherits from another class. 
4. Hierarchical inheritance: Multiple classes inherit from the same parent class.
5. Hybrid inheritance: A combination of two or more types of inheritance.

Example 
# Single inheritance
class Parent:
    def func1(self):
        return "Parent"
class Child(Parent):
    def func2(self):
        return "Child"

# Multiple inheritance
class Parent1:
    def func1(self):
        return "Parent 1"
class Parent2:
    def func2(self):
        return "Parent 2"
class Child(Parent1, Parent2):
    def func3(self):
        return "Child"

# Multilevel inheritance
class Grandparent:
    def func1(self):
        return "Grandparent"
class Parent(Grandparent):
    def func2(self):
        return "Parent"
class Child(Parent):
    def func3(self):
        return "Child"

# Hierarchical inheritance
class Parent:
    def func1(self):
        return "Parent"
class Child1(Parent):
    def func2(self):
        return "Child 1"
class Child2(Parent):
    def func3(self):
        return "Child 2"

# Hybrid inheritance
class Grandparent:
    def func1(self):
        return "Grandparent"
class Parent1(Grandparent):
    def func2(self):
        return "Parent 1"
class Parent2(Grandparent):
    def func3(self):
        return "Parent 2"
class Child(Parent1, Parent2):
    def func4(self):
        return "Child"
