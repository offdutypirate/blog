Delete iptables rule
####################

:date: 2015-11-18 08:20
:modified: 2015-11-18 08:30
:tags: command line
:slug: delete-iptables-rule
:authors: Jon Moore
:summary: Short command to delete a single iptables rule

To delete an iptables rules you can edit `/etc/sysconfig/iptables` and remove
the rule and then reload iptables.  

You can also remove the rule using the `iptables` command
.. codeblock::

   $ iptables -D INPUT -s 198.51.100.232 -p tcp --dport 22 -j ACCEPT

Yet another way is to delete the rule based on the chain and the rule number
.. codeblock::

   $ iptables -D INPUT 3

When the chains are large it can be difficult to know the rule number.  The following will add line numbers
.. codeblock::

   $ iptables -L -vn --line-numbers INPUT