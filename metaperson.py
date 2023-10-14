from dataclasses import dataclass,Field
from datetime import datetime

#Field -> 'default', 'default_factory', 'init', 'repr', 'hash','compare','metadata','kw_only
params = {
    'firstname':Field(None,None,True,True,True,True,None,True),
    'lasttname':Field(None,None,True,True,True,True,None,True),
    'year_of_birth':Field(None,None,True,True,True,True,None,True)
}

def age(self):
    return datetime.now().year - self.year_of_birth

MetaPerson = dataclass(type('MetaPerson',(),{'__annotations__':params,'personage':property(age)}))

p = MetaPerson('Romualda','Tracz',1977)
print(p)
print(p.personage)
