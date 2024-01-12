#!/usr/bin/env python3

import ipdb

class MyString:

  def __init__(self, value=""):

    self.value = value
  
  @property
  def value(self):
    return self._value

  @value.setter
  def value(self, value):

    if (isinstance(value, str)):
      self._value = value
      
    else:
      print("The value must be a string.")
  
  def is_sentence(self):

    if (self.value[-1] == '.'):
      return True

    else:
      return False

  def is_question(self):

    if (self.value[-1] == '?'):
      return True

    else:
      return False
  
  def is_exclamation(self):

    if (self.value[-1] == '!'):
      return True

    else:
      return False
  
  def count_sentences(self):

    str_in_list = self.value.split()
    counter = 0

    for word in str_in_list:
      if (word[-1] == "." or word[-1] == "!" or word[-1] == "?"):
        counter += 1

    return counter