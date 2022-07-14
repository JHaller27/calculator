from typing import Callable, Optional
import states


OpFuncType = Callable[[int, int, int], int]


def _add(x: int, y: int, factor: int) -> int:
	return x + y

def _sub(x: int, y: int, factor: int) -> int:
	return x - y

def _mult( x: int, y: int, factor: int) -> int:
	return (x * y) // factor

def _div(x: int, y: int, factor: int) -> int:
	q, r =  divmod(x, y)
	decimal = round(r * 10 // (y // factor), -1) // 10  # r*10 then //10 to get next digit, to use for rounding
	return q * factor + decimal


_OP_FUNC_MAP: dict[str, OpFuncType] = {
	'+': _add,
	'-': _sub,
	'x': _mult,
	'/': _div,
}


class Calculator:
	result: Optional[int]
	prev_num: Optional[int]
	curr_num: Optional[int]
	_operation: Optional[OpFuncType]
	_state: states.IState

	def __init__(self, precision: int = 3) -> None:
		self._precision = precision
		self._factor = 10**self._precision
		self._state = states.InitialState(self)

		self.reset()

	@property
	def factor(self) -> int:
		return self._factor

	def i2s(self, num: int) -> str:
		whole_part, decimal_part = divmod(num, self.factor)
		out_str = f'{whole_part}.{decimal_part}'.rstrip('0').rstrip('.')
		return out_str

	def get_display(self) -> str:
		return self._state.get_display()

	def _press_digit(self, digit: str) -> None:
		digit = int(digit)
		self._state = self._state.handle_digit(digit)

	def _press_operation(self, operation: str) -> None:
		self._state = self._state.handle_operator(operation)

	def append_digit(self, digit: int) -> None:
		if self.curr_num is None:
			self.curr_num = 0
		self.curr_num = self.curr_num * 10 + (digit * self._factor)

	def set_operation(self, operation: str) -> None:
		self._operation = _OP_FUNC_MAP[operation]

	def get_result(self) -> int:
		assert self._operation is not None and self.prev_num is not None and self.curr_num is not None
		result = self._operation(self.prev_num, self.curr_num, self._factor)
		return result

	def reset(self) -> None:
		self.result = None
		self.prev_num = None
		self.curr_num = None
		self._operation = None

	def press_button(self, button: str) -> None:
		if button.upper() == 'AC':
			self.reset()
			return

		try:
			self._press_digit(button)
		except ValueError:
			self._press_operation(button)


if __name__ == '__main__':
	calc = Calculator()
	n = int(input())
	for _ in range(n):
		raw = input()
		calc.press_button(raw)
		print(calc.get_display())
