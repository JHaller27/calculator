Feature: AC operation
	Scenario: Input, then cleared
		Given a calculator
		 When 1 is entered
		  And calculator is cleared
		 Then the screen displays 0

	Scenario Outline: Input, cleared, then more input
		Given a calculator
		 When <buttons> are entered
		  And calculator is cleared
		  And <more_buttons> are entered
		 Then the screen displays <display>

		Examples:
			| buttons | more_buttons | display |
			| 1 | 2 | 2 |
			| 1+ | 2+ | 2 |
