from mcdreforged.api.all import *

PLUGIN_METADATA = {
	'id': 'join_motd',
	'version': '1.1.0',
	'name': 'Join MOTD Display',
	'author': 'Fallen_Breath',
	'link': 'https://github.com/TISUnion/joinMOTD',
	'dependencies': {
		'mcdreforged': '>=1.0.0',
		'daycount': '*'
	}
}

Prefix = '!!joinMOTD'
server_name = 'IFT-survival'
main_server_name = 'IFT 国际科技联盟'
server_list = [
	'survival'
]


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
	messages = []
	for subServerName in server_list:
		command = '/server {}'.format(subServerName)
		messages.append(RText('[{}]'.format(subServerName)).h(command).c(RAction.run_command, command))

	server.tell(player, '§7=======§r Welcome back to §e{}§7 =======§r'.format(server_name))
	server.tell(player, '今天是§e{}§r开服的第§e{}§r天'.format(main_server_name, get_day(server)))
	server.tell(player, '§7-------§r Server List §7-------§r')
	server.tell(player, RTextBase.join(' ', messages))


def on_user_info(server, info):
	if info.content == Prefix:
		on_player_joined(server, info.player, None)


def on_load(server, old):
	server.register_help_message(Prefix, '显示欢迎消息')
