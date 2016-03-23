Dynamic
=======

Class to create dynamic objects.

Installation
------------

Install through **pip**.

::

    $ pip install dynamic

or get from source

::

    $ git clone https://github.com/gravmatt/py-dynamic.git
    $ cd py-dynamic
    $ python setup.py install

Import module
-------------

Import the module into your python project.

::

    from dynamic import Dynamic

Usage
-----

Create object when you need them.

::

    me = Dynamic()
    me.name = 'Rene'
    me.username = 'gravmatt'

    print '%s (%s)' % (me.name, me.username)

    # Rene (gravmatt)

Explicit Mode
~~~~~~~~~~~~~

By default the explicit is ON.

That means if you try to get a value that doesn't exists, a
AttributeError get raised.

::

    me = Dynamic()
    me.name = 'Rene'

    print me.age # age does not exist

    # AttributeError: Property 'age' not found

You can turn the explicit mode off, by:

::

    me = Dynamic(explicit=False)
    me.name = 'Rene'

    print 'My age:', me.age
    # My age: None

Now when you try to access a property that doesn't exists, ``None`` get
returned.

Licence
-------

The MIT License (MIT)

Copyright (c) 2016 René Tanczos

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
