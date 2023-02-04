# Game State

game = {"tool": 0, "money": 0}

tools = [
  {  "name": "Teeth","profit": 1,"cost": 0},
  {  "name": "Scissors","profit": 10,"cost": 5},
  {  "name": "Lawnmower","profit": 25,"cost": 25},
  {  "name": "Battery Lawnmower","profit": 100,"cost": 250},
  {  "name": "Students","profit": 250,"cost": 500},
  ]

##Game Option Function

def mow_lawn():
  tool = tools[game["tool"]]
  print(f"You can mow a lawn with your {tool['name']} and make {tool['profit']}")
  game['money'] += tool['profit']
  
def check_stats():
    tool = tools[game["tool"]]
    print(f"You currently have {game['money']} and are using a {tool['name']}")
    
def upgrade():
  if(game['tool'] >= len(tools) - 1):
    print("No more upgrades")
    return 0
  next_tool = tools[game['tool']+1]
  if (next_tool == None):
        print("There is no more tools")
        return 0
  if(game["money"]< next_tool['cost']):
        print("Not enough to buy tool")
        return 0
  print("You are upgrading your tool")    
  game['money'] -= next_tool['cost']
  game['tool'] += 1
      
def win_check():
        if(game['tool'] == 1 and game['money'] >= 1000):
          print("You win")
          return True
        return False
        
while (True):
  
    i = input("[1] Mow Lawn [2] Check Stats [3] Upgrade [4] Quit")
    
    i= int(i)
    
    if (i == 1):
      mow_lawn()
      
    if ( i == 2):
      check_stats()
          
    if(i== 3):
      upgrade()
            
    if (i == 4):
      print("you quit the game")
      break
    
    if(win_check()):
      break