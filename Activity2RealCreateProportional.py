from Robot import MainRun

# In this problem you will need too create a PROPORTIONAL CONTROLLER for your robot.
# Steps:  - Create a kp "gain constant" start at a value of 1, and a desired distance or 300
#         - Within a forever while loop, calculate error then adjust power according to the error*kp
#         - Adjust the KP until you think the robot responds well

def go(bot):
  bot.wait(2000)  # Wait 2 seconds before starting
  while (bot.ultrasonic_sensor() > 300):  # Edit this so that it stops at 300
    bot.run(50)  # TRY EDITING THIS POWER (from -100 to 100)
  bot.run(0)  # When sensor reading of 300 reached stop!

MainRun(go)


# How  does changing your kp (gain) affect:
#   1. speed,
#   2. overshoot and
#   3. stability
# Answer below (as comment):