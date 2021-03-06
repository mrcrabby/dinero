from dinero import get_gateway
from dinero.exceptions import InvalidCustomerException
from dinero.log import log


class Customer(object):
    """
    A Customer resource. `Customer.create` uses the gateway to create a
    customer.  You can use this Customer object in calls to
    `Transaction.create`.
    """

    @classmethod
    @log
    def create(cls, gateway_name=None, **kwargs):
        gateway = get_gateway(gateway_name)
        resp = gateway.create_customer(kwargs)
        return cls(gateway_name=gateway.name, **resp)

    @classmethod
    @log
    def retrieve(cls, customer_id, gateway_name=None):
        gateway = get_gateway(gateway_name)
        resp = gateway.retrieve_customer(customer_id)
        # resp must have customer_id in it
        return cls(gateway_name=gateway.name, **resp)

    def __init__(self, gateway_name, customer_id, **kwargs):
        self.gateway_name = gateway_name
        self.customer_id = customer_id
        self.data = kwargs

    def update(self, options):
        for key, value in options.iteritems():
            setattr(self, key, value)

    @log
    def save(self):
        if not self.customer_id:
            raise InvalidCustomerException("Cannot save a customer that doesn't have a customer_id")
        gateway = get_gateway(self.gateway_name)
        gateway.update_customer(self.customer_id, self.data)
        return True

    @log
    def delete(self):
        if not self.customer_id:
            raise InvalidCustomerException("Cannot delete a customer that doesn't have a customer_id")
        gateway = get_gateway(self.gateway_name)
        gateway.delete_customer(self.customer_id)
        self.customer_id = None
        return True

    def to_dict(self):
        return vars(self)

    def __getattr__(self, attr):
        try:
            return self.data[attr]
        except KeyError as e:
            raise AttributeError(e)

    def __setattr__(self, attr, val):
        if attr in ['gateway_name', 'customer_id', 'data']:
            self.__dict__[attr] = val
        else:
            self.data[attr] = val

    @classmethod
    def from_dict(cls, dict):
        return cls(dict['gateway_name'],
                   dict['customer_id'],
                   **dict['data']
                   )

    def __repr__(self):
        return "Customer({gateway_name!r}, {customer_id!r}, **{data!r})".format(**self.to_dict())
