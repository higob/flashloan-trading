from brownie import FlashloanV1, accounts

AAVE_LENDING_POOL_ADDRESS_PROVIDER = "0x3632Bd7D50CcD2D0777414dd2C0cBFB6b0c44b8e"


def main():
    """
    Deploy a `FlashloanV1` contract from `accounts[0]`.
    """

    acct = accounts.load()  # add your keystore ID as an argument to this call

    flashloan = FlashloanV1.deploy(AAVE_LENDING_POOL_ADDRESS_PROVIDER, {"from": acct})
    return flashloan
