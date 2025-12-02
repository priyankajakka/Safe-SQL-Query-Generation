grammar SimpleSQL;

query
    : select_stmt EOF?
    ;

select_stmt
    : SELECT selectExpr fromExpr whereExpr?
      groupByExpr? orderByExpr? limitExpr?
    ;

selectExpr
    : select_item (',' select_item)*
    ;

select_item
    : expr (AS IDENT)?
    ;

fromExpr
    : FROM table_ref (',' table_ref)*
    ;

table_ref
    : simple_table join_sequence?
    ;

join_sequence
    : (join_op simple_table)+
    ;

simple_table
    : IDENT (AS IDENT)?
    | '(' select_stmt ')' (AS IDENT)?
    ;

join_op
    : (JOIN_TYPE)? JOIN ON bool_expr
    ;

JOIN_TYPE
    : LEFT | RIGHT | FULL | INNER
    ;

whereExpr
    : WHERE bool_expr
    ;

groupByExpr
    : GROUP BY expr (',' expr)*
    ;

orderByExpr
    : ORDER BY order_item (',' order_item)*
    ;

order_item
    : expr (ASC | DESC)?
    ;

limitExpr
    : LIMIT USER_DEFINED_NUMBER
    ;

bool_expr
    : bool_term (OR bool_term)*
    ;

bool_term
    : bool_factor (AND bool_factor)*
    ;

bool_factor
    : NOT bool_factor
    | comparison_predicate
    | '(' bool_expr ')'
    ;

comparison_predicate
    : expr comparison_op expr
    | expr IS NULL
    | expr IS NOT NULL
    | expr BETWEEN expr AND expr
    | expr IN '(' expr (',' expr)* ')'
    ;

comparison_op
    : '=' | '<>' | '!=' | '<' | '<=' | '>' | '>='
    ;

expr
    : additive_expr
    ;

additive_expr
    : multiplicative_expr (('+' | '-') multiplicative_expr)*
    ;

multiplicative_expr
    : unary_expr (('*' | '/') unary_expr)*
    ;

unary_expr
    : NOT unary_expr
    | primary_expr
    ;

primary_expr
    : literal
    | column_name
    | function_call
    | '(' expr ')'
    ;

function_call
    : IDENT '(' (expr (',' expr)* | '*')? ')'
    ;

column_name
    : IDENT ('.' IDENT)?
    ;

literal
    : USER_DEFINED_NUMBER
    | USER_DEFINED_STRING
    ;

SELECT : 'SELECT';
FROM : 'FROM';
WHERE : 'WHERE';
GROUP : 'GROUP';
BY : 'BY';
ORDER : 'ORDER';
ASC : 'ASC';
DESC : 'DESC';
JOIN : 'JOIN';
ON : 'ON';
LIMIT : 'LIMIT';
AND : 'AND';
OR : 'OR';
NOT : 'NOT';
AS : 'AS';
IS : 'IS';
NULL : 'NULL';
IN  : 'IN';
BETWEEN : 'BETWEEN';

LEFT : 'LEFT';
RIGHT : 'RIGHT';
FULL : 'FULL';
INNER : 'INNER';

USER_DEFINED_NUMBER : [0-9]+;
USER_DEFINED_STRING : '\'' (~'\'')* '\'';
IDENT : [a-zA-Z_] [a-zA-Z_0-9]*;
WS : [ \t\r\n]+ -> skip;
