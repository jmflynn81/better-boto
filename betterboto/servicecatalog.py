import types
import logging

from .utils import slurp


logger = logging.getLogger(__file__)


def search_products_as_admin_single_page(self, **kwargs):
    """
    This will continue to call search_products_as_admin until there are no more pages left to retrieve.  It will return
    the aggregated response in the same structure as search_products_as_admin does.

    :param self: servicecatalog client
    :param kwargs: these are passed onto the search_products_as_admin method call
    :return: servicecatalog_client.search_products_as_admin.response
    """
    return slurp(
        'search_products_as_admin',
        self.search_products_as_admin,
        'ProductViewDetails',
        **kwargs
    )


def list_portfolios_single_page(self, **kwargs):
    """
    This will continue to call list_portfolios until there are no more pages left to retrieve.  It will return
    the aggregated response in the same structure as list_portfolios does.

    :param self: servicecatalog client
    :param kwargs: these are passed onto the list_portfolios method call
    :return: servicecatalog_client.list_portfolios.response
    """
    return slurp(
        'list_portfolios',
        self.list_portfolios,
        'PortfolioDetails',
        **kwargs
    )


def list_provisioning_artifacts_single_page(self, **kwargs):
    """
    This will continue to call list_provisioning_artifacts until there are no more pages left to retrieve.  It will return
    the aggregated response in the same structure as list_provisioning_artifacts does.

    :param self: servicecatalog client
    :param kwargs: these are passed onto the list_provisioning_artifacts method call
    :return: servicecatalog_client.list_provisioning_artifacts.response
    """
    return slurp(
        'list_provisioning_artifacts',
        self.list_provisioning_artifacts,
        'ProvisioningArtifactDetails',
        **kwargs
    )


def list_portfolios_for_product_single_page(self, **kwargs):
    """
    This will continue to call list_portfolios_for_product until there are no more pages left to retrieve.  It will return
    the aggregated response in the same structure as list_portfolios_for_product does.

    :param self: servicecatalog client
    :param kwargs: these are passed onto the list_portfolios_for_product method call
    :return: servicecatalog_client.list_portfolios_for_product.response
    """
    return slurp(
        'list_portfolios_for_product',
        self.list_portfolios_for_product,
        'PortfolioDetails',
        **kwargs
    )


def list_provisioned_product_plans_single_page(self, **kwargs):
    """
    This will continue to call list_provisioned_product_plans until there are no more pages left to retrieve.  It will return
    the aggregated response in the same structure as list_provisioned_product_plans does.

    :param self: servicecatalog client
    :param kwargs: these are passed onto the list_provisioned_product_plans method call
    :return: servicecatalog_client.list_provisioned_product_plans.response
    """
    return slurp(
        'list_provisioned_product_plans',
        self.list_provisioned_product_plans,
        'ProvisionedProductPlans',
        **kwargs
    )

def search_provisioned_products_single_page(self, **kwargs):
    """
    This will continue to call search_provisioned_products until there are no more pages left to retrieve.  It will return
    the aggregated response in the same structure as search_provisioned_products does.

    :param self: servicecatalog client
    :param kwargs: these are passed onto the search_provisioned_products method call
    :return: servicecatalog_client.search_provisioned_products.response
    """
    return slurp(
        'search_provisioned_products',
        self.search_provisioned_products,
        'ProvisionedProducts',
        **kwargs
    )

def list_launch_paths_single_page(self, **kwargs):
    """
    This will continue to call list_launch_paths until there are no more pages left to retrieve.  It will return
    the aggregated response in the same structure as list_launch_paths does.

    :param self: servicecatalog client
    :param kwargs: these are passed onto the list_launch_paths method call
    :return: servicecatalog_client.list_launch_paths.response
    """
    return slurp(
        'list_launch_paths',
        self.list_launch_paths,
        'LaunchPathSummaries',
        **kwargs
    )


def make_better(client):
    client.search_products_as_admin_single_page = types.MethodType(search_products_as_admin_single_page, client)
    client.list_portfolios_single_page = types.MethodType(list_portfolios_single_page, client)
    client.list_provisioning_artifacts_single_page = types.MethodType(list_provisioning_artifacts_single_page, client)
    client.list_portfolios_for_product_single_page = types.MethodType(list_portfolios_for_product_single_page, client)
    client.list_provisioned_product_plans_single_page = types.MethodType(list_provisioned_product_plans_single_page, client)
    client.search_provisioned_products_single_page = types.MethodType(search_provisioned_products_single_page, client)
    client.list_launch_paths_single_page = types.MethodType(list_launch_paths_single_page, client)
    return client
