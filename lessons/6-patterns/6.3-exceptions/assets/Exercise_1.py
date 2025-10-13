# Create a try/except that will run successfully
try:
  # Add something that will run successfully
  
except:
  print("try/except 1 produced an error")


  
  # Create a try/except that will fail to run
try:
  # Add something that will not run successfully
  
except:
  print("try/except 2 produced an error")



# The whole program should still complete, despite an error occurring above
print("program did not abort")