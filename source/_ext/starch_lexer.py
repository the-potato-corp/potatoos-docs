from pygments.lexer import RegexLexer, bygroups, words, include
from pygments.token import *

class StarchLexer(RegexLexer):
	name = "STARCH"
	aliases = ["starch"]
	filenames = ["*.starch"]
	mimetypes = ["text/x-starch"]
	
	tokens = {
		"root": [
			include("comments"),
			include("keywords"),
			include("constants"),
			include("numbers"),
			include("strings"),
			include("operators"),
			include("functions"),
			include("types"),
			include("names"),
			(r"\s+", Text),
		],
		
		"comments": [
			(r"//.*?$", Comment.Single),
			(r"#.*?$", Comment.Single),
			(r"/\*", Comment.Multiline, "block-comment"),
			(r"<!--", Comment.Multiline, "html-comment"),
		],
		
		"block-comment": [
			(r"\*/", Comment.Multiline, "#pop"),
			(r"[^*]+", Comment.Multiline),
			(r"\*", Comment.Multiline),
		],
		
		"html-comment": [
			(r"-->", Comment.Multiline, "#pop"),
			(r"[^-]+", Comment.Multiline),
			(r"-", Comment.Multiline),
		],
		
		"keywords": [
			(words((
				"if", "elif", "else", "for", "in", "while", "match",
				"break", "continue", "return", "raise",
				"try", "catch", "as"
			), suffix=r"\b"), Keyword),
			
			(words((
				"function", "class", "enum", "extends"
			), suffix=r"\b"), Keyword.Declaration),
			
			(words((
				"var", "const"
			), suffix=r"\b"), Keyword.Declaration),
			
			(words((
				"using", "from"
			), suffix=r"\b"), Keyword.Namespace),
			
			(words((
				"and", "or", "not"
			), suffix=r"\b"), Operator.Word),
		],
		
		"constants": [
			(words((
				"true", "false", "null"
			), suffix=r"\b"), Keyword.Constant),
			
			# ALL_CAPS constants (like ANSWER, THE_NAME, UNIT_NEUTRAL)
			(r"\b[A-Z][A-Z0-9_]*\b", Name.Constant),
		],
		
		"numbers": [
			# Hex and binary
			(r"0x[0-9a-fA-F]+", Number.Hex),
			(r"0b[01]+", Number.Bin),
			
			# Floats (including scientific notation)
			(r"\d+\.\d*([eE][+-]?\d+)?", Number.Float),
			(r"\d+[eE][+-]?\d+", Number.Float),
			
			# Integers
			(r"\d+", Number.Integer),
		],
		
		"strings": [
			# String with interpolation support (if you add that later)
			(r'"', String.Double, "string-double"),
			(r"'", String.Single, "string-single"),
			(r"`", String.Backtick, "string-backtick"),
		],
		
		"string-double": [
			(r'\\"', String.Escape),
			(r'"', String.Double, "#pop"),
			(r"[^\"]+", String.Double),
		],
		
		"string-single": [
			(r"\\'", String.Escape),
			(r"'", String.Single, "#pop"),
			(r"[^']+", String.Single),
		],
		
		"string-backtick": [
			(r"\\`", String.Escape),
			(r"`", String.Backtick, "#pop"),
			(r"[^`]+", String.Backtick),
		],
		
		"operators": [
			# Pipeline (the star of the show)
			(r"~>", Operator.Word),
			
			# Range
			(r"\.\.", Operator),
			
			# Arrow (return type annotation)
			(r"->", Punctuation),
			
			# Comparison
			(r"==|!=|<=|>=|<|>|≈", Operator),
			
			# Assignment operators
			(r"\+=|-=|\*=|/=|%=|\^=", Operator),
			(r"=", Operator),
			
			# Arithmetic
			(r"[+\-*/%^]", Operator),
			
			# Concatenation/tilde
			(r"~", Operator),
			
			# Delimiters
			(r"[()[\]{},:;.]", Punctuation),
		],
		
		"types": [
			# Built-in types (colour them like Godot does)
			(words((
				"int", "float", "str", "bool", "void",
				"Vector2", "Vector3", "Vector4",
				"dict", "array", "list"
			), suffix=r"\b"), Keyword.Type),
		],
		
		"functions": [
			# Function definitions: function name(
			(r"(function)\s+([a-zA-Z_][a-zA-Z0-9_]*)(\s*)(\()",
			 bygroups(Keyword.Declaration, Name.Function, Text, Punctuation)),
			
			# Function calls: name(
			(r"([a-zA-Z_][a-zA-Z0-9_]*)(\s*)(\()",
			 bygroups(Name.Function, Text, Punctuation)),
		],
		
		"names": [
			# Type annotations after colons (var name: type)
			(r"(?<=:)\s*([a-zA-Z_][a-zA-Z0-9_]*)", Keyword.Type),
			
			# Enum members (inside braces after enum keyword)
			(r"(?<=\{)\s*([A-Z_][A-Z0-9_]*)", Name.Constant),
			
			# Regular identifiers
			(r"[a-zA-Z_][a-zA-Z0-9_]*", Name),
		],
	}

def setup(app):
	app.add_lexer("starch", StarchLexer)