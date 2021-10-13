import unittest

PLEDGE = "I pledge my honor I have abided by the Stevens Honor System."

# The Errors (Exceptions) below outline what is checked by this script. This script
# does NOT edit your file to fix your mistakes, this just validates the file that 
# you have given it.

class IncorrectFileExtensionError(Exception):
    """Raised when the file provided does not have a .py file extension."""
    pass

class TestScriptNotFound(Exception):
    """Raised when the test script could not be found."""
    pass

def autograde(file_name: str, student_name: str, test_script: str = None) -> bool:
    """
    file_name: str               = the name of the file to check.
    student_name: str            = the name of the student to check for in the file.
    test_script: str  (optional) = the name of the test script to run with the file. MUST USE the `unittest` module, 
                                   and the name of the test functions must start with test
    """
    didPass = []

    if file_name.split(".")[-1] != "py":
        raise IncorrectFileExtensionError
    else:
        didPass.append(True)
    
    file = open(file_name, "r")
    contents = file.read()
    file.close()

    if PLEDGE in contents:
        print("PLEDGE...........OK")
        didPass.append(True)
    else:
        print("PLEDGE...........NO")
    
    if student_name in contents:
        print("NAME.............OK")
        didPass.append(True)
    else:
        print("NAME.............NO")
    
    lines = contents.strip().split("\n")

    func_count = 0
    docscring_count = 0
    functions_missing_docstrings = []

    previous_line_contains_def = False
    previous_function = ""
    for line in lines:

        if "def" in line:
            previous_line_contains_def = True
            previous_function = line
            func_count += 1
        elif line != "":
            if previous_line_contains_def and ("\"\"\"" in line or "\'\'\'" in line):
                docscring_count += 1
                didPass.append(True)
            elif previous_function != "":
                functions_missing_docstrings.append(previous_function.split(" ")[1].split("(")[0])

        previous_function = ""
        previous_line_contains_def = False
    
    cleaned_missing = [func for func in functions_missing_docstrings if func != ""]

    if len(cleaned_missing) == 0:
        print("DOCSTR...........OK")
    else:
        for func in cleaned_missing:
            print("MISSING DOCSTR..."+func)

    if test_script != None:
        try:
            test_module = __import__(test_script.split(".")[0])
        except ImportError:
            raise TestScriptNotFound

        tests = [method for method in dir(test_module.Test) if method.startswith('_') == False and method.startswith("test") == True]

        for test in tests:
            didPass.append(unittest.TextTestRunner().run(test_module.Test(test)).wasSuccessful())
    else:
        print("No test script was provided. This is ok if there is no provided test script, but I urge you to write your own tests to ensure that your code works.")
        print("NOTE: Test scripts that you write will not work in this script unless the test script uses the `unittest` module and the test class is named `Test`.")   

    passed = all(didPass)

    if passed:
        print("PASS.............OK")

    return passed