import os
import sys
import time


class Shell:
	def __init__(self):
		os.system('cls')
		print('CMD bypass (Windows)')
		time.sleep(3)
		os.system('cls')

	def execute_command(self, command):
		if command.startswith('cd'):
			try:
				os.chdir(command.lstrip('cd '))
			except OSError:
				print('An error occured')
		return os.system(command)

	def main(self):
		while True:
			cmd = input(f'{os.getcwd()}> ')
			self.execute_command(cmd)


if __name__ == '__main__':
	s = Shell()
	s.main()