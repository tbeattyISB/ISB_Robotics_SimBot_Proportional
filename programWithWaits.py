from Robot import MainRun

def go(bot):
    bot.setPayload(0) # Up to 20 kg
    bot.wait(2000)  # Wait 2 seconds before starting
    bot.run(50)     # Power the motors to 50%
    bot.wait(1000)  # CHANGE THIS TIME TO STOP 300 pixels from the wall
    bot.run(0)      # Stop Robot

MainRun(go)