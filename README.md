# 14-Open-Assignment  
For this assignment, you will create a game of Hangman. 
## How the game will work. 
The inputs will be one `-int` input and one `-str` input. The integer input will be used to choose one of ten words. The string input will be checked against the selected word input.

For simplicity's sake, I recommend having all words be the same length. For example: 
1. Arcosanti
2. Intercept
3. Positions
4. Collected
5. Gemstones
6. Cellulose 
7. Mastodons
8. Meteorite
9. Phoenixes
10. Fireflies 

If the string input is too long or too short, the program will print a `die` statement. 
If the string perfectly matches the word, the program will end and print 'You Win!'.
If the string is *not* a perfect match, the program will print a string with underscores `_` in the place of mismatched words.
## How to perform this assignment
For the initialization, I would strongly recommend using a dictionary to assign the words to the numbers. The program will then need to iterate through both strings letter by letter, printing the letter when they match and printing an underscore when they do not. 
