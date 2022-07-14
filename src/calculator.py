from typing import Callable, Optional


def coalesce(*args):
	for a in args:
		if a is not None:
			return a


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
	_result: Optional[int]
	_prev_num: Optional[int]
	_curr_num: Optional[int]
	_operation: Optional[str]

	def __init__(self, precision: int = 3) -> None:
		self._precision = precision
		self._factor = 10**self._precision

		self._reset()

	def get_display(self) -> str:
		num: int = coalesce(self._result, self._curr_num, self._prev_num, 0)

		whole_part, decimal_part = divmod(num, self._factor)
		out_str = f'{whole_part}.{decimal_part}'.rstrip('0').rstrip('.')
		return out_str

	def _press_digit(self, digit: str) -> None:
		num = int(digit)
		assert len(digit) == 1

		if self._result is not None:
			self._reset()

		if self._curr_num is None:
			self._curr_num = 0

		self._curr_num = self._curr_num * 10 + (num * self._factor)

	def _press_operation(self, operation: str) -> None:
		if self._prev_num is None:
			self._prev_num = self._curr_num

		elif self._curr_num is not None:
			if self._result is None:
				self._prev_num = self._get_result()
			else:
				self._result = None

		self._curr_num = None
		self._operation = operation

	def _get_result(self) -> int:
		assert self._operation is not None and self._prev_num is not None and self._curr_num is not None
		op_func = _OP_FUNC_MAP[self._operation]
		result = op_func(self._prev_num, self._curr_num, self._factor)
		return result

	def _reset(self) -> None:
		self._result = None
		self._prev_num = None
		self._curr_num = None
		self._operation = None

	def press_button(self, button: str) -> None:
		if button.upper() == 'AC':
			self._reset()
			return

		if button == '=':
			self._result = self._get_result()
			self._prev_num = self._result
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
