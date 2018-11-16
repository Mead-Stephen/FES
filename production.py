##This snipped of code will define production of goods
## r2 and r3 simulate local weather/effects on crops
## version 2 goal is to add climate effects based on temp/precip

class prod:
	def __init__(self):
        
## Farm production is a function (farmers * sum(randoms)) + tile_modifier + team modifier.
## Volume of farmers is limited by the tile max.  
## global modifier is determined at the beginning of spring
## grain and produce are both for population consumption
    def __farm__(self, global_farm_modifier,tile, tile_modifier, team_modifier, tile_max):
        r2 = ra.randrange(0,6,1)  
        r3 = ra.randrange(0,6,1)
        if tile['grain_farmers'] + tile['produce_farmers'] <= tile_max:
            tile['grain_prod'] = ((tile['grain_farmers'] * .25)*(global_rand + r2 + r3)) + team_modifier + tile_modifier['grain']
            tile['produce_prod'] = ((tile['produce_farmers'] * .0625)*(global_rand + r2 + r3)) + team_modifier + tile_modifier['produce']
        else tile['grain_prod'] = (((tile['grain_farmers']/tile_max) * .25)*(global_rand + r2 + r3)) + team_modifier['grain'] + tile_modifier['produce']
            tile['produce_store'] = ((tile['produce_farmers'] * .0625)*(global_rand + r2 + r3)) + team_modifier['grain'] + tile_modifier['produce']
    return tile   
	
	
## Mine production
## Stone is used for construction of advanced buildings
## Iron is a catchall for useful unit needs
## Precious metal is a catchall for trade, sovereign relations, taxing needs (likely more for v2 and beyond)
	def __mine__(self, tile, tile_modifier, team_modifier, tile_max):
	    tile['stone_prod'] = tile['stone_miner'] * (tile_modifier['stone'] + team_modifier['stone_mine'])
		tile['iron_prod'] = tile['iron_miner'] * (tile_modifier['iron'] + team_modifier['iron'])
		tile['silver'] = tile['silver_miner'] * (tile_modifier['silver'] + tile_modifier['silver'])
	return tile
	
## Wood Production
## Wood is used for construction of buildings + some unit types + population consumption
	def__wood__(self, tile, tile_modifier, team_modifier):
		tile['wood_prod'] = tile['logger'] * [tile_modifier['wood'] + team_modifier['wood']

## Livestock Production
## meat is for population consumption
## wool is for adv population consumption and some unit types
	def__livestock__(self, tile, tile_modifier,team_modifier):
		tile['meat_prod'] = tile['livestock'] * (team_modifier['meat'] + tile_modifier['livestock])
		tile_['wool_prod'] = tile['livestock'] * (team_modifier['wool'] + tile_modifier['livestock']
	return tile