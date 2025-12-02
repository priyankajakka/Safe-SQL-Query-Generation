# Generated from SimpleSQL.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SimpleSQLParser import SimpleSQLParser
else:
    from SimpleSQLParser import SimpleSQLParser

# This class defines a complete listener for a parse tree produced by SimpleSQLParser.
class SimpleSQLListener(ParseTreeListener):

    # Enter a parse tree produced by SimpleSQLParser#query.
    def enterQuery(self, ctx:SimpleSQLParser.QueryContext):
        pass

    # Exit a parse tree produced by SimpleSQLParser#query.
    def exitQuery(self, ctx:SimpleSQLParser.QueryContext):
        pass


    # Enter a parse tree produced by SimpleSQLParser#select_stmt.
    def enterSelect_stmt(self, ctx:SimpleSQLParser.Select_stmtContext):
        pass

    # Exit a parse tree produced by SimpleSQLParser#select_stmt.
    def exitSelect_stmt(self, ctx:SimpleSQLParser.Select_stmtContext):
        pass


    # Enter a parse tree produced by SimpleSQLParser#selectExpr.
    def enterSelectExpr(self, ctx:SimpleSQLParser.SelectExprContext):
        pass

    # Exit a parse tree produced by SimpleSQLParser#selectExpr.
    def exitSelectExpr(self, ctx:SimpleSQLParser.SelectExprContext):
        pass


    # Enter a parse tree produced by SimpleSQLParser#select_item.
    def enterSelect_item(self, ctx:SimpleSQLParser.Select_itemContext):
        pass

    # Exit a parse tree produced by SimpleSQLParser#select_item.
    def exitSelect_item(self, ctx:SimpleSQLParser.Select_itemContext):
        pass


    # Enter a parse tree produced by SimpleSQLParser#fromExpr.
    def enterFromExpr(self, ctx:SimpleSQLParser.FromExprContext):
        pass

    # Exit a parse tree produced by SimpleSQLParser#fromExpr.
    def exitFromExpr(self, ctx:SimpleSQLParser.FromExprContext):
        pass


    # Enter a parse tree produced by SimpleSQLParser#table_ref.
    def enterTable_ref(self, ctx:SimpleSQLParser.Table_refContext):
        pass

    # Exit a parse tree produced by SimpleSQLParser#table_ref.
    def exitTable_ref(self, ctx:SimpleSQLParser.Table_refContext):
        pass


    # Enter a parse tree produced by SimpleSQLParser#join_sequence.
    def enterJoin_sequence(self, ctx:SimpleSQLParser.Join_sequenceContext):
        pass

    # Exit a parse tree produced by SimpleSQLParser#join_sequence.
    def exitJoin_sequence(self, ctx:SimpleSQLParser.Join_sequenceContext):
        pass


    # Enter a parse tree produced by SimpleSQLParser#simple_table.
    def enterSimple_table(self, ctx:SimpleSQLParser.Simple_tableContext):
        pass

    # Exit a parse tree produced by SimpleSQLParser#simple_table.
    def exitSimple_table(self, ctx:SimpleSQLParser.Simple_tableContext):
        pass


    # Enter a parse tree produced by SimpleSQLParser#join_op.
    def enterJoin_op(self, ctx:SimpleSQLParser.Join_opContext):
        pass

    # Exit a parse tree produced by SimpleSQLParser#join_op.
    def exitJoin_op(self, ctx:SimpleSQLParser.Join_opContext):
        pass


    # Enter a parse tree produced by SimpleSQLParser#whereExpr.
    def enterWhereExpr(self, ctx:SimpleSQLParser.WhereExprContext):
        pass

    # Exit a parse tree produced by SimpleSQLParser#whereExpr.
    def exitWhereExpr(self, ctx:SimpleSQLParser.WhereExprContext):
        pass


    # Enter a parse tree produced by SimpleSQLParser#groupByExpr.
    def enterGroupByExpr(self, ctx:SimpleSQLParser.GroupByExprContext):
        pass

    # Exit a parse tree produced by SimpleSQLParser#groupByExpr.
    def exitGroupByExpr(self, ctx:SimpleSQLParser.GroupByExprContext):
        pass


    # Enter a parse tree produced by SimpleSQLParser#orderByExpr.
    def enterOrderByExpr(self, ctx:SimpleSQLParser.OrderByExprContext):
        pass

    # Exit a parse tree produced by SimpleSQLParser#orderByExpr.
    def exitOrderByExpr(self, ctx:SimpleSQLParser.OrderByExprContext):
        pass


    # Enter a parse tree produced by SimpleSQLParser#order_item.
    def enterOrder_item(self, ctx:SimpleSQLParser.Order_itemContext):
        pass

    # Exit a parse tree produced by SimpleSQLParser#order_item.
    def exitOrder_item(self, ctx:SimpleSQLParser.Order_itemContext):
        pass


    # Enter a parse tree produced by SimpleSQLParser#limitExpr.
    def enterLimitExpr(self, ctx:SimpleSQLParser.LimitExprContext):
        pass

    # Exit a parse tree produced by SimpleSQLParser#limitExpr.
    def exitLimitExpr(self, ctx:SimpleSQLParser.LimitExprContext):
        pass


    # Enter a parse tree produced by SimpleSQLParser#bool_expr.
    def enterBool_expr(self, ctx:SimpleSQLParser.Bool_exprContext):
        pass

    # Exit a parse tree produced by SimpleSQLParser#bool_expr.
    def exitBool_expr(self, ctx:SimpleSQLParser.Bool_exprContext):
        pass


    # Enter a parse tree produced by SimpleSQLParser#bool_term.
    def enterBool_term(self, ctx:SimpleSQLParser.Bool_termContext):
        pass

    # Exit a parse tree produced by SimpleSQLParser#bool_term.
    def exitBool_term(self, ctx:SimpleSQLParser.Bool_termContext):
        pass


    # Enter a parse tree produced by SimpleSQLParser#bool_factor.
    def enterBool_factor(self, ctx:SimpleSQLParser.Bool_factorContext):
        pass

    # Exit a parse tree produced by SimpleSQLParser#bool_factor.
    def exitBool_factor(self, ctx:SimpleSQLParser.Bool_factorContext):
        pass


    # Enter a parse tree produced by SimpleSQLParser#comparison_predicate.
    def enterComparison_predicate(self, ctx:SimpleSQLParser.Comparison_predicateContext):
        pass

    # Exit a parse tree produced by SimpleSQLParser#comparison_predicate.
    def exitComparison_predicate(self, ctx:SimpleSQLParser.Comparison_predicateContext):
        pass


    # Enter a parse tree produced by SimpleSQLParser#comparison_op.
    def enterComparison_op(self, ctx:SimpleSQLParser.Comparison_opContext):
        pass

    # Exit a parse tree produced by SimpleSQLParser#comparison_op.
    def exitComparison_op(self, ctx:SimpleSQLParser.Comparison_opContext):
        pass


    # Enter a parse tree produced by SimpleSQLParser#expr.
    def enterExpr(self, ctx:SimpleSQLParser.ExprContext):
        pass

    # Exit a parse tree produced by SimpleSQLParser#expr.
    def exitExpr(self, ctx:SimpleSQLParser.ExprContext):
        pass


    # Enter a parse tree produced by SimpleSQLParser#additive_expr.
    def enterAdditive_expr(self, ctx:SimpleSQLParser.Additive_exprContext):
        pass

    # Exit a parse tree produced by SimpleSQLParser#additive_expr.
    def exitAdditive_expr(self, ctx:SimpleSQLParser.Additive_exprContext):
        pass


    # Enter a parse tree produced by SimpleSQLParser#multiplicative_expr.
    def enterMultiplicative_expr(self, ctx:SimpleSQLParser.Multiplicative_exprContext):
        pass

    # Exit a parse tree produced by SimpleSQLParser#multiplicative_expr.
    def exitMultiplicative_expr(self, ctx:SimpleSQLParser.Multiplicative_exprContext):
        pass


    # Enter a parse tree produced by SimpleSQLParser#unary_expr.
    def enterUnary_expr(self, ctx:SimpleSQLParser.Unary_exprContext):
        pass

    # Exit a parse tree produced by SimpleSQLParser#unary_expr.
    def exitUnary_expr(self, ctx:SimpleSQLParser.Unary_exprContext):
        pass


    # Enter a parse tree produced by SimpleSQLParser#primary_expr.
    def enterPrimary_expr(self, ctx:SimpleSQLParser.Primary_exprContext):
        pass

    # Exit a parse tree produced by SimpleSQLParser#primary_expr.
    def exitPrimary_expr(self, ctx:SimpleSQLParser.Primary_exprContext):
        pass


    # Enter a parse tree produced by SimpleSQLParser#function_call.
    def enterFunction_call(self, ctx:SimpleSQLParser.Function_callContext):
        pass

    # Exit a parse tree produced by SimpleSQLParser#function_call.
    def exitFunction_call(self, ctx:SimpleSQLParser.Function_callContext):
        pass


    # Enter a parse tree produced by SimpleSQLParser#column_name.
    def enterColumn_name(self, ctx:SimpleSQLParser.Column_nameContext):
        pass

    # Exit a parse tree produced by SimpleSQLParser#column_name.
    def exitColumn_name(self, ctx:SimpleSQLParser.Column_nameContext):
        pass


    # Enter a parse tree produced by SimpleSQLParser#literal.
    def enterLiteral(self, ctx:SimpleSQLParser.LiteralContext):
        pass

    # Exit a parse tree produced by SimpleSQLParser#literal.
    def exitLiteral(self, ctx:SimpleSQLParser.LiteralContext):
        pass



del SimpleSQLParser