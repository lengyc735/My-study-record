print("Let's practice everything.")
print('You\'d need to konw \'bout escapes with \\ that do \nnewlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\twhere there is none.
"""

print('----------')
print(poem)
print('----------')

five = 10 - 2 + 3 - 6
print("This should be five: %s" % five)

def secret_formula(stared):
    jelly_beans = stared * 500
    jars = jelly_beans / 100
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)  # 分别赋值

print("With a starting point of: %d" % start_point)
print("We'd have %d beans, %d jars, and %d cartes." % (beans,jars, crates))

start_point = start_point / 10

print("We can also do that this way:")
print("We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point))