"""
    pygments.lexers.cplint
    ~~~~~~~~~~~~~~~~~~~~~~

    Lexer for the cplint language https://cplint.eu, including CP-logic, Logic Programs with Annotated Disjunctions, 
    ProbLog and Distributional Clauses syntax

    :copyright: Copyright 2006-2022 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

import re

from pygments.lexer import bygroups, inherit, words
from pygments.lexers import PrologLexer
from pygments.token import Text, Comment, Operator, Keyword, Name, String, \
    Number, Punctuation

__all__ = ['CplintLexer']


class CplintLexer(PrologLexer):
    """
    Lexer for cplint files, https://cplint.eu, including CP-logic, Logic Programs with Annotated Disjunctions, 
    ProbLog and Distributional Clauses syntax
      .. versionadded:: 2.11
    """
    name = 'cplint'
    aliases = ['cplint']
    filenames = ['*.ecl', '*.prolog', '*.pro', '*.pl', '*.P', '*.lpad', '*.cpl']
    mimetypes = ['text/x-cplint']

    flags = re.UNICODE | re.MULTILINE

    tokens = {
        'root': [
            (words(('gaussian','uniform_dens','dirichlet','gamma','beta','poisson','binomial','geometric',
              'exponential','pascal','multinomial','user',
              'uniform','discrete','finite'), suffix=r'\b'),Name.Builtin),
            (r'([a-z]+)(:)', bygroups(String.Atom, Punctuation)),
            (r'::', Operator),
            (r':',  Operator),
            (r'~=', Operator),
            (r'~', Operator),
            (r'([a-z\u00c0-\u1fff\u3040-\ud7ff\ue000-\uffef]'
             r'[\w$\u00c0-\u1fff\u3040-\ud7ff\ue000-\uffef]*)'
             r'(\s*)(:=)',
             bygroups(Name.Function, Text, Operator)),  # function defn
             (r':=', Operator),
            inherit,
        ],
    }


