from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str
    description: str

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int
    completed: bool

    class Config:
        orm_mode = True
        
        
        
class TaskUpdate(BaseModel):
    title: str
    description: str
    completed: bool




#this validates incoming data
#then prevents bad requests
#and finally, converts db objects->JSON automatically