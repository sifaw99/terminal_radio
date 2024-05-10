import subprocess
from rich import print
from rich.panel import Panel
from rich.console import Console
from rich.text import Text

class Fplay:
	def __init__(self,url,name):
		self.url = url
		self.name = name
	def handlePlaying(self):
		try:
			console = Console()
			cmd = ["ffplay", "-nodisp", "-i", "-loglevel", "error", "-vn", self.url]
			panel = Panel(Text(f"{self.name}",justify="center"), title= ":play_button:[bold yellow] Playing Now", subtitle= "[blink]:radio:", title_align="center", width=83)
			console.print(panel)
			subprocess.check_output(cmd)
		except:
			print("Exit Playing Radio")
