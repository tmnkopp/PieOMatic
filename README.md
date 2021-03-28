![alt text](https://the80port.com/cdn/logos/som75-1.png "pom") 
# PieOMatic

POM: A [Sledge-O-Matic](https://github.com/tmnkopp/sledgeomatic) for Python.


## CONFIG
1. configure config.json

    "editor_path":"C:\\PATH\\TO\\NOTEPAD.EXE"  <- put your editor_path path here
    
    "output_file_path":"C:\\PATH\\TO\\OutputFile.txt"   <- put your output_file_path path here

2. configure snippets

    use `snippets.txt` to configure custom templates
    
    templates are `%% delimited`
    models are key value replacements using $0 $1
    
3. run main.py
 
## 1.3 release notes
Compiles DataFrame column lists into models   

Index(['Age', 'Income','Job', 'Degree', 'Major'],
      dtype='object')
      
      

