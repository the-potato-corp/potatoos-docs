from pygments.lexers.shell import BashLexer

# TOTALLY not reskinned Bash
class SmashLexer(BashLexer):
    name = "Smash"
    aliases = ["smash"]
    filenames = ["*.sm", "*.smash"]
    mimetypes = ["text/x-smash"]

def setup(app):
	app.add_lexer("smash", SmashLexer)