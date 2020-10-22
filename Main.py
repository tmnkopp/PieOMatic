import subprocess 
from compiler import ColumnCompiler 
from context import ConfigProvider
_ctx = ConfigProvider()  
with open(_ctx.output_file_path, 'w') as file: 
    file.write('paste colums here') 
subprocess.call([_ctx.editor_path, _ctx.output_file_path]) 
txt = ColumnCompiler(_ctx).Compile() 
if _ctx.editor_path.strip() != '': 
    with open(_ctx.output_file_path, 'w') as file: 
        file.write(txt) 
    subprocess.call([_ctx.editor_path, _ctx.output_file_path])  
 

 
 