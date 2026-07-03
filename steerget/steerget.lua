-- Runs once when the application initializes

local fullLock = nil
local OUTPUT_FILE = "apps/lua/steerget/steerlock.txt"

function script.update(dt)
    local car = ac.getCar(0)

    if not car then return end

    local newFullLock = car.steerLock * 2

    if newFullLock ~= fullLock then
        fullLock = newFullLock

        local ioSucc = io.save(OUTPUT_FILE, tostring(fullLock))
            ac.log("io.save returned: " .. tostring(ioSucc))
            ac.log("Saved steer lock: " .. tostring(fullLock))
        
    end
end

function script.windowMain()

    ui.text("Debugging screen for Steering Bar. Not neccessary to leave on-screen :)")
    ui.text("Current full steer lock: "..tostring(fullLock))
    ui.text("steerlock.txt exists: "..tostring(io.fileExists(OUTPUT_FILE)))

end
