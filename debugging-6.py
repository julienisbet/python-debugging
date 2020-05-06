# each of the calls to this function are broken
# fix them so they print out the information in the comment
# and follow the rules

def say_hello(first_name, last_name, middle_initial=""):
  if middle_initial != "":
    print(f"Hello {first_name} {middle_initial} {last_name}")
  else:
    print(f"Hello {first_name} {last_name}")
# 1.
# should print "Hello Julie M Nisbet"
#
say_hello("Julie", "Nisbet")

# 2.
# should print "Hello Julie M Nisbet"
# do not change the order of the arguments in this call
say_hello(last_name="Nisbet", "Julie", middle_initial="M")

# 3.
# should print "Hello Julie Nisbet"
# do not change the order of the arguments in this call
say_hello("Nisbet", "Julie")



