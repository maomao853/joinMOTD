from mcdreforged.api.all import *

PLUGIN_METADATA = {
	'id': 'join_motd',
	'version': '1.1.0',
	'name': 'Join MOTD Display',
	'author': 'Fallen_Breath',
	'link': 'https://github.com/TISUnion/joinMOTD'
}

Prefix = '!!joinMOTD'
server_name = 'IFT-Survival'
main_server_name = 'IFT国际科技联盟'


def get_day(server: ServerInterface):
	api = server.get_plugin_instance('daycount')
	if hasattr(api, 'getday') and callable(api.getday):
		return api.getday()
	try:
		import daycount
		return daycount.getday()
	except Exception as e:
		server.logger.info(e)
		return '?'


def on_player_joined(server: ServerInterface, player, info):
	server.tell(player, '§7=======§r Welcome back to §e{}§7 =======§r'.format(server_name))
	server.tell(player, '今天是§e{}§r开服的第§e{}§r天'.format(main_server_name, get_day(server)))


def on_user_info(server, info):
	if info.content == Prefix:
		on_player_joined(server, info.player, None)


def on_load(server, old):
	server.register_help_message(Prefix, '显示欢迎消息')
