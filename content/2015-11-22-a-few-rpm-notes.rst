A few RPM notes
####################

:date: 2015-11-22 09:20
:modified: 2015-11-26 08:30
:tags: command line
:category: short tips
:slug: a-few-rpm-notes
:authors: Jon Moore

Here is a collection of my notes on using RPM.  Most of these are well documented in man pages and other sources around the web.  I've collected the ones I've used most here as a reference for myself and others.  

Query package information
=========================

Show package information
------------------------

::

	$
	rpm -qi yum-cron
	Name        : yum-cron                     Relocations: (not relocatable)
	Version     : 3.2.29                            Vendor: CentOS
	Release     : 69.el6.centos                 Build Date: Fri 24 Jul 2015 05:28:06 AM CDT
	Install Date: Thu 03 Sep 2015 06:14:37 PM CDT      Build Host: c6b9.bsys.dev.centos.org
	Group       : System Environment/Base       Source RPM: yum-3.2.29-69.el6.centos.src.rpm
	Size        : 28204                            License: GPLv2+
	Signature   : RSA/SHA1, Fri 24 Jul 2015 03:43:15 PM CDT, Key ID 0946fca2c105b9de
	Packager    : CentOS BuildSystem <http://bugs.centos.org>
	URL         : http://yum.baseurl.org/
	Summary     : Files needed to run yum updates as a cron job
	Description :
	These are the files needed to run yum updates as a cron job.
	Install this package if you want auto yum updates nightly via cron.

Show pakage file list
------------------------

This shows all files included in a package.
::

	$ rpm -ql yum-cron
	/etc/cron.daily/0yum.cron
	/etc/rc.d/init.d/yum-cron
	/etc/sysconfig/yum-cron
	/etc/yum/yum-daily.yum
	/etc/yum/yum-weekly.yum
	/usr/share/doc/yum-cron-3.2.29
	/usr/share/doc/yum-cron-3.2.29/COPYING
	/usr/share/man/man8/yum-cron.8.gz

Show a packages configuration files
-----------------------------------

Similar to -q but only lists configuration files

::

	$  rpm -qc yum-cron
	/etc/sysconfig/yum-cron
	/etc/yum/yum-daily.yum
	/etc/yum/yum-weekly.yum

Show a packages documentation
-----------------------------

Similar to previous examples, but only shows documentation.

::

	$ rpm -qd yum-cron
	/usr/share/doc/yum-cron-3.2.29/COPYING
	/usr/share/man/man8/yum-cron.8.gz
