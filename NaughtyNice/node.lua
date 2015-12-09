gl.setup(1024, 768)

local font = resource.load_font("/home/pi/.fonts/Carrington.ttf")

function node.render()
    font:write(150, 320, "Hello World", 100, 1,1,1,1)
end
