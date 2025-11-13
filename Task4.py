fruits = ["apple","banana","kiwi"]
vowels = "aeiou"
count = {word: 
         sum(1 for ch in word if ch.lower() in vowels) 
         for word in fruits}
print(count)

