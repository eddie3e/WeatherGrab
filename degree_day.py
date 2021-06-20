## class to define degree day object. can take data to return object
## show count of days from date if possible, from historical table

class degree_day(object):

    def _init_(self):
        self.par = 50


    def convert_temp(self, data):
        gdd = (data.high + data.low)/2 - self.par

## print in table format.

## High and Low temp with GDD and count


        
## Try input of zip code to retrieve data    
    
