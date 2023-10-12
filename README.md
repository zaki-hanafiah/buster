Buster (Zakhov's fork)
===================

Super simple, totally awesome, brute force **static site generator for**
`Ghost <http://ghost.org>`__.

Start with a clean, no commits Github repository.

*Generate Static Pages. Preview. Deploy to Github Pages.*

Warning! This project is a hack. It's not official. But it works for me.

About this fork
============

This is a work in progress containing many of the pull requests made to the
original buster repo (which unfortunately has been abandoned by its author).

It includes most of the changes by

* petemichel77
* Misiur
* Jeongseok Son
* raccoony
* leftofnull
* alokard
* dariosky
* skosch

It should also work with static pages (e.g. `about`, `tag/...`, etc.).

There may well be issues still, especially around Windows compatibility; I'm
happy to merge your PRs.

Installation
===========

Dependencies you may need:

- `pip install future`
- `pip install python-dateutil`
- `pip install gitdb2==2.0.0`
- `pip install GitPython==2.1.7`

With `pip` installed, simply run

``pip install git+https://github.com/zaki-hanafiah/buster``

You could also just clone the source and use the ``buster.py`` file directly.

*If you encounter any issues upon install, make sure to install the dependencies listed above.


The interface
-------------

``setup [--gh-repo=<repo-url>]``

      Creates a GIT repository inside ``static/`` directory.

``generate [--domain=<local-address>]``

      Generates static pages from locally running Ghost instance.

``preview``

      Preview what's generated on ``localhost:9000``.

``deploy``

      Commits and deploys changes static files to Github repository.

``add-domain <domain-name>``

      Adds CNAME file with custom domain name as required by Github
Pages.

Buster assumes you have ``static/`` folder in your current directory (or
creates one during ``setup`` command). You can specify custom directory
path using ``[--dir=<path>]`` option to any of the above commands.

Don't forget to change your blog URL in config.js in Ghost.

Requirements
------------

-  wget: Use ``brew install wget`` to install wget on your Mac.
   Available by default on most linux distributions.

-  git: Use ``brew install git`` to install git on your Mac.
   ``sudo apt-get install git`` on ubuntu/debian

The following python packages would be installed automatically when
installed via ``pip``:

-  `docopt <https://github.com/docopt/docopt>`__: Creates beautiful
   command line interfaces *easily*.
-  `GitPython <https://github.com/gitpython-developers/GitPython>`__:
   Python interface for GIT.

Ghost. What?
------------

`Ghost <http://ghost.org/features/>`__ is a beautifully designed,
completely customisable and completely `Open
Source <https://github.com/TryGhost/Ghost>`__ **Blogging Platform**. If
you haven't tried it out yet, check it out. You'll love it.

The Ghost Foundation is not-for-profit organization funding open source
software and trying to completely change the world of online publishing.
Consider `donating to Ghost <http://ghost.org/about/donate/>`__.

Buster?
~~~~~~~

Inspired by THE GhostBusters.

.. figure:: http://upload.wikimedia.org/wikipedia/en/c/c7/Ghostbusters_cover.png
   :alt: Ghost Buster Movie Poster

   Ghost Buster Movie

Contributing
------------

Checkout the existing `issues <https://github.com/skosch/buster/issues>`__ or create a new one.
 Pull requests welcome (actually, this time)!

