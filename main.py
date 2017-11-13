import Model
import View
import Controller
import settings

Model.init()

Controller.init()

if (len(settings.com_list) == 0):
    Controller.startscreen()
else:
    Controller.refresh(settings.com_list[0], settings.com_list[0].info)
