class Codec:

    def serialize(self, root):
        def rserialize(root, string):
            if root is None:
                string += "None,"
            else:
                string += str(root.val) + ","
                string = rserialize(root.left, string)
                string = rserialize(root.right, string)
            return string
        
        return rserialize(root, "")
    
    def deserialize(self, data):
        def rdeserialize(data_list):
            if data_list[0] == "None":
                data_list.pop(0)
                return None
            
            root = TreeNode(int(data_list[0]))
            data_list.pop(0)
            root.left = rdeserialize(data_list)
            root.right = rdeserialize(data_list)
            return root 
        
        data_list = data.split(",") #这一行代码的作用是将输入的字符串 data 按照逗号 , 进行 拆分，并将拆分后的结果存储在一个列表 data_list 中
        return rdeserialize(data_list)
