# a=[{"id":1,"name":"nacho"},
#  {"id":100, "name":"cheese"},
#  {"id":3, "name":"cake"}]

# maxhand=0
# for i in a:
#     if i["id"]>maxhand:
#         maxhand=i["id"]
# print(maxhand)   

# from pydantic import BaseModel

class test:
    def __init__(self, id, name):
        self.id=id
        self.name=name
    def __str__(self):
        return f"id: {self.id}, name={self.name}"



t1= test(1, "sa")
print(t1)
    
  