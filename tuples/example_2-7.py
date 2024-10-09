
#%%
# Example2-7.Tuples used as records
#%%
lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'),
    ('ESP', 'XDA205856')]
for passport in sorted(traveler_ids):
    print('%s/%s' % passport)
#%%
lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'),
    ('ESP', 'XDA205856')]
for passport in sorted(traveler_ids):
    print(f'{passport}')

#%%
latitude, longitude = lax_coordinates  # tuple unpacking
print(latitude)
print(longitude)

#%%
divmod(20, 8)
...(2, 4)
t = (20, 8)
divmod(*t)
...(2, 4)
quotient, remainder = divmod(*t)
quotient, remainder
...(2, 4)
# %% [markdown] The preceding code also shows a further use of tuple unpacking: enabling functions to return multiple
# values in a way that is convenient to the caller. For example, the os.path.split() function builds a tuple (path,
# last_part) from a filesystem path:
#%%
import os
_, filename = os.path.split('/home/luciano/.ssh/idrsa.pub')
filename
..."idrsa.pub"
#%% [markdown]
# # Using * to grab excess items
#%%
a, b, *rest = range(5)
a, b, rest
...(0, 1, [2, 3, 4])
a, b, *rest = range(3)
a, b, rest
...(0, 1, [2])
a, b, *rest = range(2)
a, b, rest
...(0, 1, [])




