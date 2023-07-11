# # <a href="https://colab.research.google.com/github/pulkit8690/Mini-Project-Combo-Finder/blob/main/ComboFinder.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
#   ---
# # **ComboFinder**
# ---
# ####**Problem Statement:**
# # Find all the list of products whose sum-of-price is between 290 and 310.

# ProductList = {p1:10, p2:15, p3:20, p4:25, p5:30, p6:35, p7:50}

# ---
### **1 Library inclusion**
import random as r
### **2 Parameter Setting**
# Read the productId-price file and convert to dictionary
ProductList = {'p1':10, 'p2':15, 'p3':20, 'p4':25, 'p5':30, 'p6':35, 'p7':50,
               'p8':40, 'p9':55, 'p10':60, 'p11':65, 'p12':75, 'p13':70,
               'p14':45}
LB          = 290
UB          = 310
ResultList  = set()   # Store Result List i.e. list of sets whose sum is between 90 and 210.
Iterations  = 1000    # Number of Inerations
### **Single Run**



# Select combo size (i.e. number of products in a combo)
SetSize = r.randint(2, len(ProductList)-1)
print("Number of Product: ", SetSize)


# Select number of elements from Set
ComboList = r.sample(list(ProductList.keys()),SetSize)
print("Product List     : ", ComboList)


# Sum the products in ColboList
ComboSum = sum([ ProductList[i] for i in ComboList])
print("Sum of Product   : ", ComboSum)

### **3 Start Program**



# Loop till number of Iterations
ResultList  = set()

for i in range(Iterations):

    # Select combo size (i.e. number of products in a combo)
    SetSize = r.randint(2, len(ProductList)-1)

    # Select number of elements from Set
    ComboList = r.sample(list(ProductList.keys()),SetSize)

    # Sum the products in ColboList
    ComboSum = sum([ ProductList[i] for i in ComboList])
    
    # Check the Sum Between LB and UB
    if ComboSum>= LB and ComboSum<= UB:
      ResultList.add(tuple(ComboList))

print("Done")
### **4 Print the comboLists and total count**

# Print all the sets whose sum is between LB and UB
for r in ResultList:
	print (r)

# Print total sets
print ("\nTotal Sets: ", len(ResultList), "\n")

### **5 Complete Program with sorting**

#-------------------------------------------------------------
# Step 1: Library inclusion                             
#-------------------------------------------------------------
import random as r


#-------------------------------------------------------------
# Step 2: Parameter Setting
#-------------------------------------------------------------
ProductList = {'p1':10, 'p2':15, 'p3':20, 'p4':25, 'p5':30, 'p6':35, 'p7':50,
               'p8':40, 'p9':55, 'p10':60, 'p11':65, 'p12':75, 'p13':70,
               'p14':45}
LB          = 290
UB          = 310
ResultList  = set()   # Store Result List i.e. list of sets whose sum is between 90 and 210.
Iterations  = 1000    # Number of Inerations


#-------------------------------------------------------------
# Step3: Start Program
#-------------------------------------------------------------
for i in range(Iterations):

    # Select combo size (i.e. number of products in a combo)
    SetSize = r.randint(2, len(ProductList)-1)

    # Select number of elements from Set
    ComboList = r.sample(list(ProductList.keys()),SetSize)
    ComboList.sort()

    # Sum the products in ColboList
    ComboSum = sum([ ProductList[i] for i in ComboList])

    # Check the Sum Between LB and UB
    if ComboSum>= LB and ComboSum<= UB:
      ResultList.add(tuple(ComboList))


# Print all the sets whose sum is between LB and UB
for r in ResultList:
	print (r)

# Print total sets
print ("\nTotal Sets: ", len(ResultList), "\n")
