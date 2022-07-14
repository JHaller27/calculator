from istate import IState
from calculator import Calculator


def coalesce(*args):
	for a in args:
		if a is not None:
			return a


def i2s(num: int, precision_factor: int) -> str:
	whole_part, decimal_part = divmod(num, precision_factor)
	out_str = f'{whole_part}.{decimal_part}'.rstrip('0').rstrip('.')
	return out_str


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


class InitialState(BaseState):
	def handle_digit(self, digit: int) -> IState:
		if self.ctx.result is not None:
			self.ctx.reset()

		self.ctx.append_digit(digit)

		return self

	def handle_operator(self, operation: str) -> IState:
		if operation == '=':
			self.ctx.result = self.ctx.get_result()
			self.ctx.prev_num = self.ctx.result
			return self

		if self.ctx.prev_num is None:
			self.ctx.prev_num = self.ctx.curr_num

		elif self.ctx.curr_num is not None:
			if self.ctx.result is None:
				self.ctx.prev_num = self.ctx.get_result()
			else:
				self.ctx.result = None

		self.ctx.curr_num = None
		self.ctx.operation = operation

		return self

	def get_display(self) -> str:
		num: int = coalesce(self.ctx.result, self.ctx.curr_num, self.ctx.prev_num, 0)
		return i2s(num, self.ctx.factor)
