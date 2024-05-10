from pyradios import RadioBrowser
from rich.console import Console
from rich.table import Table
from rich import print
from src.fplay import Fplay

class Utilities:
	def __init__(self,name):
		self.name = name
	def searchRadio(self):
		try:
			stations = []
			stationsName = []
			table = Table(expand=False, header_style="bold magenta")
			rb = RadioBrowser()
			console = Console()
			searchResults = rb.search(name=self.name, order='votes', limit=40, reverse=True)
			#print(searchResults)
			table.add_column("ID", justify="left")
			table.add_column("Stations",justify="left")
			table.add_column("Country", justify="left")
			table.add_column("Tags", justify="left")
			table.add_column("Votes", justify="left")
			# Loop into Results to get radios infos
			for id, searchResult in enumerate(searchResults):
				stations.append(searchResult['url_resolved'])
				stationsName.append(searchResult['name'])
				table.add_row(str(id),searchResult['name'], searchResult['country'], searchResult['tags'], str(searchResult['votes']))
			if table.columns or stations != []:
				console.print(table)
				chosenStation = console.input("[bold red] Type the ID to play a station[/] ! :smiley: ")
				print(f" You entered the Id: {chosenStation}")
				#print(stations[int(chosenStation)])
				#print(stationsName[int(chosenStation)])
				playingUrl = Fplay(stations[int(chosenStation)],stationsName[int(chosenStation)])
				playingUrl.handlePlaying()
			else:
				 print("[i]No data...[/i]")
		except:
			print("Exit Playing Radio")
