# PieOMatic
## what
Pie-O-Matic

## why
python code generation and scaffolding util

## how
1. configure config.json

    "editor_path":"C:\\PATH\\TO\\NOTEPAD.EXE"  <- put your editor_path path here
    
    "output_file_path":"C:\\PATH\\TO\\OutputFile.txt"   <- put your output_file_path path here

2. configure snippets

    use snippets.txt to configure custom templates
    
    templates are %% delimited 
    models are key value replacements using $0 $1
    
3. run main.py
 
#1.1 release notes
compiles df column lists into models 
more compilers to come
df.columns

Index(['Age', 'Income','Job', 'Degree', 'Major'],
      dtype='object')
      
      

