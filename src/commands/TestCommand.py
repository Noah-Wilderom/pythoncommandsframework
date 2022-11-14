from src.lib.Command import Command

class TestCommand(Command):

	def __init__(self):
		super().__init__()

	def handle(self):
		self.testprint()