import brick

def main():
  doing = brick.pick(["transmit","receive"])
  if doing == 0:
    while True:
      device = brick.pick(["apple tv","infocus","nec","samsung"])
      if device == 0:
        action = brick.pick(["reboot","menu","play_pause","up","down","left","right","center"])
        if action == 0:
          
  elif doing == 1:
