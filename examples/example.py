import toml

from calc_tester import Test
from pydantic import ValidationError

with open('example.toml') as f:
  data = toml.load(f)
  try:
    print(Test.model_validate(data))
  except (TypeError, ValidationError) as err:
    print(err)