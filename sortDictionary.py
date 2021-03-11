fishes = [{"name": "Northern Pike", "average": 35},
          {"name": "Sunfish", "average": 13}, {"name": "Walleye", "average": 67}]

# def sortDic(fish):
#     # return fish["average"]
#
#
# fishes.sort(key=sortDic)

# another way of doing

fishes.sort(key=lambda fish: fish["average"])

print(fishes)
