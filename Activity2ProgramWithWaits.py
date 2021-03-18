from Robot import MainRun

def go(bot):
    bot.wait(2000)  # Wait 2 seconds before starting
    bot.run(50)     # Power the motors to 50%
    bot.wait(1000)  # CHANGE THIS TIME TO STOP 300 pixels from the wall
    bot.run(0)      # Stop Robot

MainRun(go)


# What real world variables influence the robots ability to run in an "ideal" way.
# Answer below (as comment):