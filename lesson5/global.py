from watchdog.observers.fsevents2 import message

greeting = "hello"

def greett(name):
    message = f"{greeting}, {name}"
    print(message)

greett("Egzon")

print(greeting)