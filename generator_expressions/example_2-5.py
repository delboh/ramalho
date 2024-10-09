#%%
symbols = '$¢£¥€¤'
mytuple = tuple(ord(symbol) for symbol in symbols)
print(mytuple)


#%%
import array
myarray = array.array('I', (ord(symbol) for symbol in symbols))
print(myarray)

#%% [markdown]
# Example2-6.Cartesian product in a generator expression
#%%
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
for tshirt in ((f'{c} {s}') for c in colors for s in sizes):
    print(tshirt)
