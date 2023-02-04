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
      next_tool = tools[game['tool']+1]
      if (next_tool == None):
        print("There is no more tools")
        return 0
      if(game["money"]< next_tool['cost']):
        print("Not enough to buy tool")
        return 0
      game['money'] -= next_tool['cost']
      game['tool'] += 1