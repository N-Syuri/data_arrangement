class TreeNode:
    def __init__(self, nodenum):
        self.data = nodenum
        self.left = None
        self.right = None

def min_val(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def insert(root, value):
    if root is None:
        return TreeNode(value)

    if value < root.data:
        root.left = insert(root.left, value)
    elif value > root.data:
        root.right = insert(root.right, value)

    return root

def search(root, target_value, depth):
    if root is None:
        print(f"{target_value}はツリー内に見つかりませんでした")
        return -1
    
    if root.data == target_value:
        print(f"{target_value}を深さ{depth}で見つけました")
        return depth
    elif target_value < root.data:
        return search(root.left, target_value, depth + 1)
    elif target_value > root.data:
        return search(root.right, target_value, depth + 1)

def operation(root, flag):
    while flag:
        print("What operation do you select?")
        print("1 is insert")
        print("2 is search")
        print("3 is delete")
        print("4 is end")
        try:
            user_input = int(input("Input a number (1, 2, 3, or 4): "))
            if user_input not in [1, 2, 3, 4]:
                raise ValueError("Input must be 1, 2, 3, or 4")
        except ValueError as e1:
            print(f"Error: {e1}")
            print("Input must be the number 1, 2, 3, or 4")

        if user_input == 1:
            input_value = float(input("Input insert value: "))
            root = insert(root, input_value)

        elif user_input == 2:
            input_value = float(input("Input searching value: "))
            search_depth = search(root, input_value, 1)
            if search_depth != -1:
                print(f"Depth of {input_value}: {search_depth}")

        elif user_input == 3:
            input_value = float(input("Input delete value: "))
            # ここでノードの削除処理を実装する必要があります

        elif user_input == 4:
            flag = 0

if __name__ == "__main__":
    root = None
    operation(root, 1)
