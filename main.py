import random
cards = 8

choose = []

# не повторяться

wc = ['hog_rider', 'ram_rider','royal_hogs', 'rune_giant', 'e-giant', 'skeleton-giant', 'giant', 'royal_giant', 'goblin_giant', 'goblinstein', 
      'skeleton_barrel', 'goblin_barrel', 'lava_hound', 'baloon', 'X-bow', 'mortar', 'golem', 'elixir_golem', 'megaknight', 'PEKKA', 'wall_breakers', 
      'battle_ram', 'goblin_drill', 'inferno_dragon', 'princess', 'mini_PEKKA', 'elite_barbarians', 'recruits', 'sus_bush']

ad = []



lists = [wc, ad, splash, tank, lsp, hsp, building, trash]
for i in lists:
    choose.append(random.choice(i))


print(choose)
