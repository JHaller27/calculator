Feature: Input operation
	Scenario Outline: Input, best-case
		Given a calculator
		 When <buttons> are entered
		 Then the screen displays <display>

		Examples: Digit then operation
			| buttons | display |
			| 1+ | 1 |
			| 123+ | 123 |
			| 123- | 123 |
			| 123x | 123 |
			| 123/ | 123 |

		Examples: Digits, operation, then digits
			| buttons | display |
			| 1+1 | 1 |
			| 1+23 | 23 |
			| 1-23 | 23 |
			| 1x23 | 23 |
			| 1/23 | 23 |

		Examples: Two operations
			| buttons | display |
			| 1+23+ | 24 |
			| 1+23- | 24 |
			| 1+23x | 24 |
			| 1+23/ | 24 |

		Examples: Two operations then a number
			| buttons | display |
			| 1+23+34 | 34 |
			| 1+23-34 | 34 |
			| 1+23x34 | 34 |
			| 1+23/34 | 34 |

		Examples: Many many operations
			| buttons | display |
			| 1+2+3+4+5+6+7+8+ | 36 |
			| 1+2+3+4+5+6+7+8+9 | 9 |

		Examples: Order of operations
			| buttons | display |
			| 2+3x5+ | 25 |
			| 3-2x5+ | 5 |
			| 2+3/5+ | 1 |

	Scenario Outline: Changed mind
		Given a calculator
		 When <buttons> are entered
		 Then the screen displays <display>

		Examples:
			| buttons | display |
			| 3+-2+ | 1 |
			| 3-1+x5 | 5 |
			| 3-1+x5+ | 10 |
