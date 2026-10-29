=========
Changelog
=========

0.4.0 (2026-10-29)
==================

New features
------------

* Updated resources and their specific paths.
* Updated and added missing documentation.

0.3.0 (2026-10-22)
==================

New features
------------

* Added the basic resources and endpoints for the ``producttypen`` API (these will be 
  gradually updated according to the needs):
  
  - contentlabels
  - prijzen
  - producttypen
  - themas

0.2.3 (2022-11-22)
==================

Bugfixes
--------

* Fixed startup errors due to no configuration present.

Project maintenance
-------------------

* Added more gotcha's to the README.

0.2.2 (2022-10-03)
==================

Bugfixes
--------

* Fixed length of slugfield (default is now 100 instead of 50) which matches
  the slug length in Open Forms.

0.2.1 (2022-09-29)
==================

* Fixed various documentation issues.

0.2.0 (2022-09-29)
==================

Project maintenance
-------------------

* Added ``OpenFormsSlugField`` and renamed ``OpenFormsField`` to 
  ``OpenFormsUUIDField``.
* Added tests for templatetags.
* Fixed various documentation issues.


0.1.0 (2022-09-27)
==================

* Initial release
