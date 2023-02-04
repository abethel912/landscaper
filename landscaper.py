# Game State

game = {"tool": 0, "money": 0}

tools = [
  {  "name": "Teeth","profit": 1,"cost": 0},
  {  "name": "Scissors","profit": 10,"cost": 5},
  {  "name": "Lawnmower","profit": 25,"cost": 25},
  {  "name": "Battery Lawnmower","profit": 100,"cost": 250},
  ]

##Game Option Function

def mow_lawn():
  tool = tools[game["tool"]]
  print(f"")