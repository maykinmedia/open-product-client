Testing
=======

The current implementation is tested against a docker container, which is fed with some
test data. The container is configured according to a live version (image) of Open Product
and we support this specific one (see :doc:`README <readme>` file). You can see the
settings for the container inside the `docker-compose file <https://github.com/maykinmedia/open-product-client/blob/main/docker-compose.yaml>`_

We are using VCR tests which record cassettes against the real instance. This helps us
to be sure that our test data adhere to the real APIs. These tests should be re-recorded
when there are changes and during each major release cycle. A helpful script exists for
this and you can see it `here <https://github.com/maykinmedia/open-product-client/blob/main/re_record_vcr_cassettes.sh>`_.


.. note::

    In case you need to modify the test data this should be done in a safe way for all the 
    developers. Each change should be commited as a patch (git), so we can track all the
    changes.
