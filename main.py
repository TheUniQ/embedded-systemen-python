import Model
import View
import Controller
import settings

Model.init()

Controller.init()

Controller.refresh(settings.com_list[0], settings.com_list[0].info)