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

## Expected Behavior

Here is the expected usage statement. The program must have the guess as a required input: 
<html>
  
    $ ./Hangman.py 
    usage: Hangman.py [-h] -g str [-c int]
    Hangman.py: error: the following arguments are required: -g/--guess
    dhcp-10-132-136-25:14-Open-Assignment antoniogutierrez-jaramillo$ 
</html>

If `-h` is input, this should appear: 
<html>
  
    $ ./Hangman.py -h
    usage: Hangman.py [-h] -g str [-c int]

    Argparse Python script

    optional arguments:
      -h, --help            show this help message and exit
      -g str, --guess str   Guess string (default: None)
      -c int, --choice int  Word choice (default: 1)

</html>
## Expected Outcome

## Test Suite 
<html>
  
    $ make test
    python3 -m pytest -v test.py 
    ============================= test session starts ==============================
    platform darwin -- Python 3.7.1, pytest-4.0.2, py-1.7.0, pluggy-0.8.0 -- /anaconda3/bin/python3
    cachedir: .pytest_cache
    rootdir: /Users/antoniogutierrez-jaramillo/14-Open-Assignment, inifile:
    plugins: remotedata-0.3.1, openfiles-0.3.1, doctestplus-0.2.0, arraydiff-0.3
    collected 12 items                                                             
    test.py::test_usage PASSED                                               [  8%]
    test.py::test_bad_args PASSED                                            [ 16%]
    test.py::test_good_one PASSED                                            [ 25%]
    test.py::test_good_two PASSED                                            [ 33%]
    test.py::test_good_three PASSED                                          [ 41%]
    test.py::test_good_four PASSED                                           [ 50%]
    test.py::test_good_five PASSED                                           [ 58%]
    test.py::test_good_six PASSED                                            [ 66%]
    test.py::test_good_seven PASSED                                          [ 75%]
    test.py::test_good_eight PASSED                                          [ 83%]
    test.py::test_good_nine PASSED                                           [ 91%]
    test.py::test_good_ten PASSED                                            [100%]
    
    ========================== 12 passed in 0.65 seconds ===========================
</html>
`
