# ConsoleHelp

We all have used the console before at one time or another to make text adventures, or even test out functions a what not.

But sometimes, it can be a real hassle. Having to get a typing animation, but not at the right speed. 

Wait no more! The ConsoleHelp pip package makes all of that so much easier! Use the installation table to get started with installing the package!!

|Manager          |Command                                       |
|:----------------|:---------------------------------------------|
|**pip**          |`pip install ConsoleHelp`                          |
|**poetry**       |`python -m poetry add ConsoleHelp`                 |
|**Repl.it**      |Search `ConsoleHelp` in the package tab and add it.(coming soon)|     |

# Additions:
 
Printing in python is nice an all, but sometimesI just looks so premade. To solve this, you need to make it look like someone is typing out text, **LIVE**. But how do you do that. Well, we may not show the code, but we sure can show you how to use in in console help! Here is a demonstration:

``` python
import ConsoleHelp as window # We recomend you change the name to something that is not ConsoleHelp
window.sp("Hello World")
```

This will simulate typing. Cool right! Try it out!

But while this works, maybe you want color? Maybe you need important text to stand out so the user will pay more attantion to it. Well, we took that into account too! 

First, we have printing with the colored text. We allow you to use this by doing:
```python
import ConsoleHelp as window # We recomend you change the name to something that is not ConsoleHelp
window.printred("This will be red")
```

It will then log your string into the terminal to be printed as red text. You can get a full list of them here:

* `printred(`
* `printgreen(`
* `printorange(`
* `printcyan(`
* `printblue(`
* `printmagenta(`

That is a full list of them now, but there will be so many more coming to you in the future! And most likely they will be moved to another class function, so make sure to follow our readme's to make sure you have the latest updates!

Now, I'm sure that some of you are asking, "But how do I get the sp function to have color". We also took the liberty of designing that too! It is in the color class function right now, it is small, but many things will be moved there and there is more to be developed there. But, here is how the sp function can have color in it:
``` python
import ConsoleHelp as window # We recomend you change the name to something that is not ConsoleHelp
window.color.spc("This will be red", 'red')
```

Let's break down how this function works. The window is our import(duh), and color is the class it is apart of. The color class is small curently, but will grow in time! After that, is spc. The the sp in spc stands for slow print, and the c in there stands for color. So, it means slow print color. Cool right! Then in quotation marks, you can put in your text, after that, put a comma and in quots put in your color. We have the same colors as the print func, so to find the colors, go there!.

## Math Module!

The math module is made to make your math needs easier, and faster! A lot of people are bad at math, and this class function will make it easier. We have addition, subtraction, division, and mulitplacation. To use this, do:

``` python
import ConsoleHelp as window # We recomend you change the name to something that is not ConsoleHelp
window.math.add(1, 2)
```
This will return the number `3`. We also have

* `window.math.add(1, 2)`
* `window.math.subtract(4, 1)`
* `window.math.multiply(1, 3)`
* `window.math.divide(6, 2)`

But there is one very special math function. It is called `window.math.rand(num1, num2)`. 
