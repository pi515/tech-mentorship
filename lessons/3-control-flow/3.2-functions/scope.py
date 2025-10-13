my_txt = "example text"  # global variable


def func_local():
  my_txt = "some text"  # local variable
  print("local:", my_txt)


def func_global_0():
  global my_txt  # reference global variable
  print("global 0:", my_txt)


def func_global_1():
  global my_txt
  my_txt = "other text"  # reference and update the global variable
  print("global 1:", my_txt)


def func_global_2():
  global my_txt_2  # define a global variable anywhere
  my_txt_2 = "last text"


if __name__ == "__main__":

  print("outside:", my_txt)

  func_local()

  print("outside:", my_txt)

  # print("outside:", my_txt)

  # func_global_0()

  func_global_1()

  print("outside:", my_txt)

  func_global_2()
  print(my_txt_2)  # what will happen?
