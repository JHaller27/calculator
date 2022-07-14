from istate import IState
from calculator import Calculator


def coalesce(*args):
	for a in args:
		if a is not None:
			return a


class BaseState(IState):
	def __init__(self, ctx: Calculator):
		self._ctx = ctx

	@property
	def ctx(self) -> Calculator:
		return self._ctx

	def handle_digit(self, digit: int) -> IState:
		raise NotImplementedError

	def handle_operator(self, op: str) -> IState:
		raise NotImplementedError

	def get_display(self) -> str:
		raise NotImplementedError


class RefactorState(BaseState):
	def handle_digit(self, digit: int) -> IState:
		raise NotImplementedError

	def handle_operator(self, operation: str) -> IState:
		if operation == '=':
			self.ctx.result = self.ctx.get_result()
			self.ctx.prev_num = self.ctx.result
			return HasResultState(self.ctx)

		next_state = self

		if self.ctx.prev_num is None:
			self.ctx.prev_num = self.ctx.curr_num

		elif self.ctx.curr_num is not None:
			if self.ctx.result is None:
				self.ctx.prev_num = self.ctx.get_result()
			else:
				self.ctx.result = None
				next_state = InitialState(self.ctx)

		self.ctx.curr_num = None
		self.ctx.operation = operation

		return next_state

	def get_display(self) -> str:
		raise NotImplementedError


class InitialState(RefactorState):
	def handle_digit(self, digit: int) -> IState:
		self.ctx.append_digit(digit)
		return self

	def get_display(self) -> str:
		num: int = coalesce(self.ctx.curr_num, self.ctx.prev_num, 0)
		return self.ctx.i2s(num)


class HasResultState(RefactorState):
	def handle_digit(self, digit: int) -> IState:
		self.ctx.reset()
		self.ctx.append_digit(digit)
		return InitialState(self.ctx)

	def get_display(self) -> str:
		return self.ctx.i2s(self.ctx.result)
