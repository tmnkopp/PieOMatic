from IPython.display import display, HTML
class Convert:  
    def __init__(self):
        self.name=''
    def to_percent(self, num1, num2):  
        return round((num1/num2)*100,2)
    def to_percentf(self, num1, num2):  
        return '{0:.0f}%'.format(self.to_percent( num1, num2))
    def to_des(self):  
        return HTML('<img src="https://ca.slack-edge.com/T01ADCEKEDR-U01BFB7LFC0-8334c324cf2c-512" />' )   
       


    
    
    