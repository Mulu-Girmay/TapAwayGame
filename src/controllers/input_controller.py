class InputController:
   def __init__(self, rotation_controller):
       self.rotation = rotation_controller

   def process(self, event):
       self.rotation.handle_event(event)
