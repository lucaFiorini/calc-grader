from dataclasses import dataclass
from typing import Callable

@dataclass
class TestDefinition:
  name : str
  weight : float
  
@dataclass
class Success:
  pass
@dataclass
class Fail:
  reason : str

type Result = Success|Fail

@dataclass
class TestCase[TestType : Callable[...,Result]]:
  definition : TestDefinition
  func : TestType

@dataclass
class ExecutedTest:
  definition : TestDefinition
  result : Result