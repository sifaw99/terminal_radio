from rich import print
from rich import print
from rich.panel import Panel
from src.args import arguments



def main():
	welcome = Panel(
		"""
	📻 Play any radios around the globe :globe_showing_europe-africa: right from this Terminal [yellow]:zap:[/yellow]!
	😄 Author: Lahcen Ouchary
	🐛 Visit: https://github.com/sifaw99/terminal_radio to submit issues
	⭐ Show some love by starring the project on GitHub ❤️
	❌ Press Ctrl+C to quit
		""",
		title="[b]RADIO STATION[/b]",
		width=85,
		expand=True,
		safe_box=True,
	)


	print(welcome)
	arguments()

if __name__=="__main__":
	main()