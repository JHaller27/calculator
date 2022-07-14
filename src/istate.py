class IState:
	def handle_digit(self, digit: int) -> 'IState':
		raise NotImplementedError

	def handle_operator(self, op: str) -> 'IState':
		raise NotImplementedError

	def get_display(self) -> str:
		raise NotImplementedError
