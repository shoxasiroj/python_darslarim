ismlar = ['olim','sanjar','shohruh']
print(f"Salom {ismlar[0].title()} ishlaring yaxshimi?")
print(f"Salom {ismlar[1].title()} ahvollaring yaxshimi?")
print(f"Salom {ismlar[-1].title()} nima gaplar nima ishlar bilan shug`ullanib yuripsan")

sonlar = [1,24,45,87,-22,-24.5,]
sonlar[0] = 4
sonlar[4] = sonlar[4] + 27
print(sonlar)
t_shaxslar = ['Imom Buhoriy','Abu Ali Ibn Sino','Amur Temur','Alisher Navoiy','Zahiriddin Muhammad Bobur']
z_shaxslar = ['Bill Gates','Ilon Mask','Jeff Bezos']
print(f"Men tarixiy shaxslardan {t_shaxslar.pop(3)} bilan,"
      f"zamonaviy shaxslardan esa {z_shaxslar.pop(1)} bilan suhbat qilishni istar edim")

friends = []
friends.append('shohruh')
friends.append('sanjar')
friends.append('umid')
friends.append('ahmad')
friends.append('malik')
friends.append('javohir')
friends.append('sardor')
print(friends)
friends.remove('sanjar')
friends.remove('malik')
friends.remove('javohir')
print(friends)
friends.insert(0,'malik')
friends.insert(2,'sergey')
print(friends)

mehmonlar = []
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop(2))
mehmonlar.append('sarvar')
print(mehmonlar)