Make JSON look pretty in Vim
############################

:date: 2015-11-30 12:00
:modified: 2015-11-30 12:00
:category: short tips
:slug: make-json-pretty-in-vim
:authors: Jon Moore
:tags: vim

Python 2.6+ has a nifty builtin json validator that can be used to print pretty json.  This can be used within Vim to make json easier to read.

::

    :%!python -m json.tool

Or, if you have a file with json in it, can be piped over the same

::

	cat output.json | python -m json.tool
