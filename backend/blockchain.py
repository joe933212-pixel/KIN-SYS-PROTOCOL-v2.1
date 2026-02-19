import web3

class PolygonClient:
    def __init__(self, rpc_url):
        self.web3 = web3.Web3(web3.Web3.HTTPProvider(rpc_url))
        if not self.web3.isConnected():
            raise Exception("Unable to connect to the Polygon network")

    def get_balance(self, address):
        return self.web3.fromWei(self.web3.eth.get_balance(address), 'ether')

    def send_transaction(self, from_address, to_address, amount, private_key):
        nonce = self.web3.eth.getTransactionCount(from_address)
        gas_price = self.web3.eth.gas_price
        tx = {
            'nonce': nonce,
            'to': to_address,
            'value': self.web3.toWei(amount, 'ether'),
            'gas': 2000000,
            'gasPrice': gas_price,
        }

        signed_tx = self.web3.eth.account.sign_transaction(tx, private_key)
        tx_hash = self.web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        return self.web3.toHex(tx_hash)

    def estimate_gas(self, tx):
        return self.web3.eth.estimateGas(tx)

    def optimize_gas(self, from_address, to_address, amount):
        tx = {
            'from': from_address,
            'to': to_address,
            'value': self.web3.toWei(amount, 'ether'),
            'gas': 2000000,
        }
        return self.estimate_gas(tx)