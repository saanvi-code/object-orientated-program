class parrot:
    species="bird"
    def __init__(self,name,age):
        self.n=name
        self.a=age

blu=parrot("blu",6)
gold=parrot("gold",2)

print("the species of parrot blu is a {}".format(blu.species))
print("the species of parrot gold is {}".format(gold.species))

print("the name and age of the first parrot are {}and{} ".format(blu.n,blu.a))
print("the name and age of the second parrot are {}and{} ".format(gold.n,gold.a))