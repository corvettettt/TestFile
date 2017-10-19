class Student(object):
   def get_score(self):
      return self._score

   def set_score(self, value):
      if not isinstance(self, value):
	 raise ValueError('score much')
      if value <0 or value > 100:
	 raise ValueError('')
