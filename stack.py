class Stack:
   def __init__(self):
      self.content = []
    
   def push(self, x: int) -> None:
      self.content.append(x)
         
   def pop(self) -> int:
      answer = self.content[-1]
      self.content = self.content[:-1:]
      return answer
   
