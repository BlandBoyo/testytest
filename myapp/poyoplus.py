import fire

def hello(name="World"):
  return "Hello %s! you dumb boyo" % name

if __name__ == '__main__':
  fire.Fire(hello)
