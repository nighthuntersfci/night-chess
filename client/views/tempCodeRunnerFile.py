def set_username(self):
		socket_service.set_username(self.name.get())
		data.name = self.name.get()

		Rooms(self.parent)
		self.destroy()