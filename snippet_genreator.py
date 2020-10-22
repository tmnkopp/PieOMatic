import subprocess 
from compiler import ColumnCompiler 
from context import ConfigProvider

class SnippetGenerator:
    
    def __init__(self, context):
        self._ctx = context
       
    def Generate(self):  
        with open(self._ctx.output_file_path, 'w') as file: 
            file.write('paste colums here') 
        subprocess.call([self._ctx.editor_path, self._ctx.output_file_path]) 
        txt = ColumnCompiler(self._ctx).Compile() 
        if self._ctx.editor_path.strip() != '': 
            with open(self._ctx.output_file_path, 'w') as file: 
                file.write(txt) 
            subprocess.call([self._ctx.editor_path, self._ctx.output_file_path])  
            
 
 # _ctx = ConfigProvider()  
 # from snippet_genreator import ConfigProvider           