animals = ['Ravens', 'Pigions', 'Seagulls', 'Penguin', 'Robin', 'Falcon', 'Eagles',]
print(animals)
for animal in animals:
    print(animal)
    print(f"{animal.title()} are great flyers.")
print("All of these animala are birds")

Message0 = ("The first three items in the list are")
print(Message0)
print(animals[0:3])

Message0 = ("Three items from the middle of the list are")
print(Message0)
print(animals[2:5])

Message0 = ("The last three items in the list are")
print(Message0)
print(animals[4:7])



Buffets = ('Pork', 'Steak', 'Chicken', 'Fried Fish', 'Lamb')
print(Buffets[0])
print(Buffets[1])
print(Buffets[2])
print(Buffets[3])
print(Buffets[4])
for Buffet in Buffets:
  print(Buffet)
# Buffet[0] = 3
Buffets = ('Pork', 'Steak', 'Chicken', 'Sushi', 'Mutton')
print("\nModified Buffets")
for Buffet in Buffets:
  print(Buffet)



Multiples = []
for value in range(1, 11):
 Multiple = value * 3
 Multiples.append(Multiple)
print(Multiples)