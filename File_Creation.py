def create_blank_files(filenames):
    for filename in filenames:
        with open(filename, "w") as f:
            pass
filenames = [
            "1.Introduction.py","2.BasicSyntaxandDataTypes.py",
            "3.VariablesandScope.py", "4.InputandOutput.py", 
            "5.BasicOperators.py", "6.ControlFlowStatements.py", 
            "7.Loops.py", "8.FunctionsandScope.py",
            "9.ModulesandPackages","10.ErrorandExceptionHandling.py", 
            "11.BasicDataStructures.py"
            ]
create_blank_files(filenames)
