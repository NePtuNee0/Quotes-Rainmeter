function Initialize()
end

function Update()
    local path = SKIN:GetVariable('CURRENTPATH') .. 'quote.txt'
    local file = io.open(path, 'r')
    if file then
        local content = file:read('*all')
        file:close()
        SKIN:Bang('!SetOption', 'MeterQuote', 'Text', content)
        SKIN:Bang('!UpdateMeter', 'MeterQuote')
        SKIN:Bang('!Redraw')
    end
end