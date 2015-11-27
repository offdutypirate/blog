Publish Pelican blog to Github Pages
####################################

:date: 2015-11-16 08:00
:modified: 2015-11-16 08:00
:category: misc
:slug: publish-pelican-blog-to-gh-pages
:authors: Jon Moore

My reminder on how to get changes to offdutypirate.github.io.  These notes were created using mostly the `Pelican docs <http://docs.getpelican.com/en/3.6.3/tips.html#user-pages>`.

1. Commit changes

::
	
	$ git commit -m 'messages'
	$ git push

2. ghp-import
Update gh-pages branch

::
    
	$ ghp-import -m 'publish new blog' output

3. Push new blog to Github
Push the gh-pages branch to the master branch of offdutypirate.github.io repository.

::

	$ git push https://github.com/offdutypirate/offdutypirate.github.io.git gh-pages:master