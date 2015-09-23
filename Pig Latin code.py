#Rebekah Orth
#Week 3: Pig Latin
#CIS 125 FA 2015

def main():
    #prompt user for English word
    word = input("Please enter an English word to translate (using all lowercase letters): ")
    
    #vowels listed as string, using both upper and lower case
    vowel = "aeiouAEIOU"
    
    #making all letters lowercase
    pig = word.lower()
    
    #print pig latin word if first letter is a vowel
    if pig [0] in vowel:
        print(pig+"yay")
    #print pig latin word if first letter is consonant
    else:
        print(pig[1:]+pig[0]+"ay")
main()