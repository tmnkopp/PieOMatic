from context import ConfigProvider   
print(  ']['.join(['foo','bar','qux'])) 
_ctx = ConfigProvider()
_snippet_genreator = SnipGen( _ctx )  
_snippet_genreator.Generate()

 