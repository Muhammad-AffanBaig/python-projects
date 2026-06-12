# Challenge 1: Text Analyzer
sentence = input("Enter a Paragraph: ")
if sentence == "":
    print("Paragraph is empty")
else:    
 print("Total Characters:",len(sentence))
 words = sentence.split()
 print("Total words:",len(words))
 shortest = words[0]
 longest = words[0]
 for element in words:
    if len(element)> len(longest):
       longest = element
    if len(element)<len(shortest):
       shortest = element   
 countV = 0 
 countC = 0     
 for ch in sentence:
    if ch.lower() in "aeiou":
       countV +=1
    elif ch.isalpha():
       countC +=1   

 print("Longest Word:",longest)
 print("Shortest word:",shortest)
 print("No of vowels:", countV)
 print("No of consonants:",countC)

        