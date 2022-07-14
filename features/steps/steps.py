from behave import *
from src.calculator import Calculator


@given('a calculator')
def _(ctx):
	ctx.calc = Calculator()


@when('{buttons} are entered')
def _(ctx, buttons):
	calc: Calculator = ctx.calc
	for button in buttons:
		calc.press_button(button)


@when('{button} is entered')
def _(ctx, button):
	calc: Calculator = ctx.calc
	calc.press_button(button)


@when('calculator is cleared')
def _(ctx):
	calc: Calculator = ctx.calc
	calc.press_button('AC')


@then('the screen displays {display}')
def _(ctx, display):
	calc: Calculator = ctx.calc
	result = calc.get_display()
	assert result == display
