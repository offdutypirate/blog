Satellite hammer cli notes
##########################

:date: 2015-12-09 08:00
:modified: 2015-12-09 08:00
:tags: command line, satellite
:category: short tips
:slug: satellite-hammer-notes
:authors: Jon Moore
:status: published

Here is a collection of my notes on using hammer cli with Red Hat Satellite.  Most of these things probably work with Katello also, but all of my testing is with Satellite.


Add new Product
---------------
Products are a group of repositories.  Content Hosts can subscribe to a product to make those repositories available.
::

	$ hammer product create --name="Product Name" --organization="Default Organization" --description="Description about Product"
	[Foreman] Username:
	[Foreman] Password for username:
	Product created
	$

Content View