class Testpaper:
	
	def __init__(self, subject, markscheme, pass_mark):
		self.subject = subject
		self.markscheme = markscheme
		self.pass_mark = pass_mark
	

class Student:


	def __init__(self):
		self.tests_taken = "No tests taken"

	def take_test(self, paper, choices):
		correct_answers = [i for i in range(len(choices)) if choices[i] in paper.markscheme]
		percentage = round(len(correct_answers)/len(paper.markscheme)*100)
		if percentage > int(paper.pass_mark.replace('%','')):
			test_result = "Passed!"
		test_result = "Failed!"

		if self.tests_taken == str:
			self.tests_taken = {paper.subject: "{} ({}%)".format(test_result, percentage) }
		self.tests_taken[paper.subject] = "{} ({}%)".format(test_result, percentage)


