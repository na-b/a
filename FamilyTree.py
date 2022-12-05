from collections import defaultdict
class Solution:

   def __init__(self, head_name):
      self.family = defaultdict(list)
      self.head = head_name
      self.dead = set()

   def birth(self, p_name, c_name):
      self.family[p_name].append(c_name)

   def death(self, name):
      self.dead.add(name)

   def inheritance(self):
      self.ans = []
      self.depth_search(self.head)
      return self.ans

   def depth_search(self, current):
      if current not in self.dead:
         self.ans.append(current)
      for child in self.family[current]:
         self.depth_search(child)

ob = Solution('Bharani')
ob.birth('Bharani', 'Narasimha')
ob.birth('Bharani', 'Vamsi')
ob.birth('Vamsi', 'Bose')
ob.birth('Vamsi', 'Madesh')
ob.birth('Vamsi', 'Nagarjuna')
ob.death('Bharani')
print(ob.inheritance())
ob.death('Narasimha')
print(ob.inheritance())

"""

OUTPUT
------
['Narasimha', 'Vamsi', 'Bose', 'Madesh', 'Nagarjuna']
['Vamsi', 'Bose', 'Madesh', 'Nagarjuna']

"""