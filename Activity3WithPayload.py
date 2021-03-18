from Robot import MainRun

def go(bot):
    bot.setPayload(20)
    bot.wait(2000)  # Wait 2 seconds before starting
    bot.run(50)     # Power the motors to 50%
    bot.wait(1000)  # CHANGE THIS TIME TO STOP 300 pixels from the wall
    bot.run(0)      # Stop Robot

MainRun(go)

# How does adding and removing a payload affect the robots behavior?
# Answer below (as comment):