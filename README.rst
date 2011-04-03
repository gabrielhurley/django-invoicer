===============
Django Invoicer
===============

A simple django app for managing invoices and generating attractive
printouts/PDFs using CSS and HTML templates.

Migrations
==========

Django Invoicer is fully compatible with south_ and will continue to
ship with migrations for all future versions.

.. _south: http://south.aeracode.org/

Settings
========

Django Invoicer uses a handful of additional settings to control
its behavior.

``INVOICES_PER_PAGE``
---------------------

:Default: 10

Integer used as the default number of items per page for pagination.

``INVOICER_UPLOAD_DIR``
-----------------------

:Default: ``invoicer``

The name of the directory in which user-uploaded media (stylesheets and
images) should be saved.
