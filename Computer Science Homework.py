def product_one():
  print ("This is Product 1")

def product_two():
  print ("This is product 2")

def main():
  print ("Welcome to the shop!")
  choice = input("Enter 1 for Product 1 and 2 for Product 2)
  if choice == "1":
    product_one()
  elif choice == "2":
    product_two()
  else:
    print ("Invalid...")

  main()
