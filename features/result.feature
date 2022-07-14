Feature: Result operation
	Scenario Outline: Result op, best-case
		Given a calculator
		 When <buttons> are entered
		 Then the screen displays <display>

		Examples: Get result at end
			| buttons | display |
			| 2+1= | 3 |
			| 2+1======== | 10 |

		Examples: Get result then start new operation
			| buttons | display |
			| 2+1=40 | 40 |
			| 2+1=40+5 | 5 |
			| 2+1=40+5= | 45 |
			| 2+1=+ | 3 |
			| 2+1==+ | 4 |
			| 2+1==+6 | 6 |
			| 2+1==+6= | 10 |
