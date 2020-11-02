def varargs(arg1, *args):
    for a in args:
        print(a)
varargs("one", "two", "three")

def vararg(arg1, *args):
    print("Got ", arg1, " and ", args)

vararg("one")
vararg("one", "two")
vararg("one", "two", "three", "four")