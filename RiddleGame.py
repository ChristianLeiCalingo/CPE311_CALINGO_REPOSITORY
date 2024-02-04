class Sides:
  def __init__(self):
    self.leftside = ["Wolf", "Sheep", "Cabbage", "Jack"]
    self.rightside = []

class Eating:
    
    def __init__(self, place):
      self.life = 1
      self.leftside = place.leftside
      self.rightside = place.rightside
      
    def eating(self):
          self.check_status(self.leftside)
          self.check_status(self.rightside)
          
    def check_status(self, side):
        if "Wolf" in side and "Sheep" in side and "Jack" not in side:
            print("The Sheep was Eaten")
            self.life -= 1
        elif "Wolf" in side and "Sheep" in side and "Jack" in side:
            pass
        if "Cabbage" in side and "Sheep" in side and "Jack" not in side:
            print("The Cabbage was Eaten")
            self.life -= 1
        elif "Cabbage" in side and "Sheep" in side and "Jack" in side:
            pass
          
    def switchside_left(self, char):
        self.leftside.remove(char)
        self.leftside.remove("Jack")
        self.rightside.append("Jack")
        self.rightside.append(char)
        
    def switchside_right(self, char):
        self.rightside.remove(char)
        self.rightside.remove("Jack")
        self.leftside.append("Jack")
        self.leftside.append(char)
        
    def print_sides(self):
        print("-> On the rightside: ", ', '.join(map(str, self.rightside)))
        print("-> On the leftside: ", ', '.join(map(str, self.leftside)))
        
class Prompt:
    def __init__(self, eat, left, right, switch_left, switch_right):
        print("Jack has to transport Wolf, Cabbage, and Sheep, He can only carry one passenger per trip")
        answer = input("Who is coming with Jack?\n-> ")
        while answer not in left:
          print("No such thing")
          answer = input("Who is coming with Jack?\n-> ")
        switch_left(answer)
        eat.eating()
        if eat.life == 0:
          print("Oh no")
        else:
          print("------------------")
          print("Jack reached the right side with the", answer)
          eat.print_sides()
          print("------------------")
          print("After transporting the " + answer + ", Jack goes back to the left side")
          right.remove("Jack")
          left.append("Jack")
          eat.print_sides()
          print("------------------")
          answer2 = input("Jack is going back to the right side, who is coming with Jack?\n-> ")
          while answer2 not in left:
            print("No such thing")
            answer2 = input("Who is coming with Jack?\n-> ")
          print("------------------")
          print("Jack reached the right side with the", answer2)
          switch_left(answer2)
          eat.print_sides()
          print("------------------")
          print("Enter None if no one")
          answer3 = input("Jack is going back to the left side, who is coming with Jack?\n-> ")
          if answer3 == "None":
            right.remove("Jack")
            left.append("Jack")
            print("Oh no")
            eat.eating()
          else:
            switch_right(answer3)
            eat.eating()
            print("------------------")
            print("Jack reached the left side with the ", answer2)
            eat.print_sides()
            print("------------------")
            print("Enter None if no one")
            answer4 = input("Jack is going back to the right side, who is coming with Jack?\n-> ")
            if answer4 == "None":
              left.remove("Jack")
              right.append("Jack")
              print("Oh no")
              eat.eating()
            else:
              switch_left(answer4)
              eat.eating()
              eat.print_sides()
              print("------------------")
              print("Since the Wolf won't  eat the cabbage, Jack decides to go alone in the left side")
              print("------------------")
              print("Jack reached the left side with no one")
              right.remove("Jack")
              left.append("Jack")
              eat.print_sides()
              print("------------------")
              answer5 = input("Jack is going back to the right side, who is coming with Jack? ")
              while answer5 not in left:
                print("No such thing")
                answer5 = input("Who is coming with Jack? ")
              switch_left(answer5)
              eat.eating()
              print("------------------")
              print("Jack reached the right side with the ", answer5)
              eat.print_sides()
              print("------------------")
              if len(right) == 4:
                print("Jack Have Successfully transported all of them")
            
side = Sides()
eat = Eating(place=side)
left = eat.leftside
right = eat.rightside
switch_left = eat.switchside_left
switch_right = eat.switchside_right

Pr = Prompt(eat, left, right, switch_left, switch_right)