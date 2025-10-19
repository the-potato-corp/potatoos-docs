from pygments.lexers.shell import BashLexer

# TOTALLY not reskinned Bash
class MashLexer(BashLexer):
    name = "Mash"
    aliases = ["mash"]
    filenames = ["*.sm", "*.mash"]
    mimetypes = ["text/x-mash"]

def setup(app):
	app.add_lexer("mash", MashLexer)