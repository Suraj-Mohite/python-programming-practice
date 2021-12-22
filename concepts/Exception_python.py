no=int(input("Enter the number.\n"))
no2=int(input("Enter the number.\n"))

try:
    if no==5:
        raise ValueError("invalid")
    #print(no/no2)
except ValueError:    #except Exception as e:
    raise
finally:
    print("\nThank You\n")
"""except Exception:    #except Exception as e:
    raise Exception("Error hhhhh")"""
"""      """