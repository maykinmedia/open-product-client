Developers
==========

Open product client library tries to implement the communication to the Open Product APIs
in a safe way. That is the reason that we want to implement everything with the help of
msgspec library, due to its speed and validation features.

Having that in mind, all the following contributions to the library should adhere to this
guideline. For now, only the basic endpoints (resources) for the ``producttypen`` API
are implemented. Each one of them has a specific ``msgspec.Struct`` attached to them, 
that describes the data (input and output).
