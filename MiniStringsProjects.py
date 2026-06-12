# Project 1: String Analyzer
sentence = input("Enter asentence: ")
print("length:",len(sentence))
print("Upper Case:",sentence.upper())
print("Lower Case:",sentence.lower())
Words = sentence.split()
print("Total Words:",len(Words))
count = 0

for ch in sentence:
    if(ch.lower() in "aeiou"):
        count+=1


print("Total Vowels:",count)
# Project 2: Username Checker
username = input("Enter a username: ")
if username.isalnum():
    print("Contains only letter and digits")
else:
    print("Contains other than letters and digits")    
if len(username)> 0 and username[0].isalpha():
    print("starts with Letter")
else:
    print("Does not start from letter")
if len(username)>= 5:
    print("Contains required characters")            
else:
    print("Characters are lesser than 5")  
# Project 3: Email Checker
Email = input("Enter Your Email: ")
if("@" in Email and Email.endswith(".com") and " " not in Email ):
    print("Valid Email")
else:
    print("Invalid Email")

#Project 5: Simple Text Formatter
sentence = input("Enter a Paragraph: ")
print("Upper Case:",sentence.upper())
print("Lower Case:",sentence.lower())
print("Title Case:",sentence.title())
elements = sentence.split()
print("Total Words:",len(elements))
reverse = elements[::-1]
print(" ".join(reverse))

# Project 4: Word Statistics
paragraph = input("Enter a paragraph: ")
word = paragraph.split()
print("Total Words:",len(word))
print("Total Characters:",len(paragraph))
if len(word)==0:
    print("No words entered")
else:
 shortest = word[0]
 longest = word[0]
 for item in word:
    if(len(item) > len(longest)):
     longest = item
    if(len(item) < len(shortest)):
     shortest = item   
 print("Longest Word:",longest)
 print("Shortest Word:",shortest)

