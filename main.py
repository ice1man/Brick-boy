import brick
import rps
import remote
import counter

brick.display_text.putstr("welcome to the")
brick.display_text.move_to(0,1)
brick.display_text.putstr("brick boi")

brick.display_text.clear()
item = brick.pick(["rps","ir"])
if item == 0:
  rps.main()
elif item == 1:
  remote.main()
elif item == 2:
  counter.main()
