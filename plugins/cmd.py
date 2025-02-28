from plugin_base import PluginBase
from telethon import TelegramClient, events, types
from telethon.tl.functions.messages import SendReactionRequest
import subprocess

class CommandLineExecutor:
    def execute(self, command):
        return subprocess.run(command, shell=True, capture_output=True)
    
class Cmd(PluginBase):
    description = "Execute shell commands on .cmd command"
    enabled = True
    
    executor = CommandLineExecutor()

    def __init__(self, api) -> None:
        super().__init__(api)
        
    async def on_command(self, event, args) -> str:
        if args[0] == "cmd" or args[0] == "shell" or args[0] == "exec":
            output = ""
            try:
                output = output + str(self.executor.execute(args[1]).stdout.decode('utf-8'))
                output = output + str(self.executor.execute(args[1]).stderr.decode('utf-8'))
            except Exception as e:
                output = e
            return output