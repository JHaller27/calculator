Feature: Input digits

	Scenario Outline: Basic number entry
		Given a calculator
		 When <digits> are entered
		 Then the screen displays <display>

		Examples: Single digits
			| digits | display |
			| 1 | 1 |
			| 2 | 2 |
			| 3 | 3 |
			| 4 | 4 |
			| 5 | 5 |
			| 6 | 6 |
			| 7 | 7 |
			| 8 | 8 |
			| 9 | 9 |
			| 0 | 0 |

		Examples: Multiple digits
			| digits | display |
			| 123 | 123 |
			| 4567890 | 4567890 |
			| 0123 | 123 |
			| 000000 | 0 |
			| 100000 | 100000 |

