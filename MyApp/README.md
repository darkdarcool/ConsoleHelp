# ConsoleHelp

We all have used the console before at one time or another to make text adventures, or even test out functions a what not.

But sometimes, it can be a real hassle. Having to get a typing animation, but not at the right speed. 

Wait no more! The ConsoleHelp pip package makes all of that so much easier! Use the installation table to get started with installing the package!!
| Pip      | pip install ConsoleHelp |
| ----------- | ----------- |
| Replit      | Add ConsoleHelp in the package tab       |
| Poetry   | python -m poetry add ConsoleHelp        |

## Additions:
 
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
put it here.
```
