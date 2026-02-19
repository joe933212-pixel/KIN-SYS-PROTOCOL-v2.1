from web3 import Web3

class PolygonWeb3Client:
    def __init__(self, infura_url):
        self.web3 = Web3(Web3.HTTPProvider(infura_url))

    def get_balance(self, address):
        """
        Get the balance of an account in Wei.
        Args:
            address (str): The address of the account.
        Returns:
            int: The balance in Wei.
        """
        balance = self.web3.eth.get_balance(address)
        return balance

    def send_transaction(self, from_address, to_address, value, private_key):
        """
        Send a transaction from one account to another.
        Args:
            from_address (str): The sender's address.
            to_address (str): The receiver's address.
            value (int): The amount to send in Wei.
            private_key (str): The private key of the sender's account.
        Returns:
            str: Transaction hash.
        """
        transaction = {
            'to': to_address,
            'value': value,
            'gas': 2000000,
            'gasPrice': self.web3.toWei('50', 'gwei'),
            'nonce': self.web3.eth.get_transaction_count(from_address),
        }
        signed_txn = self.web3.eth.account.sign_transaction(transaction, private_key)
        txn_hash = self.web3.eth.send_raw_transaction(signed_txn.rawTransaction)
        return txn_hash.hex()

    def contract_interaction(self, contract_address, abi, method_name, *args):
        """
        Interact with a smart contract.
        Args:
            contract_address (str): The contract's address.
            abi (list): The contract's ABI.
            method_name (str): The method to call.
            *args: Arguments for the method.
        Returns:
            any: The result of the method call.
        """
        contract = self.web3.eth.contract(address=contract_address, abi=abi)
        method = getattr(contract.functions, method_name)
        return method(*args).call()  

