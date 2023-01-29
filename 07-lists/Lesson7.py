ismlar = ['dima', 'vika', 'olya']

print("Привет", ismlar[0])
print("как дела", ismlar[1])
print("здорова", ismlar[2])

sonlar = [12, 17, -14, 13.20, -46]
sonlar[0] = 15
sonlar[2] = sonlar[2] + 25
print(sonlar[0] + sonlar[3])
print(sonlar)

t_shaxslar = ['alisher navoiy', 'amir temur']
z_shaxslar = ['shavkar mirziyoyev', 'vladimir putin']
print(f"Men tarixiy shaxslardan {t_shaxslar.pop(0).title()} bilan, "
      f"zamonaviy shaxslardan esa {z_shaxslar.pop(1).title()} bilan "
      f"suhbat qilishni istar edim")

friends = []
friends.append('ahmad')
friends.append('sanjar')
friends.append('shahboz')
friends.append('bobur')
friends.append('farrux')
friends.append('shohruh')
print(friends)

friends.remove('sanjar')
del friends[1]
print(friends)

friends.append('olim')
friends.insert(1, 'baxriyor')
friends.insert(3, 'sarvar')


mehmonlar = []
mehmonlar.append(friends.pop(2))
mehmonlar.append(friends.pop(4))
mehmonlar.append('sobir')
print(mehmonlar)
