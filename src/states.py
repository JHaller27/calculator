from istate import IState
from calculator import Calculator


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

	def get_display(self) -> int:
		raise NotImplementedError


class InitialState(BaseState):
	def handle_digit(self, digit: int) -> IState:
		self.ctx.curr_num = 0
		self.ctx.append_digit(digit)
		return TypingFirstNumber(self.ctx)

	def handle_operator(self, op: str) -> IState:
		if op == '=':
			return self

		self.ctx.curr_num = 0

		self.ctx.store_operand()
		self.ctx.curr_num = None

		self.ctx.set_operation(op)

		return TypingOperator(self.ctx)

	def get_display(self) -> int:
		return 0


class TypingFirstNumber(BaseState):
	def handle_digit(self, digit: int) -> IState:
		self.ctx.append_digit(digit)
		return self

	def handle_operator(self, op: str) -> IState:
		self.ctx.store_operand()
		self.ctx.curr_num = None
		self.ctx.set_operation(op)
		return TypingOperator(self.ctx)

	def get_display(self) -> int:
		return self.ctx.curr_num


class TypingOperator(BaseState):
	def handle_digit(self, digit: int) -> IState:
		self.ctx.curr_num = 0
		self.ctx.append_digit(digit)
		return TypingSecondNumber(self.ctx)

	def handle_operator(self, op: str) -> IState:
		self.ctx.set_operation(op)
		return self

	def get_display(self) -> int:
		return self.ctx.prev_num


class TypingSecondNumber(BaseState):
	def handle_digit(self, digit: int) -> IState:
		self.ctx.append_digit(digit)
		return self

	def handle_operator(self, op: str) -> IState:
		self.ctx.store_result()
		if op == '=':
			return HasResultState(self.ctx)

		self.ctx.curr_num = None
		self.ctx.set_operation(op)
		return TypingOperator(self.ctx)

	def get_display(self) -> int:
		return self.ctx.curr_num


class HasResultState(BaseState):
	def handle_digit(self, digit: int) -> IState:
		self.ctx.reset()

		self.ctx.curr_num = 0
		self.ctx.append_digit(digit)

		return TypingFirstNumber(self.ctx)

	def handle_operator(self, op: str) -> IState:
		if op == '=':
			self.ctx.store_result()
			return self

		self.ctx.curr_num = None
		self.ctx.set_operation(op)
		return TypingOperator(self.ctx)

	def get_display(self) -> int:
		return self.ctx.prev_num
