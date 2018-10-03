print("Greetings to internet citizens!")

Class Node:

    #constructor
    def_init_(self,data):
        self.data = data
        self.left=None
        self.right = None

#functions to compare dif objects 

     def __lt__(self, val):
        return self.val < val
    def __gt__(self, val):
        return self.val > val

     def __eq__(self, val):
        return self.val == val
     def __str__(self):
        return "[Node val: %d]" % self.val
