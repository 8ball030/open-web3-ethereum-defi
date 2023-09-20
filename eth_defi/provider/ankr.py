"""Ankr specific Web3.py functionality.

- Ankr has issues with some JSON-RPC access patterns.

.. warning ::

    We do not recommend using Ankr as it randomly returns empty responses to eth_call RPC method
    and this is not fixable at the client side.

See also :py:mod:`eth_defi.provider.broken_provider`.
"""
from web3 import Web3

from eth_defi.provider.named import get_provider_name


def is_ankr(web3: Web3) -> bool:
    """Are we connected to Ankr as a provider.

    We use this function to detect and activate Ankr workarounds
    for their bugs and features.
    """
    name = get_provider_name(web3.provider)
    return name == "rpc.ankr.com"
