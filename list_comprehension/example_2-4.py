#%% [markdown]
# Listcomps can generate lists from the Cartesian product of two or more iterables. The items that make up the
# cartesian product are tuples made from items from every input iterable. The resulting list has a length equal to
# the lengths of the input iterables multiplied.

# # Example2-4.Cartesian product using a list comprehension
#%%
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors
                         for size in sizes]
print(tshirts)
#%%
for color in colors:
    for size in sizes:
        print((color, size))

#%%
for size in sizes:
    for color in colors:
        print((color, size))
#%%
tshirts = [(color, size) for size in sizes
                         for color in colors]
print(tshirts)