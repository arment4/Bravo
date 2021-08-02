string	\"[^\n"]+\"

ws	[ \t]+

alpha	[A-Za-z]
dig	[0-9]
name	({alpha}|{dig}|\$)({alpha}|{dig}|\_|\.|\-|\/|\$)*
num1	[-+]?{dig}+\.?([eE][-+]?{dig}+)?
num2	[-+]?{dig}*\.{dig}+([eE][-+]?{dig}+)?
number	{num1}|{num2}
%%
"int"|"var"|"short"|"long"|"float"|"double"|"mat"|"string"|"char"|"bool"|"byte" { printf("variable ");}

{ws}	/* skip blanks and tabs */

{number}	{ printf("number ");}

{name}		{ printf("name ");}

{string}	{ printf("string ");}


%%

main() {
	/* code */
	yylex();
}
