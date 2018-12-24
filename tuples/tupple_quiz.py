# given the tuple below that represents the Imelda May album "More Mayhem", write code to print the album details,
# followed by a listing of all the tracks in the album.
#
# indent the tracks by a single tab stop when printing them ( remember you can pass more than one item to the print
# function, separating them with comma

Imelda = "More Mayhem", "Imelda", 2011, ([
    (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz")])
print(len(Imelda[3]))
title, artist, year, tracks = Imelda
print(title)
print(artist)
print(year)

for song in tracks:
    tracks, title = song
    print("\t Track Number {}, Title : {} ".format(tracks, title))

# Even though we have new track the code still works

Imelda2 = "More Mayhem", "Imelda", 2011, ([
    (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz")])
Imelda2[3].append((5, "All For You"))
title2, artist2, year2, tracks2 = Imelda2
Imelda2[3].append((6, "Eternity"))
print(title2)
print(artist2)
print(year2)
print("=" * 30)
for song2 in tracks2:
    tracks2, title2 = song2
    print("\t Track Number {}, Title : {} ".format(tracks2, title2))

trees = ["Larch", "Larch"]
identifiedTrees = trees
trees.append("Oak")

print(identifiedTrees)