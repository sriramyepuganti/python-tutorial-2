#decorator
def main(sub):
    print("msg from parent")
    sub()
def sub():
    print("msg from child")
read = main(sub)

#@decorator

def parent(sub):
    print("msg from parent")
    sub()
@parent
def child():
    print("msg from child")