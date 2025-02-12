"""Example of a submodule"""

def example_function(x: int, y: int, print_flag: bool =True):
  """
  This example function is here to give a template for docstrings. These are numpy-style docstrings.
  
  Parameters
  ----------
  x : int
      The first parameter.
  y : int
      The second parameter.
  print_flag: bool, optional, default True
      Flag, prints result of summation if True.

  Returns
  -------
  int
      the sum of x and y
  """
  result = x + y
  if print_flag:
    print(result)
    
  return result
