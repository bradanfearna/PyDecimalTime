from kivy.app import App
from kivy.uix.button import Button
from datetime import datetime
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.label import Label
    
def getDecimalTimeMicro():
    n = datetime.now()
    st = float(n.hour*60*60 +  n.minute*60 + n.second + float(float(n.microsecond) / 1000000.0)) / float(24*60*60)
    dats = str(st*100000000)
    return (int(dats[0:1]),int(dats[1:3]),int(dats[3:5]) )
    
class DecimalClock(App):
    
    def nextTip(self,label):
        sf = "%dh:%02dm:%02ds" %getDecimalTimeMicro()  
        label.text=sf
        return label

    def build(self):
        l = Label( markup=True,font_size='60sp')
        #Clock.schedule_once(lambda dt: self.nextTip(l),3)
        Clock.schedule_interval(lambda dt: self.nextTip(l),0.01)
        return l

if __name__=="__main__":        
    Window.size = (400, 200)        
    DecimalClock().run()