class tree:
    def __init__(node,nodenum):
        node.data = nodenum
        node.left = None
        node.right = None
        
def minVal(node):
    current = node
    while current.left != None:
        current = current.left
    return current

def insert(root,value):
    if root is None:
        return tree(value)
    
    if value < root.data:
        root.left = insert(root.left,value)
    
    elif value > root.data:
        root.right = insert(root.right,value)

    return root

def search(root,target_value,depth):
    if root.data == target_value:
        return depth
    else:
        if target_value < root.data:
            depth += 1
            return search(root.left,target_value,depth)
        else:
            depth += 1
            return search(root.right,target_value,depth)
    

def delete(root,target_value):
    if root == None:
        return root
    if target_value < root.data:
        root.left = delete(root.left,target_value)
    elif target_value > root.data:
        root.right = delete(root.right,target_value) 
    else:
        if root.left == None:
            return root.right
        elif root.right == None:
            return root.left
        root.data = minVal(root.right).data
        root.right = delete(root.right,root.data)
    return root

def operation(root,flag):
    while flag:
      print("What operation do you select?")
      print("1 is insert")
      print("2 is search")
      print("3 is delete")
      print("4 is end")
      try:
          user_input = int(input("input word or number "))
          if user_input not in [1,2,3,4]:
              raise ValueError("Input must be 1, 2, 3 or 4")
      except ValueError as e1:
          print(f"Error: {e1}")
          print("input the number 1 , 2 , 3 or 4")
      
      if user_input == 1:
          input_value = float(input("input insert value"))
          insert(root,input_value)
      
      elif user_input == 2:
          input_value = float(input("input searching \ value"))
          search(root,input_value,1)

      elif user_input == 3:
          input_value = float(input("input insert value"))
          search(root,input_value)
          
      elif user_input == 4:
          flag = 0
      
if __name__ == "__main__":
    root = None
    operation(root,1)

