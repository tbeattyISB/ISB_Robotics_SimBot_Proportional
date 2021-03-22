from IdealBot import MainRun

def go(bot):
    bot.wait(2000)  # Wait 2 seconds before starting
    while(bot.ultrasonic_sensor() > 450): #Edit this so that it stops at 300
      bot.run(50)   # TRY EDITING THIS POWER (from -100 to 100)
    bot.run(0)      # When sensor reading of 300 reached stop!

MainRun(go)


# Answer below (as comment):
