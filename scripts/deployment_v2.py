from brownie import FlashloanV2, accounts, config, network

# AAVE_LENDING_POOL_ADDRESS_PROVIDER = "0x3632Bd7D50CcD2D0777414dd2C0cBFB6b0c44b8e"


def main():
    """
    Deploy a `FlashloanV2` contract from `accounts[0]`.
    """

    acct = accounts.add(
        config["wallets"]["from_key"]
    )  # add your keystore ID as an argument to this call

    flashloan = FlashloanV2.deploy(
        config["networks"][network.show_active()]["aave_lending_pool_v2"],
        {"from": acct},
    )
    return flashloan
