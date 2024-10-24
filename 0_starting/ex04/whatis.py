Create a script that takes a number as argument, checks whether it is odd or even,
and prints the result.
If more than one argument is provided or if the argument is not an integer, print an
AssertionError.


Expected output:
$> python whatis.py 14
I'm Even.
$>
$> python whatis.py -5
I'm Odd.
$>
$> python whatis.py
$>
$> python whatis.py 0
I'm Even.
$>
$> python whatis.py Hi!
AssertionError: argument is not an integer
$>
$> python whatis.py 13 5
AssertionError: more than one argument is provided
$>