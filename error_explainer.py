import os
import configparser
from datetime import datetime
from IPython.display import Markdown as md
from IPython.display import HTML

report = False


def consent():
    """
    Ask for consent to report the first time, and remember this by storing a dot file
    """

    config = configparser.ConfigParser()
    config.read("config.ini")
    dologging = config["Options"].getboolean("logging")
    if not dologging:
        return 
    
    fname = os.path.expanduser(config["Paths"]["consent_file"])

    if os.path.isfile(fname):
        with open(fname, "r") as f:
            report = bool(int(f.read().strip("\n")))
        return report

    message = config["HTML"]["consent_header"]
    if message:
        display(HTML(message))
    
    
    text = """
Do you consent to having your error messages anonymously logged?
Please type Y/N and press return """


    pos = ["y", "yes"]
    neg = ["n", "no"]

    answer = input(text).lower()
    while answer not in pos + neg:
        answer = input("Please input Yes (Y) or No (N) ").lower()
        
    with open(fname, "w") as f:
        if answer in pos:
            f.write("1")
            return True
        else:
            f.write("0")            
            return False
            
    return

def log(error_type, error_val, msg = True, time = True):
    """
    Report the error type and optionally value and date
    """
        
    config = configparser.ConfigParser()
    config.read("config.ini")
        
    fname = os.path.expanduser(config["Paths"]["logging_file"])

    dologging = config["Options"].getboolean("logging")
    if not dologging:
        return 
    
    if not os.path.isdir(os.path.dirname(fname)) and os.path.dirname(fname):
        return        
    
    text = ""
    if time:
        text += f'{datetime.now().strftime("%d/%m/%Y %H:%M:%S"):20s}'
    
    text += f"{repr(error_type):15s} "
    if msg:
        text += str(error_val)
    text += "\n"
    with open(fname, "a") as f:
        f.write(text)
        
    return

def custom_exc(shell, etype, evalue, tb, tb_offset=None):

    config = configparser.ConfigParser()
    config.read("config.ini")
    course = config["Text"]["course_name"]
    course = config["HTML"]["message_final"]
    
    final = course + "<hr>"
    
    shell.showtraceback((etype, evalue, tb), tb_offset=tb_offset)

    if etype == ModuleNotFoundError:
        display(HTML(f"""
    <hr>
    <h2><span style="color:Midnightblue"> {course} help on 'ModuleNotFoundError' error message</span></h2>
    <span style="color:Midnightblue">
    <p></p>    
    Python is telling you: it can't find the module you tried to import.
    <p></p>  
    <p><strong>What to do</strong>:</p>
    <p></p>     
    Look at the line number in your code mentioned in the error message (indicated by </span><span style="color:yellowGreen">----></span> <span style="color:Midnightblue">), and
    <ul>
        <li> Check that the you spelt the module name correctly </li>
    <li> If the module name is spelt correctly, check that the package is installed on your system.</li>
    </ul>
    </span>
    """ + final))


    elif etype == FileNotFoundError:
        display(HTML(f"""
    <hr>
    <h2><span style="color:Midnightblue"> {course} help on 'FileNotFoundError' error message</span></h2>
    <span style="color:Midnightblue">
    <p></p>    
    Python is telling you: it can't open the file.
    <p></p>  
    <p><strong>What to do: </strong></p>
    <p></p>     
    Look at the line number in your code mentioned in the error message (indicated by </span><span style="color:yellowGreen">----></span> <span style="color:Midnightblue">) and check the common causes below.
    <p></p>
    <p><strong> Common causes of this message: </strong></p>
    <p> </p>
    <ul>
    <li> File name spelt incorrectly </li>
    <li> The file doesn't exist yet (if you want to write the file you need to pass "w" as the
        second argument) </li>
    </ul>
    </span>
        """ + final))

    elif etype == ImportError:
        display(HTML(f"""
    <hr>
    <h2><span style="color:Midnightblue"> {course} help on 'ImportError' error message</span></h2>
    <span style="color:Midnightblue">
    <p></p>    
    Python is telling you: it can't find what you are trying to import.
    <p></p>
    <p><strong>What to do: </strong></p>
    <p></p>     
    Look at the line number in your code mentioned in the error message (indicated by </span><span style="color:yellowGreen">----></span> <span style="color:Midnightblue">) and check the common causes below.
    <p></p>
    <p><strong> Common causes of this message: </strong></p>
    <p> </p>
    <ul>
    <li> Variable or function name spelt incorrectly </li>
    <li> Trying to import a variable/function from the wrong module </li>
    </ul>
    </span>
        """ + final))

    elif etype == SyntaxError:
        display(HTML(f"""
    <hr>
    <h2><span style="color:Midnightblue"> {course} help on 'SyntaxError' error message</span></h2>
    <span style="color:Midnightblue">
    <p></p>
    Python is telling you: what you have written isn't valid python code. Most syntax errors are caused by typos.
    <p></p>
    <p><strong> What to do: </strong></p>
    <p></p>
    Look at the position in your code where the ^ points to, on the line indicated by 
    <span style="font-family:Courier New"><span style="color:seagreen">line</span></span>
    <span style="color:yellowGreen"> [number]</span></span><span style="color:Midnightblue">. 
    (Or if ^ points to the start of a line, look at the end of the previous line to find the cause of the error).
    <p></p>
    <p><strong> Common causes of this message: </strong></p>
    <ul>
    <li> Forgetting a colon (:) at the end of an <span style="font-family:Courier New">if, elif, else, for, while, </span> 
    or  <span style="font-family:Courier New">def</span> statement </li>
    <li> Trying to use a reserved word as a variable name. (e.g. <span style="font-family:Courier New">def = 1</span>) </li>
    <li> Different number of opening or closing brackets/braces/quotes </li>
    <li> Missing a comma or having one in an unexpected place </li>
    <li> Forgetting to put quotes around a string </li>
    </ul></span>
    """ + final))

    elif etype == IndentationError:
        display(HTML(f"""
        <hr>
        <h2><span style="color:Midnightblue"> {course} help on 'IndentationError' error message</span></h2>
        <span style="color:Midnightblue">
        <p></p>
        Python is telling you: it has found too much or too little indentation (i.e. number of spaces or tabs).
        <p></p>
        <p><strong> What to do: </strong></p>
        <p></p>
        Look at the position in your code where the ^ points to, on the line indicated by <span style="font-family:Courier New"><span style="color:seagreen">line</span></span><span style="color:yellowGreen"> [number]</span></span><span style="color:Midnightblue">. 
        This is the line that has an inconsistent level of indentation.
        <p></p>
        <p><strong> Common causes of this message: </strong></p>
        <ul>
        <li> Too much or too little indentation (i.e. spaces or tabs) in a function definiton, loop, or conditional statement.  </li>
        <li> Each line in a code block isn't indented equally  </li>
        </ul></span>
    """ + final))


    elif etype == NameError:
        display(HTML(f"""
        <hr>
        <h2><span style="color:Midnightblue"> {course} help on 'NameError' error message</span></h2>
        <span style="color:Midnightblue">
        <p></p>
        Python is telling you: the variable, function, or module you're trying to use can't be found. This is often due to a typo.
        <p></p>
        <p><strong> What to do: </strong></p>
        <p></p>
        Look at the line number in your code mentioned in the error message (indicated by </span><span style="color:yellowGreen">----></span> <span style="color:Midnightblue">) and check the common causes below.
        <p></p>
        <p><strong> Common causes of this message: </strong></p>
        <ul>
        <li> Variable or function not spelt correctly  </li>
        <li> A required module hasn't been imported  </li>
        <li> Forgetting to define a variable  </li>
        <li> The code calls a function or variable  before it's defined. Or the cell that has the definition or import hasn't run  </li>
        <li> Using == when = should be used </li>
        </ul></span>
    """ + final))

    elif etype == TypeError:
        display(HTML(f"""
        <hr>
        <h2><span style="color:Midnightblue"> {course} help on 'TypeError' error message</span></h2>
        <span style="color:Midnightblue">
        <p></p>
        Python is telling you: you're trying to use an operator on the wrong type of object, or you're trying to 
        combine/compare variables that are of incompatible type.
        <p></p>
        <p><strong> What to do: </strong></p>
        <p></p>
        Look at the line number in your code mentioned in the error message (indicated by </span><span style="color:yellowGreen">----></span> <span style="color:Midnightblue">) and check the common causes below.
        <p></p>
        <p><strong> Common causes of this message: </strong></p>
        <ul>
        <li> Strings not converted to int or float before trying to perform a calculation </li>
        <li> A function is called with the incorrect number or type of arguments </li>
        </ul>
        You can also try printing the type() of the variable and check it is what you expect.</span>
        <p></p>
    """ + final))


    elif etype == ValueError:
        display(HTML(f"""
        <hr>
        <h2><span style="color:Midnightblue"> {course} help on 'ValueError' error message</span></h2>
        <span style="color:Midnightblue">
        <p></p>
        Python is telling you: the variable you're using has the correct type but the value isn't acceptable. E.g. trying sqrt(-1).
        <p></p>
        <p><strong> What to do: </strong></p>
        <p></p>
        Look at the line number in your code mentioned in the error message (indicated by </span><span style="color:yellowGreen">----></span> <span style="color:Midnightblue">) and check the common causes below.
        <p></p>
        <p><strong> Common causes of this message: </strong></p>
        <ul>
        <li> Negative value where a positive one is required (e.g. sqrt(-1) ) </li>
        </ul>
    """ + final))

    elif etype == AttributeError:
        display(HTML(f"""
        <hr>
        <h2><span style="color:Midnightblue"> {course} help on 'AttributeError' error message</span></h2>
        <span style="color:Midnightblue">
        <p></p>
        Python is telling you: the variable or function you're asking for isn't provided by the object or module.
        E.g. trying to use .append() on a string, but strings don't support .append().
        <p></p>
        <p><strong> What to do: </strong></p>
        <p></p>
        Look at the line number in your code mentioned in the error message (indicated by the first </span><span style="color:yellowGreen">----></span> <span style="color:Midnightblue">) and check the common causes below.
        <p></p>
        <p><strong> Common causes of this message: </strong></p>
        <ul>
        <li> Variable or function not spelt correctly  </li>
        <li> The variable is of the wrong type; try using type() to see if it is what you expect
        </ul>
        <p></p>
        </span>
    """ + final))

    elif etype == KeyError:
        display(HTML(f"""
        <hr>
        <h2><span style="color:Midnightblue"> {course} help on 'KeyError' error message</span></h2>
        <span style="color:Midnightblue">
        <p></p>
        Python is telling you: you're trying to look up a key in a dictionary that doesn't exist.
        <p></p>
        <p><strong> What to do: </strong></p>
        <p></p>
        Look at the line number in your code mentioned in the error message (indicated by the first
        </span><span style="color:yellowGreen">----></span> <span style="color:Midnightblue">) and
        try the checks below.
        <p></p>
        <p><strong> Things you can check: </strong></p>
        <ul>
        <li> Check if the key is spelt correctly  </li>
        <li> Print out the dict, using print(), to see what it contains  </li>
        </ul>
        <p></p>
        </span>
    """ + final))

    elif etype == IndexError:
        display(HTML(f"""
        <hr>
        <h2><span style="color:Midnightblue"> {course} help on 'IndexError' error message</span></h2>
        <span style="color:Midnightblue">
        <p></p>
        Python is telling you: you're trying to access an element in a data structure
        (e.g. list/tuple/string/array etc) that is bigger than the size of the structure.
        E.g. trying to access the 10th element of a list that is only 9 elements long.
        <p></p>
        <p><strong> What to do: </strong></p>
        <p></p>
        Look at the line number in your code mentioned in the error message (indicated by
        </span><span style="color:yellowGreen">----></span> <span style="color:Midnightblue">) and
        try the checks below.
        <p></p>
        <p><strong> Some things to check: </strong></p>
        <ul>
        <li> If you're using a variable as the index, print it out and make sure the value is what you expect </li>
        <li> Print out the len() of the data structure </li>
        <li> Remember that indices in python start from 0 and go to size -1 </li>
        </ul>
    """ + final))

    elif etype == ZeroDivisionError:
        display(HTML(f"""
        <hr>
        <h2><span style="color:Midnightblue"> {course} help on 'ZeroDivisionError' error message</span></h2>
        <span style="color:Midnightblue">
        <p></p>
        Python is telling you: you're trying to divide by zero.
        <p></p>
        <p><strong> What to do: </strong></p>
        <p></p>
        Look at the line number in your code mentioned in the error message (indicated by the first </span><span style="color:yellowGreen">----></span> <span style="color:Midnightblue">) and check the common causes below.
        <p></p>
        <p><strong> Common causes of this message: </strong></p>
        <p> </p>
        <ul>
        <li> Value in denominator is unexpectedly zero  </li>
        </ul>
        You can use a conditional statement to check the denominator isn't zero before performing the division. 
        <p></p>
        </span>
    """ + final))

    else:
        ename = repr(etype).split("'")[1]
        display(HTML(f"""
        <hr>
        <h2> <span style="color:Midnightblue"> {course} help </span></h2>
        <span style="color:Midnightblue"> 
        <p></p>
        We have not implemented an explanation for '{ename}' error messages.  
        <p></p> 
        Try:
        <ul>
        <li> Looking at the python error documentation: <a href=https://docs.python.org/3/library/exceptions.html>https://docs.python.org/3/library/exceptions.html</a>  </li>
        <li> Googling the error (professional developers do this all the time!) </li>
        </ul>""" + final))

    log(etype, evalue)
        
    return

report = consent()
del consent

# this registers a custom exception handler for the whole current notebook
get_ipython().set_custom_exc((Exception,), custom_exc)
del custom_exc

