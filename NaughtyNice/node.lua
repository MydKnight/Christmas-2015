gl.setup(1024, 768)

local font = resource.load_font("Carrington.ttf")
background = resource.load_image("Parchment-42.jpg")

function node.render()
    background:draw(0,0, WIDTH, HEIGHT)
    font:write(150, 320, "Hello World", 100, 1,1,1,1)
end
