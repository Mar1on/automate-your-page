# Generate HTML codes using list of project title and description
# uses <ul> HTML element

# Use variables to assign 3 titles
project2_programIntro = 'Introduction to Serious Programming'
project2_variables = 'Variables and Strings'
project2_functions = 'Functions'

# Use variables to assign list of description for each title
# Introduction to Serious Programming
program01 = 'Programming is the core of computer science.'
program02 = 'Most machines do one thing or are limited to what it’s designed to do.'
program03 = '''Computers without a program can’t do anything.
The power of computers is that it can do anything that it’s programmed to do. 
It uses a precise sequence of steps that can be executed super fast.
'''
program04 = 'Programs tell the computer what steps to take.'
program05 = '''Python is one example of a programming language.  It has specific grammar.
Codes must use correct grammar so that the interpreter can process it.'''
program06 = 'Python expression is a statement that does something ( i.e. calculate sum of 2 numbers, assign a value).'

# Variables and Strings
variable01 = 'Variables are names used to hold values.'
variable02 = 'Values are assigned to variables by using an assignment statement.'
variable03 = '''The equal “=” symbol is used in the assignment statement to assign
value to a variable, i.e. my_variable = 10 means my_variable is given the value of 10. 
This is different from the equation 2 + 3 = 5 which means 2 + 3 is the same as 5.'''
variable04 = '''Variables make the program easier to understand by using names that
describes the value. It stores value of important data and gives us the ability to
reuse and/or modify its content.'''
variable05 = 'Using variables allows us to assign different values in an expression to compute different things.'
variable06 = '''Strings are sequence of characters surrounded by quotes.
The + symbol in strings means concatenation. As an example: “2” + “2” will give us “22”
since the values are surrounded by quotes and 2 + 2 will give us 4 since the values are
treated as numbers (no quotes).'''

# Functions
function01 = """A function is something that accomplishes a specific task. 
Functions usually "take in" data, process it, and "return" a result. 
Once a function is written, it can be used over and over and over again."""
function02 = """Functions are created by using the keyword “def” plus the function name
followed by the parameters in parentheses.
The parameters will be replaced by values when the function is used. """
function03 = 'The body of the function contains the actual codes or instructions that specify what to do with the input parameters.'
function04 = 'A “return” statement is used to produce an output.'
function05 = 'Functions are used by writing the name of the function followed by the value(s) in parentheses, i.e. print add_numbers(5,3)'
function06 = 'Functions can be "called" from the inside of other functions.'

# include sample to go with def keyword description
function_defSample = """
            <div class='example'>def add_numbers(a, b): <br>
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;result = a + b<br>
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return result
            </div>""" 
        
# create lists for each note section
program_intro_list = [program01, program02, program03, program04, program05, program06]
variables_list = [variable01, variable02, variable03, variable04, variable05, variable06]
functions_list = [function01, function02, function03, function04, function05, function06]

# merge titles and description lists into 1 list
project_notes_list = [ [project2_programIntro, program_intro_list],
                       [project2_variables, variables_list],
                       [project2_functions, functions_list] ]

def generate_project_notes_HTML(note_title, desc_list):
    html_text_1 = '''
<h1>''' + note_title + '''</h1>'''
    html_text_2 = '''
<div class="main">
    <ul>''' + get_list_item(desc_list)
    html_text_3 = '''
    </ul>
</div>'''
    
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

def make_HTML(project_notes):
    note_title = project_notes[0]
    note_description_list = project_notes[1]
    return generate_project_notes_HTML(note_title, note_description_list)

# enclose each description in <li> </li>
# include function_defSample variable if defSample is > 0 
def generate_list(listDesc, defSample):
    display_defSample = ""
    if defSample > 0:
        display_defSample = "<br>" + function_defSample
    li_text = '''
        <li>
            ''' + listDesc + display_defSample + '''
        </li>'''
    return li_text

def get_list_item(listItem):
    item_desc  = ""
    # identify which item uses the function_defSample variable
    find_def_keyword = 'keyword “def” plus'
    for item in listItem:
        find_text = item.find(find_def_keyword)
        item_desc = item_desc + generate_list(item, find_text)
    return item_desc


def make_HTML_for_notes_list(list_project_notes):
    HTML = ""
    for project_notes in list_project_notes:
        concept_HTML = make_HTML(project_notes)
        HTML = HTML + concept_HTML
    return HTML

print make_HTML_for_notes_list(project_notes_list)











