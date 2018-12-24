
flowers = [["Rose", "Red"], ["Snapdragon", "White"], ["Daisy", "White"], ["Lily", "Yellow"],]

secondFlowers = flowers

print(secondFlowers[1])

print(secondFlowers[1][1])
secondFlowers[1] = ["Lilac", "Purple"]
print(secondFlowers[1])
secondFlowers[1][1] = "Pink"

print(flowers)

# Assuming products is declared as
# #
# # products = (('No. 5', 'perfume', 'Chanel'),
# #             ('Inflallible', 'cosmetic', "L'Oreal"),
# #             ('Poison', 'perfume', 'Dior'),
# #             ('Double Wear', 'cosmetic', 'Estee Lauder'),
# #             ('Wonder Wing', 'cosmetic', 'Rimmel London')
# #             )
# # Which of the following will produce the output
# #
# # Chanel
# # L'Oreal
# # Dior
# # Estee Lauder
# # Rimmel London

products = (('No. 5', 'perfume', 'Chanel'),
            ('Inflallible', 'cosmetic', "L'Oreal"),
            ('Poison', 'perfume', 'Dior'),
            ('Double Wear', 'cosmetic', 'Estee Lauder'),
            ('Wonder Wing', 'cosmetic', 'Rimmel London'))

for product in products:
    print(product[2])

for product in products:
    name, product_type, company = product
    print(company)

# What is wrong with this code?
#
# imelda = 'More Mayhem', 'Imelda May', 2011, [
#     (1, 'Pulling the Rug'),
#     (2, 'Psycho'),
#     (3, 'Mayhem'),
#     (4, 'Kentish Town Waltz')]
#
# imelda[3].append(5, 'All For You')
# print(imelda[3])


imelda = 'More Mayhem', 'Imelda May', 2011, [
    (1, 'Pulling the Rug'),
    (2, 'Psycho'),
    (3, 'Mayhem'),
    (4, 'Kentish Town Waltz')]

print(imelda[3])
# imelda[3].append(5, "All For You")  -- This line is wrong because A tuple must be enclosed in Parenthesis when passed
# to a function. The Append will fail because append does not take two arguments.

# the following print statement will append 
imelda[3].append((5, "All For You"))
print(imelda[3])




