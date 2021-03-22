from Robot import MainRun
# In this assignement you will use an ideal robot to move between three different positions, without sensors. You are limited to using:
#
# while(ultrasonic_sensor()??):..
#
# bot.wait(??) and
#
# bot.run(??) to move the robot to three different positions:
#
# You can tolerate with 10 pixels of these goals and don't need to match the desired graph exactly:
#
# Starting at 700,
# Move to 300,
# Move back to 500
# Move forward to 50

def go(bot):
    bot.wait(2000)  # Wait 2 seconds before starting
    while(bot.ultrasonic_sensor() > 300): #Edit this so that it stops at 300
      bot.run(50)   # TRY EDITING THIS POWER (from -100 to 100)
    bot.run(0)      # When sensor reading of 300 reached stop!

MainRun(go)


