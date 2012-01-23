class Gateway(object):
    """
    Implemented payment gateways should implement this interface.
    """

    def charge(self, price, options):
        raise NotImplementedError

    def void(self, transaction):
        raise NotImplementedError

    def refund(self, transaction, amount):
        raise NotImplementedError

    def retrieve(self, transaction_id):
        raise NotImplementedError
