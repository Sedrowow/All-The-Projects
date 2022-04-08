entities = {}

function newposition(x,y,w,h)
	local p = {}
	p.x = x
	p.y = y
	p.w = w
	p.h = h
	
	return p
end

function newsprite(x,y)
	local s = {}
	s.x = x
	s.y = y
	return s
end

function newentity(position,sprite)
	local e = {}
	e.position = position
	e.sprite = sprite
	add(entities,e)
	return e
end

gs = {}
gs.update = function()
	cls()
	--centre camera on player
 camera(-64+player.position.x+(player.position.w/2),
		-64+player.position.y+(player.position.h/2))
 map()
	
	--draw all entities with sprites
	
	for ent in all(entities) do
		if ent.sprite ~= nil and ent.position ~= nil then
			
		sspr(player.sprite.x,
			 player.sprite.y,
		     player.position.w,
		     player.position.h,
		     player.position.x,
		     player.position.y)
		end
	end
	camera()
end

function _init()
	player = newentity{
		newposition(10,10,8,8),
		newsprite(8,0)
	}
end


function _update()
 --check player movement
	if btn(0) then player.position.x-=1 end
	if btn(1) then player.position.x+=1 end
	if btn(2) then player.position.y-=1 end
	if btn(3) then player.position.y+=1 end
end


function _draw()
gs.update()
end