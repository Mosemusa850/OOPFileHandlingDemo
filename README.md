PythonOOPAssignmentsThis repository contains two Python programs demonstrating Object-Oriented Programming (OOP) concepts, including classes, inheritance, polymorphism, encapsulation, and file handling with concurrent execution.Contentssmartphone.py  Implements a Smartphone class and a GamingSmartphone subclass.
Features:Constructor (__init__) to initialize attributes (brand, model, storage).
Encapsulation with private attributes (e.g., __storage) and getter methods.
Inheritance and polymorphism via overridden display_info method.
Saves smartphone details to a text file (smartphone.txt or gaming_smartphone.txt).

Demonstrates file handling with error handling for permissions.

animal_polymorphism.py  Implements an Animal base class with Dog and Bird subclasses to demonstrate polymorphism.
Features:Polymorphic move() method (e.g., "swinging tail" for Dog, "flapping wings" for Bird).
Concurrent file writing using threading to log animal actions to animal_actions.txt.
Synchronization with threading.Event to ensure file creation before writing.
Error handling for file operations.
