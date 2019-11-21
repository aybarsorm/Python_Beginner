1-)Kullanıcıdan bir kelime alıp bu kelimeyi bir değişkene aktardıktan sonra yan yana 10 kere yazdırınız.

kelime = input("kelime yazınız")

print(kelime*10)


2-)Kullanıcıdan aldığınız iki sayının çarpımı ile bölümlerinin arasındaki fark nedir?

x = int(input("1. tam sayıyı giriniz: "))
y = int(input("2. tam sayıyı giriniz: "))

print((x*y)-(x/y))



Listeler:
3-) a-) "Uludag Üniversitesi Yapay Zeka Topluluğu" 'nu liste haline getirip "Yapay" kelimesinin indexini ekrana yazdırınız.
    b-) Daha sonra oluşturduğunuz bu listeye "üniversite"den sonra "Bursa" kelimesini ekleyiniz.
    c-) En sondaki kelimeyi bu listeden siliniz.
    d-)Listedeki Kelimleri sondan başa doğru sıralayınız.
#a
liste = ["Uludag", "Üniversitesi", "Yapay", "Zeka", "Topluluğu"]
print(liste.index("Yapay"))

#b
liste.insert(2,"Bursa")

#c
liste.pop()

#d
liste[::-1]
    
Set:
4-) "lorem ipsum dolor sit amet ipsum dolor dolor sit amet  " 
    a-)cümlesindeki her harfin bir kere yazdığı kümeyi oluşturunuz.
    b-)bu cümlenin uzunluğunu ekrana yazdırınız.
#a
yazi2 = "lorem ipsum dolor sit amet ipsum dolor dolor sit amet  "

kume = tuple(yazi)

#b
print(len(yazi))

  
 Dict:
5-)Bir sözlük oluşturup 4 farklı bilgiyi bu sözlükte depolayınız.(indexleri 1,2,3,4 olacak şekilde)

sozluk = {"car" : "araba", "snow" : "kar", "banana" : "muz", "fly" : "sinek"}
