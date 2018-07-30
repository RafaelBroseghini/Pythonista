'''
Author: Rafael Broseghini
Implementation of python like list built in
data type using the ctypes module.
'''
import sys
import ctypes

class DynamicArray(object):
    '''
    DYNAMIC ARRAY CLASS (Similar to Python List)
    '''

    def __init__(self):
        self.n = 0 # Count actual elements (Default is 0)
        self.capacity = 1 # Default Capacity
        self.A = self.make_array(self.capacity)

    def __len__(self):
        """
        Return number of elements sorted in array
        """
        return self.n

    def __getitem__(self,k):
        """
        Return element at index k
        """
        if not 0 <= k <self.n:
            return IndexError('K is out of bounds!')

        return self.A[k]

    def append(self, ele):
        """
        Add element to end of the array
        """
        if self.n == self.capacity:
            self._resize(2*self.capacity)

        self.A[self.n] = ele
        self.n += 1
    
    def pop(self, idx=sys.maxsize):
      """
      Pop element from end of array.
      """
      if self.n == (self.capacity // 4):
        self._resize(self.capacity//2)

      if idx == sys.maxsize:
        idx = self.n - 1
      elif idx < 0 or idx > (self.n-1):
        raise Exception("Index out of range!")
 
      val = self.A[idx]
      self.A[idx] = None

      # Shift items to the left.
      for i in range(idx+1, self.n):
        self.A[i],self.A[i-1] = self.A[i-1], self.A[i]

      self.n -= 1
      return val
    
    def insert(self, idx="", element=""):
      """
      Insert element at any index in array.
      Shifting elements to the right.
      """
      # Here we make use of append to take
      # care of checking capacity and increasing n.
      self.append(None)
      
      if idx == "":
        raise Exception("No index specified!")
      elif idx < 0 or idx > (self.n-1):
        raise Exception("Index out of range!")

      # Shift items to the right.
      for i in range(self.n, idx, -1):
        self.A[i] = self.A[i-1]

      self.A[idx] = element

    def _resize(self,new_cap):
        """
        Resize internal array to capacity new_cap
        """

        B = self.make_array(new_cap) # New bigger array

        for k in range(self.n): # Reference all existing values
            B[k] = self.A[k]

        self.A = B # Call A the new bigger array
        self.capacity = new_cap # Reset the capacity

    def make_array(self,new_cap):
        """
        Returns a new array with new_cap capacity
        """
        return (new_cap * ctypes.py_object)()
