class Student(object):
  def __init__(self, name):
    self.name=name

  @property
  def score(self):
    return self._score

  @score.setter
  def score(self, value):
    if value > 100 : 
       raise ValueError('Your score is wrong')
    self._score= value

class Fib(object):
  def __init__(self,max=0):
    self.max = max

  def __iter__(self):
    self.a = 0
    self.b = 1
    self.n = 0
    print (self.a) 
    return self

  def __next__(self):
    if self.n <= self.max:
      self.a,self.b = self.b, self.a+self.b
      self.n +=1
      return self.a
    else:
      raise StopIteration

class Fib2(object):
  def __init__(self,max=0):
    self.max = max

  a = 0 
  b = 1 
  n = 0
  
  def __iter__(self):
    print(a)
    return self

  def __next__(self):
    if n < self.max:
      a , b = b , a + b
      return n 
    else: 
      return StopIteration
for i in Fib2(16):
   print(i) 

