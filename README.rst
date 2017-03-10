.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

==============================================================================
collective.behavior.relationleadimage
==============================================================================

This add-on represents a replacement for the default LeadImage Dexterity behavior.
It allows to select an existing Image content type item anywhere on the site, and store a relation to it on the object.  
This way, the same image item can be reused as a Lead Image for many News Items, or other content types that have this behavior enabled.

Features
--------

- Stores a relation to any Image content item on the site.
- Also provides a caption text field.
- Relation is used to display the image in any template that expects a Lead Image.


Examples
--------

This add-on can be seen in action at the following sites:
- http://deschuteslandtrust.org/hikes-events


Documentation
-------------

Full documentation for end users can be found in the "docs" folder.


Translations
------------

This product has been translated into

- No additional languages, yet.


Installation
------------

Install collective.behavior.relationleadimage by adding it to your buildout::

    [buildout]

    ...

    eggs =
        collective.behavior.relationleadimage


and then running ``bin/buildout``.
Restart your site, then go to the Add-ons control panel (``/prefs_install_products_form``),
and click **Install**.

Next, you will want to enable this behavior on some content types.
To do so, go to the _Dexterity Content Types_ control panel (``/@@dexterity-types``).
Click the desired content type (e.g. _News Item_), then click the _Behaviors_ tab.

- Check the box for the **Relation Lead Image** behavior.
- Make sure to **uncheck** the box for the **Lead Image** behavior 
(the two behaviors can not coexist on the same content type).
- Click **Save**

Repeat for any other content types, as desired.

Now, when you edit an item of the content type(s) on which this behavior is enabled,
you will be able to browse to any image already present on the site.
That image will then be used as the "Lead Image" for the item.


Contribute
----------

- Issue Tracker: https://github.com/collective/collective.behavior.relationleadimage/issues
- Source Code: https://github.com/collective/collective.behavior.relationleadimage


Support
-------

If you are having issues, please let us know by submitting an issue in GitHub's issue tracker listed above.


License
-------

The project is licensed under the GPLv2.
