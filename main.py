import brick
import rps

brick.display_text.putstr("welcome to the")
brick.display_text.move_to(0,1)
brick.display_text.putstr("brick boi")

brick.display_text.clear()
item = brick.pick(["rps"])
if item == 0:
  rps.main()
