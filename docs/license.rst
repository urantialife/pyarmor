.. _license:

License
=======

The software is distributed as Free To Use But Restricted. Free trial
version never expires, the limitations are

- The maximum size of code object is 32756 bytes in trial version
- The scripts obfuscated by trial version are not private. It means
  anyone could generate the license file which works for these
  obfuscated scripts.
- In trial version if obfuscating the Python scripts in advanced modes,
  the limitation is no more than about 32 functions (code objects) in
  one module.
- Without permission the trial version may not be used for the Python
  scripts of any commercial product.

About the license file of obfuscated scripts, refer to :ref:`The
License File for Obfuscated Script`

A registration code is required to obfuscate big code object or
generate private obfuscated scripts.

There are 2 basic types of licenses issued for the software. These are:

* A personal license for home users. The user purchases one license to
  use the software on his own computer.

  Home users may use their personal license to obfuscate all the
  python scripts which are property of the license owner, to generate
  private license files for the obfuscated scripts and distribute them
  and all the required files to any other machine or device.

  Home users could NOT obfuscate any python script which is NOT
  property of the license owner.

* A enterprise license for business users. The user purchases one
  license to use the software for one product serials of an
  organization.

  One product serials include the current version and any other latter
  versions of the same product.

  Business users may use their enterprise license on all computers and
  embedded devices to obfuscate all the python scripts of this product
  serials, to generate private license files for these obfuscated
  scripts and distribute them and all the required files to any other
  machine and device.

  Without permission of the software owner the license purchased for
  one product serials should not be used for other product
  serials. Business users should purchase new license for different
  product serials.

  In any case, the software is only used to obfuscate the Python scripts
  owned by the authorized person or enterprise. For example, if PyCharm
  purchases one license, it's no problem to obufscate any Python script
  of PyCharm self, but it's not allowed to apply this license to the Python
  scripts just written in the PyCharm by someone else.

Purchase
--------

To buy a license, please run command

    pyarmor register --buy

Or open the following url in any web browser

https://order.shareit.com/cart/add?vendorid=200089125&PRODUCT[300871197]=1

A registration file generally named "pyarmor-regcode-1.txt" will be sent by
email immediately after payment is completed successfully.

Save it to disk, then run the following command to register PyArmor

    pyarmor register /path/to/pyarmor-regcode-1.txt

Check the registration information:

    pyarmor register

After registration successfully, remove all the obfuscated scripts by trial
version, then obfuscate them again.

.. note::

    If the version of PyArmor < 6.5.2, please open the registration file
    "pyarmor-regcode-1.txt" by any text editor, following the guide in it to
    register PyArmor

.. important::

    The registration code is valid forever, it can be used permanently. But it
    may not work with new versions, although up to now it works with all of
    versions.

Upgrade Notes
-------------

The license purchased before **2017-10-10** don't support to upgrade the latest
version. A new license is required to use the latest version.

Technical Support
-----------------

There are 3 kinds of issues:

1. PyArmor defect.
2. The limitation of obfuscated scripts, or called known issues.
3. Wrong usage.

For example, use ``inspect`` to visit co_code of code object, use ``pdb`` to
trace obfuscated scripts. All of these don't work, they're known issues. Here
list all the known issues: :ref:`The Differences of Obfuscated Scripts`.

When reporting an issue, I'll tell which kind it is. For the first catalog, it's
my due to fix it. For the rests, it's your due to read the documentation and fix
it. I'll give you hints and maybe examples, but I could not help you to pyarmor
your scripts.

Suppose you purchase Microsoft Excel, and you want to make a complex chart. You
must learn the advanced features of Excel, then make this chart by yourself. You
can not ask Microsoft to make the complex chart for you.

The restrict mode is advanced feature of PyArmor, my due is to implement it as
described in the document, you need learn this advanced feature and refine you
code to adapt it. It's not my due to read your scripts and adapt your scripts
to restrict mode.

Q & A
-----

1. Single PyArmor license purchased can be used on various machines for
   obfuscation? or its valid only on one machine? Do we need to install license
   on single machine and distribute obfuscate code?

   | It can be used on various machines, but one license only for one product.

2. Single license can be used to obfuscate Python code that will run various
   platforms like windows, various Linux flavors?

   | For all the features of current version, it's yes. But in future versions,
   | I'm not sure one license could be used in all of platforms supported by
   | PyArmor.

3. How long the purchased license is valid for? is it life long?

   | It's life long. But I can't promise it will work for the future version of PyArmor.

4. Can we use the single license to obfuscate various versions of Python
   package/modules?

   | Yes, only if they're belong to one product.

5. Is there support provided in case of issues encountered?

   | Report issue in github or send email to me.

6. Does Pyarmor works on various Python versions?

   | Most of features work on Python27, and Python30~Python38, a few features
   | may only work for Python27, Python35 later.

7. Are there plans to maintain PyArmor to support future released Python
   versions?

   | Yes. The goal of PyArmor is let Python could be widely used in the
   | commercial softwares.

8. What is the mechanism in PyArmor to identify whether modules belong to same
   product? how it identifies product?

   | PyArmor could not identify it by itself, but I can check the obfuscated
   | scripts to find which registerred user distributes them. So I can find two
   | products are distributed by one same license.

9. If product undergoes revision ie. version changes, can same license be used
   or need new license?

   | Same license is OK.

10. What means a product serials under PyArmor EULA?

   | A product serial means a sale unit and its upgraded versions. For
   | example, AutoCAD 2003, 2010 could be taken as a product serials.

.. include:: _common_definitions.txt
