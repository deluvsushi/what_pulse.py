from requests import get


class WhatPulse:
	def __init__(self):
		self.api = "https://api.whatpulse.org"
		self.headers = {
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
		}

	def get_team_stats(self, team_name: str):
		return get(
			f"{self.api}/team.php?team={team_name}&format=json",
			headers=self.headers).json()

	def get_team_pulse_stats(self, team_name: str):
		return get(
			f"{self.api}/pulses.php?team={team_name}&format=json",
			headers=self.headers).json()

	def get_team_pulse_stats(self, user_id: str):
		return get(
			f"{self.api}/pulses.php?user={user_id}&format=json",
			headers=self.headers).json()

	def get_user_stats(self, user_id: int):
		return get(
			f"{self.api}/user.php?user={user_id}&format=json",
			headers=self.headers).json()
